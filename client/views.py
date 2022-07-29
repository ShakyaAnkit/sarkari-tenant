from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.views.generic import (TemplateView, View, CreateView, UpdateView, ListView, DetailView,DeleteView, FormView)
from django.shortcuts import get_object_or_404, render
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from django.contrib.messages.views import SuccessMessageMixin
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.urls import reverse

from tenant_schemas.utils import schema_context

from .forms import *
from .mixins import *

class DashboardView(RootClientMixin, AuthMixin, TemplateView):
	template_name = 'client/index.html'

class LoginPage(RootClientMixin, TemplateView):
	template_name = "client/auth/login.html"

	def dispatch(self, request, *args, **kwargs):
		if 'next' in self.request.GET:
			self.next_page = self.request.GET['next']
		else:
			self.next_page = reverse('client:dashboard')
		return super().dispatch(request, *args, **kwargs)

	def post(self, request):
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			form = LoginForm()
			if user is not None:
				if user.is_active:
					if user.is_superuser:
						login(request, user)
						return HttpResponseRedirect(self.next_page)
			
			# return HttpResponseRedirect(reverse('client:login'))
			messages.add_message(self.request, messages.ERROR, 'Username and password doesn\'t match')

			return render(request, self.template_name, 
			{'form':form,'user': username, 'error': 'Incorrect username or password'})


class LogoutView(RootClientMixin,View):

	def get(self, request):
		logout(request)
		return HttpResponseRedirect(reverse('client:login'))


class ClientListView(RootClientMixin, AuthMixin, ListView):
	template_name = "client/clients/list.html"
	context_object_name = "object_list"
	queryset = Client.objects.all().order_by('-created_at')

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		# context['requested'] = RequestedClient.objects.exclude(accepted_at=None)
		return context

class ClientCreateView(AuthMixin, SuccessMessageMixin, RootClientMixin,CreateView):
	template_name = "client/clients/form.html"
	form_class= ClientForm
	model = Client
	success_url = reverse_lazy('client:clients-list')
	success_message = "Client Created Successfully"

	def form_valid(self, form):
		return super().form_valid(form)

class ClientUpdateView(AuthMixin, SuccessMessageMixin,RootClientMixin, UpdateView):
	template_name = "client/clients/form.html"
	model = Client
	form_class = ClientForm
	success_url = reverse_lazy('client:clients-list')
	success_message = "Client Updated Successfully"

class ClientUserCreateView(AuthMixin, RootClientMixin, DetailView, FormView):
	template_name = "client/clients/form.html"
	model = Client
	form_class = ClientUserCreateForm
	success_url = reverse_lazy('client:clients-list')
	
	def form_valid(self, form):
		client = self.get_object()
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')

		with schema_context(client.schema_name):
			if not User.objects.filter(username=username).exists():
			
				user = User(username=username, is_active=True, is_staff=True, is_superuser=True)
				user.set_password(password)
				user.save()
				messages.success(self.request, 'User created successfully')
			else:
				messages.warning(self.request, 'User already Exists')
				
		return super().form_valid(form)

	def form_invalid(self, form):
		messages.error(self.request, 'User creation failed')
		return redirect(self.success_url)

class ClientDeleteView(AuthMixin, SuccessMessageMixin,RootClientMixin,DeleteView):
	model = Client
	success_url = reverse_lazy('client:clients-list')
	success_message = "Client Deleted Successfully"

	def get(self, request, *args, **kwargs):
		return self.delete(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super().delete(request, *args, **kwargs)
	

class RequestedClientListView(AuthMixin, RootClientMixin,ListView):
	template_name = "client/dashboard/requests/requestedclientlist.html"
	context_object_name = "object_list"
	queryset = RequestedClient.objects.all().order_by('-created_at')

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args , **kwargs)
		context['new_requests'] = RequestedClient.objects.filter(accepted_at=None, rejected_at=None).count()
		return context

class RequestedClientCreateView(SuccessMessageMixin,RootClientMixin, CreateView):
	template_name = "client/dashboard/requests/clientcreate.html"
	form_class= RequestedClientForm
	model = RequestedClient
	success_url = reverse_lazy('crm_app:welcome')
	success_message = "Your request has been sent Successfully"

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)


class AcceptClientView(AuthMixin, View):
	def get(self, request, **kwargs):
		clientId=self.kwargs['pk']
		clientObj=RequestedClient.objects.get(pk=clientId)
		clientObj.accepted_at = timezone.now()
		clientObj.save()
		domain_url = get_object_or_404(Client, schema_name='public')
		client = Client.objects.create(name=clientObj.name, domain_url = clientObj.subdomain + '.' + domain_url.domain_url, schema_name=clientObj.subdomain)
		
		return redirect('client:clientupdate', pk=client.pk)

class RejectClientView(AuthMixin,RootClientMixin, View):
	def get(self, request, **kwargs):
		clientId=self.kwargs['pk']
		clientObj=RequestedClient.objects.get(pk=clientId)
		clientObj.rejected_at = timezone.now()
		clientObj.save()

		return HttpResponseRedirect('/requestedclient/list')

