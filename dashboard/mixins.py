from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import View, FormView

from .audit import store_audit, get_audit_key

class AuthMixin(LoginRequiredMixin):
	login_url = reverse_lazy('dashboard:login')

class SuperAdminRequiredMixin(AuthMixin):
	def dispatch(self, request, *args, **kwargs):
		if self.request.user.is_superuser:
			return super().dispatch(request, *args, **kwargs)
		return self.handle_no_permission()

class GuestMixin(object):
	redirect_url = reverse_lazy('dashboard:index')
	login_url = reverse_lazy('dashboard:login')

	def dispatch(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return super().dispatch(request, *args, **kwargs)
		return redirect(self.redirect_url)


class LoginMixin(GuestMixin, FormView):

	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(self.request, user)
				store_audit('', user, get_audit_key('LOGIN'), self.request)
				return redirect(self.redirect_url)

		messages.add_message(self.request, messages.ERROR, 'Username and password doesn\'t match')
		return redirect(self.login_url)


class LogoutMixin(AuthMixin, View):
	def get(self, request):
		store_audit('', request.user, get_audit_key('LOGOUT'), self.request)
		logout(request)
		return redirect(self.login_url)


# CRUD MIXINS

class NonDeletedListMixin:
	def get_queryset(self):
		return super().get_queryset().filter(deleted_at__isnull=True)

class CreateAuditMixin:
	def form_valid(self, form):
		form.instance.created_by = self.request.user
		obj = form.save()
		store_audit('', obj, get_audit_key('CREATE'), self.request)
		return super().form_valid(form)

class UpdateAuditMixin:
	def form_valid(self, form):
		prev_obj = self.get_object()
		obj = form.save()
		store_audit(prev_obj, obj, get_audit_key('UPDATE'), self.request)
		return super().form_valid(form)

class DeleteAuditMixin:
	def get(self, request, *args, **kwargs):
		return self.delete(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		if hasattr(self, 'success_message') and self.success_message:
			messages.success(self.request, self.success_message)
		store_audit('', self.get_object(), get_audit_key('DELETE'), self.request)
		return super().delete(request, *args, **kwargs)