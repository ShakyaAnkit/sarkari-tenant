import json

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.crypto import get_random_string
from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView

from .forms import *
from .models import *
from .mixins import (LoginMixin, LogoutMixin, AuthMixin, SuperAdminRequiredMixin,
						NonDeletedListMixin, CreateAuditMixin, UpdateAuditMixin, DeleteAuditMixin)

# Create your views here.
class LoginView(LoginMixin):
	template_name = 'dashboard/auth/login.html'
	form_class = LoginForm

class LogoutView(LogoutMixin):
	pass


# Extra Mixins

class RootContentMixin:
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['config'] = SiteConfig.get_instance()
		return context

# Dashboard Index
class DashboardIndex(RootContentMixin, AuthMixin, TemplateView):
	template_name = 'dashboard/index.html'



# User CRUD
class UserListView(RootContentMixin, SuperAdminRequiredMixin, ListView):
    model = User
    template_name = "dashboard/users/list.html"
    paginate_by = 100

    def get_queryset(self):
        return super().get_queryset().exclude(username=self.request.user)

class UserCreateView(RootContentMixin, SuperAdminRequiredMixin, SuccessMessageMixin, CreateView):
    form_class= UserForm
    success_message = "User Created Successfully"
    success_url = reverse_lazy('dashboard:users-list')
    template_name = "dashboard/users/form.html"

    def get_success_url(self):
        return reverse('dashboard:users-password-reset', kwargs={'pk': self.object.pk })

class UserUpdateView(RootContentMixin, SuperAdminRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = UserForm
    model = User
    success_message = "User Updated Successfully"
    success_url = reverse_lazy('dashboard:users-list')
    template_name = "dashboard/users/form.html"

class UserStatusView(RootContentMixin, SuperAdminRequiredMixin, SuccessMessageMixin, View):
    model = User
    success_message = "User's Status Has Been Changed Successfully"
    success_url = reverse_lazy('dashboard:users-list')

    def get(self, request, *args, **kwargs):
        user_id = self.kwargs['pk']
        if user_id:
            account = User.objects.filter(pk=user_id).first()
            if account.is_active == True:
                account.is_active = False
            else:
                account.is_active = True
            account.save(update_fields=['is_active'])
        return redirect(self.success_url)


# Password Reset
class UserPasswordResetView(RootContentMixin, SuperAdminRequiredMixin, SuccessMessageMixin, View):
	model = User
	success_url = reverse_lazy("dashboard:users-list")
	success_message = "Password has been sent to the user's email."

	def get(self, request, *args, **kwargs):
		# gettings user details
		user_pk = self.kwargs["pk"]
		account = User.objects.filter(pk=user_pk).first()
		password = get_random_string(length=10)
		account.set_password(password)

		# getting site config
		config = SiteConfig.get_instance()

		# sending mail
		msg = "You can login into the {} dashboard with the following credentials.\n\n".format(config.website_title) + "Username: " + account.username + " \n" + "Password: " + password
		send_mail("Your password for {} has been created".format(config.website_title), msg, settings.EMAIL_HOST_USER, [account.email], fail_silently=True)
		
		# updating password
		account.save(update_fields=["password"])
		messages.success(self.request, self.success_message)
		return redirect(self.success_url)



# Notices
class NoticeListView(NonDeletedListMixin, RootContentMixin, AuthMixin, ListView):
	template_name = "dashboard/notices/list.html"
	queryset = Notice.objects.all().order_by('-created_at')

	def get(self, *args, **kwargs):
		Notice.objects.filter(notice_date=None).update(notice_date=F('created_at'))
		return super().get(*args, **kwargs)

class NoticeCreateView(CreateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, CreateView):
	template_name = "dashboard/notices/form.html"
	form_class= NoticeForm
	model = Notice
	success_url = reverse_lazy('dashboard:notices-list')
	success_message = "Notice created Successfully"

class NoticeUpdateView(UpdateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, UpdateView):
	template_name = "dashboard/notices/form.html"
	model = Notice
	form_class = NoticeForm
	success_url = reverse_lazy('dashboard:notices-list')
	success_message = "Notice updated Successfully"

class NoticeDeleteView(DeleteAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, DeleteView):
	model = Notice
	success_url = reverse_lazy('dashboard:notices-list')
	success_message = "Notice deleted Successfully"

class NoticeDetailView(RootContentMixin, AuthMixin, DetailView):
    model = Notice
    template_name = 'dashboard/notices/detail.html'

# PressReleases
class PressReleaseListView(NonDeletedListMixin, RootContentMixin, AuthMixin, ListView):
	template_name = "dashboard/press-releases/list.html"
	queryset = PressRelease.objects.all().order_by('-created_at')

class PressReleaseCreateView(CreateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, CreateView):
	template_name = "dashboard/press-releases/form.html"
	form_class= PressReleaseForm
	model = PressRelease
	success_url = reverse_lazy('dashboard:press-releases-list')
	success_message = "Press Release created Successfully"

class PressReleaseUpdateView(UpdateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, UpdateView):
	template_name = "dashboard/press-releases/form.html"
	model = PressRelease
	form_class = PressReleaseForm
	success_url = reverse_lazy('dashboard:press-releases-list')
	success_message = "Press Release updated Successfully"

class PressReleaseDeleteView(DeleteAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, DeleteView):
	model = PressRelease
	success_url = reverse_lazy('dashboard:press-releases-list')
	success_message = "Press Release deleted Successfully"

class PressReleaseDetailView(RootContentMixin, AuthMixin, DetailView):
    model = PressRelease
    template_name = 'dashboard/press-releases/detail.html'

# Bid
class BidListView(NonDeletedListMixin, RootContentMixin, AuthMixin, ListView):
	template_name = "dashboard/bids/list.html"
	queryset = Bid.objects.all().order_by('-created_at')

class BidCreateView(CreateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, CreateView):
	template_name = "dashboard/bids/form.html"
	form_class= BidForm
	model = Bid
	success_url = reverse_lazy('dashboard:bids-list')
	success_message = "Bid created Successfully"

class BidUpdateView(UpdateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, UpdateView):
	template_name = "dashboard/bids/form.html"
	model = Bid
	form_class = BidForm
	success_url = reverse_lazy('dashboard:bids-list')
	success_message = "Bid updated Successfully"

class BidDeleteView(DeleteAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, DeleteView):
	model = Bid
	success_url = reverse_lazy('dashboard:bids-list')
	success_message = "Bid deleted Successfully"

class BidDetailView(RootContentMixin, AuthMixin, DetailView):
    model = Bid
    template_name = 'dashboard/bids/detail.html'

# Publication
class PublicationListView(NonDeletedListMixin, RootContentMixin, AuthMixin, ListView):
	template_name = "dashboard/publications/list.html"
	queryset = Publication.objects.all().order_by('-created_at')

class PublicationCreateView(CreateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, CreateView):
	template_name = "dashboard/publications/form.html"
	form_class= PublicationForm
	model = Publication
	success_url = reverse_lazy('dashboard:publications-list')
	success_message = "Publication created Successfully"

class PublicationUpdateView(UpdateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, UpdateView):
	template_name = "dashboard/publications/form.html"
	model = Publication
	form_class = PublicationForm
	success_url = reverse_lazy('dashboard:publications-list')
	success_message = "Publication updated Successfully"

class PublicationDeleteView(DeleteAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, DeleteView):
	model = Publication
	success_url = reverse_lazy('dashboard:publications-list')
	success_message = "Publication deleted Successfully"

class PublicationDetailView(RootContentMixin, AuthMixin, DetailView):
    model = Publication
    template_name = 'dashboard/publications/detail.html'

# Policy
class PolicyListView(NonDeletedListMixin, RootContentMixin, AuthMixin, ListView):
	template_name = "dashboard/policies/list.html"
	queryset = Policy.objects.all().order_by('-created_at')

class PolicyCreateView(CreateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, CreateView):
	template_name = "dashboard/policies/form.html"
	form_class= PolicyForm
	model = Policy
	success_url = reverse_lazy('dashboard:policies-list')
	success_message = "Policy created Successfully"

class PolicyUpdateView(UpdateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, UpdateView):
	template_name = "dashboard/policies/form.html"
	model = Policy
	form_class = PolicyForm
	success_url = reverse_lazy('dashboard:policies-list')
	success_message = "Policy updated Successfully"

class PolicyDeleteView(DeleteAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, DeleteView):
	model = Policy
	success_url = reverse_lazy('dashboard:policies-list')
	success_message = "Policy deleted Successfully"

class PolicyDetailView(RootContentMixin, AuthMixin, DetailView):
    model = Policy
    template_name = 'dashboard/policies/detail.html'

# Download
class DownloadListView(NonDeletedListMixin, RootContentMixin, AuthMixin, ListView):
	template_name = "dashboard/downloads/list.html"
	queryset = Download.objects.all().order_by('-created_at')

class DownloadCreateView(CreateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, CreateView):
	template_name = "dashboard/downloads/form.html"
	form_class= DownloadForm
	model = Download
	success_url = reverse_lazy('dashboard:downloads-list')
	success_message = "Download created Successfully"

class DownloadUpdateView(UpdateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, UpdateView):
	template_name = "dashboard/downloads/form.html"
	model = Download
	form_class = DownloadForm
	success_url = reverse_lazy('dashboard:downloads-list')
	success_message = "Download updated Successfully"

class DownloadDeleteView(DeleteAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, DeleteView):
	model = Download
	success_url = reverse_lazy('dashboard:downloads-list')
	success_message = "Download deleted Successfully"

class DownloadDetailView(RootContentMixin, AuthMixin, DetailView):
    model = Download
    template_name = 'dashboard/downloads/detail.html'

# Project
class ProjectListView(NonDeletedListMixin, RootContentMixin, AuthMixin, ListView):
	template_name = "dashboard/projects/list.html"
	queryset = Project.objects.all().order_by('-created_at')

class ProjectCreateView(CreateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, CreateView):
	template_name = "dashboard/projects/form.html"
	form_class= ProjectForm
	model = Project
	success_url = reverse_lazy('dashboard:projects-list')
	success_message = "Project created Successfully"

class ProjectUpdateView(UpdateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, UpdateView):
	template_name = "dashboard/projects/form.html"
	model = Project
	form_class = ProjectForm
	success_url = reverse_lazy('dashboard:projects-list')
	success_message = "Project updated Successfully"

class ProjectDeleteView(DeleteAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, DeleteView):
	model = Project
	success_url = reverse_lazy('dashboard:projects-list')
	success_message = "Project deleted Successfully"

class ProjectDetailView(RootContentMixin, AuthMixin, DetailView):
    model = Project
    template_name = 'dashboard/projects/detail.html'

# Event
class EventListView(NonDeletedListMixin, RootContentMixin, AuthMixin, ListView):
	template_name = "dashboard/events/list.html"
	queryset = Event.objects.all().order_by('-created_at')

class EventCreateView(CreateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, CreateView):
	template_name = "dashboard/events/form.html"
	form_class= EventForm
	model = Event
	success_url = reverse_lazy('dashboard:events-list')
	success_message = "Event created Successfully"

class EventUpdateView(UpdateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, UpdateView):
	template_name = "dashboard/events/form.html"
	model = Event
	form_class = EventForm
	success_url = reverse_lazy('dashboard:events-list')
	success_message = "Event updated Successfully"

class EventDeleteView(DeleteAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, DeleteView):
	model = Event
	success_url = reverse_lazy('dashboard:events-list')
	success_message = "Event deleted Successfully"

class EventDetailView(RootContentMixin, AuthMixin, DetailView):
    model = Event
    template_name = 'dashboard/events/detail.html'

# News
class NewsListView(NonDeletedListMixin, RootContentMixin, AuthMixin, ListView):
	template_name = "dashboard/news/list.html"
	queryset = News.objects.all().order_by('-created_at')

class NewsCreateView(CreateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, CreateView):
	template_name = "dashboard/news/form.html"
	form_class= NewsForm
	model = News
	success_url = reverse_lazy('dashboard:news-list')
	success_message = "News created Successfully"

class NewsUpdateView(UpdateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, UpdateView):
	template_name = "dashboard/news/form.html"
	model = News
	form_class = NewsForm
	success_url = reverse_lazy('dashboard:news-list')
	success_message = "News updated Successfully"

class NewsDeleteView(DeleteAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, DeleteView):
	model = News
	success_url = reverse_lazy('dashboard:news-list')
	success_message = "News deleted Successfully"

class NewsDetailView(RootContentMixin, AuthMixin, DetailView):
    model = News
    template_name = 'dashboard/news/detail.html'

# HR
class HRListView(NonDeletedListMixin, RootContentMixin, AuthMixin, ListView):
	template_name = "dashboard/hr/list.html"
	queryset = HR.objects.filter(deleted_at__isnull=True)

class HRSortView(ListView):
	model = HR
	success_url = reverse_lazy('dashboard:hr-list')

	def get(self, request, *args, **kwargs):
		print(self.request.GET.get('ids'))
		if self.request.GET.get('ids'):
			ids = json.loads(self.request.GET.get('ids'))
			for element in self.model.objects.filter(pk__in=ids):
				element.priority = ids.index(element.pk)
				element.save()
		return JsonResponse({ 'success': True }, status=200)

class HRCreateView(CreateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, CreateView):
	template_name = "dashboard/hr/form.html"
	form_class= HRForm
	model = HR
	success_url = reverse_lazy('dashboard:hr-list')
	success_message = "HR created Successfully"

class HRUpdateView(UpdateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, UpdateView):
	template_name = "dashboard/hr/form.html"
	model = HR
	form_class = HRForm
	success_url = reverse_lazy('dashboard:hr-list')
	success_message = "HR updated Successfully"

class HRDeleteView(DeleteAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, DeleteView):
	model = HR
	success_url = reverse_lazy('dashboard:hr-list')
	success_message = "HR deleted Successfully"

class HRDetailView(RootContentMixin, AuthMixin, DetailView):
    model = HR
    template_name = 'dashboard/hr/detail.html'

# Slider
class SliderListView(NonDeletedListMixin, RootContentMixin, AuthMixin, ListView):
	template_name = "dashboard/sliders/list.html"
	queryset = Slider.objects.all().order_by('-created_at')

class SliderCreateView(CreateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, CreateView):
	template_name = "dashboard/sliders/form.html"
	form_class= SliderForm
	model = Slider
	success_url = reverse_lazy('dashboard:sliders-list')
	success_message = "Slider created Successfully"

class SliderUpdateView(UpdateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, UpdateView):
	template_name = "dashboard/sliders/form.html"
	model = Slider
	form_class = SliderForm
	success_url = reverse_lazy('dashboard:sliders-list')
	success_message = "Slider updated Successfully"

class SliderDeleteView(DeleteAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, DeleteView):
	model = Slider
	success_url = reverse_lazy('dashboard:sliders-list')
	success_message = "Slider deleted Successfully"

class SliderDetailView(RootContentMixin, AuthMixin, DetailView):
    model = Slider
    template_name = 'dashboard/sliders/detail.html'

# Album
class AlbumListView(NonDeletedListMixin, RootContentMixin, AuthMixin, ListView):
	template_name = "dashboard/albums/list.html"
	queryset = Album.objects.all().order_by('-created_at')

class AlbumCreateView(CreateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, CreateView):
	template_name = "dashboard/albums/form.html"
	form_class= AlbumForm
	model = Album
	success_url = reverse_lazy('dashboard:albums-list')
	success_message = "Album created Successfully"

	def form_valid(self, form):
		response = super().form_valid(form)

		if self.request.FILES.getlist('photos'):
			# for multiple images
			for photo in self.request.FILES.getlist('photos'):
				photo_form = AlbumPhotoForm(data=None, files={'photo': photo})
				if photo_form.is_valid():
					photo_form.instance.album = form.instance
					photo_form.instance.created_by = self.request.user
					photo_form.save()
		return response

class AlbumUpdateView(UpdateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, UpdateView):
	template_name = "dashboard/albums/form.html"
	model = Album
	form_class = AlbumForm
	success_url = reverse_lazy('dashboard:albums-list')
	success_message = "Album updated Successfully"

	def get_form(self):
		form = super().get_form()
		form.fields.pop('photos')
		return form

class AlbumDeleteView(DeleteAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, DeleteView):
	model = Album
	success_url = reverse_lazy('dashboard:albums-list')
	success_message = "Album deleted Successfully"


# AlbumPhoto
class AlbumPhotoMixin:
	def get_album(self):
		if hasattr(self, 'album'):
			return self.album	
		self.album = Album.objects.filter(pk=self.kwargs.get('album_pk')).first()
		return self.album

	def get_success_url(self):
		if self.request.POST.get('continue'):
			return reverse_lazy('dashboard:albums-photos-create', kwargs = {
				'album_pk' : self.get_album().pk
			})
		return reverse_lazy('dashboard:albums-photos-list', kwargs={
			'album_pk': self.get_album().pk
		})

	def get_queryset(self):
		return super().get_queryset().filter(album=self.get_album())

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['album'] = self.get_album()
		return context
	
	def form_valid(self, form):
		form.instance.album = self.get_album()
		return super().form_valid(form)	

class AlbumPhotoListView(AlbumPhotoMixin, NonDeletedListMixin, RootContentMixin, AuthMixin, ListView):
	template_name = "dashboard/albums/photos/list.html"
	queryset = AlbumPhoto.objects.all().order_by('-created_at')

class AlbumPhotoCreateView(AlbumPhotoMixin, CreateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, CreateView):
	template_name = "dashboard/albums/photos/form.html"
	form_class= AlbumPhotosForm
	model = AlbumPhoto
	success_url = reverse_lazy('dashboard:albums-photos-list')
	success_message = "Photo created Successfully"

	def form_valid(self, form):
		if self.request.FILES.getlist('photos'):
			# for multiple images
			for photo in self.request.FILES.getlist('photos'):
				photo_form = AlbumPhotoForm(data=None, files={'photo': photo})
				if photo_form.is_valid():
					photo_form.instance.album = self.get_album()
					photo_form.instance.created_by = self.request.user
					photo_form.save()
		return redirect(self.get_success_url())

class AlbumPhotoUpdateView(AlbumPhotoMixin, UpdateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, UpdateView):
	template_name = "dashboard/albums/photos/form.html"
	model = AlbumPhoto
	form_class = AlbumPhotoForm
	success_url = reverse_lazy('dashboard:albums-photos-list')
	success_message = "Photo updated Successfully"

class AlbumPhotoDeleteView(AlbumPhotoMixin, DeleteAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, DeleteView):
	model = AlbumPhoto
	success_url = reverse_lazy('dashboard:albums-photos-list')
	success_message = "Photo deleted Successfully"


# Department
class DepartmentListView(NonDeletedListMixin, RootContentMixin, AuthMixin, ListView):
	template_name = "dashboard/departments/list.html"
	queryset = Department.objects.all().order_by('-created_at')

class DepartmentCreateView(CreateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, CreateView):
	template_name = "dashboard/departments/form.html"
	form_class= DepartmentForm
	model = Department
	success_url = reverse_lazy('dashboard:departments-list')
	success_message = "Department created Successfully"

class DepartmentUpdateView(UpdateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, UpdateView):
	template_name = "dashboard/departments/form.html"
	model = Department
	form_class = DepartmentForm
	success_url = reverse_lazy('dashboard:departments-list')
	success_message = "Department updated Successfully"

class DepartmentDeleteView(DeleteAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, DeleteView):
	model = Department
	success_url = reverse_lazy('dashboard:departments-list')
	success_message = "Department deleted Successfully"

class DepartmentDetailView(RootContentMixin, AuthMixin, DetailView):
    model = Department
    template_name = 'dashboard/departments/detail.html'

# UsefulLink
class UsefulLinkListView(NonDeletedListMixin, RootContentMixin, AuthMixin, ListView):
	template_name = "dashboard/useful-links/list.html"
	queryset = UsefulLink.objects.all().order_by('-created_at')

class UsefulLinkCreateView(CreateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, CreateView):
	template_name = "dashboard/useful-links/form.html"
	form_class= UsefulLinkForm
	model = UsefulLink
	success_url = reverse_lazy('dashboard:useful-links-list')
	success_message = "Useful Link created Successfully"

class UsefulLinkUpdateView(UpdateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, UpdateView):
	template_name = "dashboard/useful-links/form.html"
	model = UsefulLink
	form_class = UsefulLinkForm
	success_url = reverse_lazy('dashboard:useful-links-list')
	success_message = "Useful Link updated Successfully"

class UsefulLinkDeleteView(DeleteAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, DeleteView):
	model = UsefulLink
	success_url = reverse_lazy('dashboard:useful-links-list')
	success_message = "Useful Link deleted Successfully"

class UsefulLinkDetailView(RootContentMixin, AuthMixin, DetailView):
    model = UsefulLink
    template_name = 'dashboard/useful-links/detail.html'

# Message
class MessageListView(NonDeletedListMixin, RootContentMixin, AuthMixin, ListView):
	template_name = "dashboard/messages/list.html"
	queryset = Message.objects.all().order_by('-created_at')

class MessageCreateView(CreateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, CreateView):
	template_name = "dashboard/messages/form.html"
	form_class= MessageForm
	model = Message
	success_url = reverse_lazy('dashboard:messages-list')
	success_message = "Message created Successfully"

class MessageUpdateView(UpdateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, UpdateView):
	template_name = "dashboard/messages/form.html"
	model = Message
	form_class = MessageForm
	success_url = reverse_lazy('dashboard:messages-list')
	success_message = "Message updated Successfully"

class MessageDeleteView(DeleteAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, DeleteView):
	model = Message
	success_url = reverse_lazy('dashboard:messages-list')
	success_message = "Message deleted Successfully"

class MessageDetailView(RootContentMixin, AuthMixin, DetailView):
    model = Message
    template_name = 'dashboard/messages/detail.html'

# Page
class PageListView(NonDeletedListMixin, RootContentMixin, AuthMixin, ListView):
	template_name = "dashboard/pages/list.html"
	queryset = Page.objects.all().order_by('-created_at')

class PageCreateView(CreateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, CreateView):
	template_name = "dashboard/pages/form.html"
	form_class= PageForm
	model = Page
	success_url = reverse_lazy('dashboard:pages-list')
	success_message = "Page created Successfully"

class PageUpdateView(UpdateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, UpdateView):
	template_name = "dashboard/pages/form.html"
	model = Page
	form_class = PageForm
	success_url = reverse_lazy('dashboard:pages-list')
	success_message = "Page updated Successfully"

class PageDeleteView(DeleteAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, DeleteView):
	model = Page
	success_url = reverse_lazy('dashboard:pages-list')
	success_message = "Page deleted Successfully"

class PageDetailView(RootContentMixin, AuthMixin, DetailView):
    model = Page
    template_name = 'dashboard/pages/detail.html'

# Navbar
class NavbarListView(NonDeletedListMixin, RootContentMixin, AuthMixin, ListView):
	template_name = "dashboard/navbar/list.html"
	queryset = Navbar.objects.all().select_related('parent')

class NavbarSortView(ListView):
	model = Navbar
	success_url = reverse_lazy('dashboard:navbar-list')

	def get(self, request, *args, **kwargs):
		print(self.request.GET.get('ids'))
		if self.request.GET.get('ids'):
			ids = json.loads(self.request.GET.get('ids'))
			for element in self.model.objects.filter(pk__in=ids):
				element.priority = ids.index(element.pk)
				element.save()
		return JsonResponse({ 'success': True }, status=200)

class NavbarCreateView(CreateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, CreateView):
	template_name = "dashboard/navbar/form.html"
	form_class= NavbarForm
	model = Navbar
	success_url = reverse_lazy('dashboard:navbar-list')
	success_message = "Navbar created Successfully"

class NavbarUpdateView(UpdateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, UpdateView):
	template_name = "dashboard/navbar/form.html"
	model = Navbar
	form_class = NavbarForm
	success_url = reverse_lazy('dashboard:navbar-list')
	success_message = "Navbar updated Successfully"

class NavbarDeleteView(DeleteAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, DeleteView):
	model = Navbar
	success_url = reverse_lazy('dashboard:navbar-list')
	success_message = "Navbar deleted Successfully"


class NavbarDetailView(RootContentMixin, AuthMixin, DetailView):
    model =  Navbar
    template_name = 'dashboard/navbar/detail.html'

# HomePagePopup
class HomePagePopupListView(NonDeletedListMixin, RootContentMixin, AuthMixin, ListView):
	template_name = "dashboard/home-page-popup/list.html"
	queryset = HomePagePopup.objects.all().order_by('-created_at')

class HomePagePopupCreateView(CreateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, CreateView):
	template_name = "dashboard/home-page-popup/form.html"
	form_class= HomePagePopupForm
	model = HomePagePopup
	success_url = reverse_lazy('dashboard:home-page-popup-list')
	success_message = "Home Page Popup created Successfully"

class HomePagePopupUpdateView(UpdateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, UpdateView):
	template_name = "dashboard/home-page-popup/form.html"
	model = HomePagePopup
	form_class = HomePagePopupForm
	success_url = reverse_lazy('dashboard:home-page-popup-list')
	success_message = "Home Page Popup updated Successfully"

class HomePagePopupDeleteView(DeleteAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, DeleteView):
	model = HomePagePopup
	success_url = reverse_lazy('dashboard:home-page-popup-list')
	success_message = "Home Page Popup deleted Successfully"


class HomePagePopupDetailView(RootContentMixin, AuthMixin, DetailView):
    model =  HomePagePopup
    template_name = 'dashboard/home-page-popup/detail.html'

class HomePagePopupStatusChangeView(RootContentMixin, AuthMixin, DetailView):
	model =  HomePagePopup

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		self.object.is_active = self.request.POST.get('is_active') == 'true'
		self.object.save(update_fields=['is_active'])
		return JsonResponse({
			'is_active': self.object.is_active,
		})

# SiteConfig
class SiteConfigListView(NonDeletedListMixin, RootContentMixin, AuthMixin, DetailView):
	template_name = "dashboard/site-config/detail.html"

	def get_object(self):
		return SiteConfig.get_instance()

class SiteConfigUpdateView(UpdateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, UpdateView):
	template_name = "dashboard/site-config/form.html"
	model = SiteConfig
	form_class = SiteConfigForm
	success_url = reverse_lazy('dashboard:site-config-list')
	success_message = "Site config updated Successfully"

	def get_object(self):
		return SiteConfig.get_instance()



# List
class ListListView(NonDeletedListMixin, RootContentMixin, AuthMixin, ListView):
	template_name = "dashboard/list/list.html"
	queryset = List.objects.all().order_by('-created_at')

class ListCreateView(CreateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, CreateView):
	template_name = "dashboard/list/form.html"
	form_class= ListForm
	model = List
	success_url = reverse_lazy('dashboard:list-list')
	success_message = "List created Successfully"

class ListUpdateView(UpdateAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, UpdateView):
	template_name = "dashboard/list/form.html"
	model = List
	form_class = ListForm
	success_url = reverse_lazy('dashboard:list-list')
	success_message = "List updated Successfully"

class ListDeleteView(DeleteAuditMixin, RootContentMixin, AuthMixin, SuccessMessageMixin, DeleteView):
	model = List
	success_url = reverse_lazy('dashboard:list-list')
	success_message = "List deleted Successfully"

class ListDetailView(RootContentMixin, AuthMixin, DetailView):
    model = List
    template_name = 'dashboard/list/detail.html'