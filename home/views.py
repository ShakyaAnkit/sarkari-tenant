from django.contrib import messages
from django.db.models import Q, F, Count, Prefetch
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse as response
from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, RedirectView, CreateView, View, ListView, DetailView
from django.views.generic.edit import FormView
from django.conf import settings

from client.mixins import TenantClientMixin
from dashboard.models import *

from .lang.utils import get_locale
from .forms import *
# Create your views here.

class RootContextMixin(TenantClientMixin):
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['locale'] = get_locale()
		context['config'] = SiteConfig.get_instance()
		context['useful_links'] = UsefulLink.objects.filter(deleted_at__isnull=True)[:5]
		context['navbar'] = Navbar.objects.filter(deleted_at__isnull=True, parent=None)
		return context	

class ListSearchMixin:
	search_fields = ['title__icontains', 'category__name__icontains']

	def get_queryset(self):
		queryset = super().get_queryset()
		search = self.request.GET.get('search', '').strip()
		if hasattr(self, 'search_fields') and search != '':
			filter_query = Q(pk__lt=0)
			for field in self.search_fields:
				filter_query = filter_query | Q(**{ field: search })
			queryset = queryset.filter(filter_query)
		return queryset


class HomeView(RootContextMixin, TemplateView):
	template_name = 'home/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['marquee_notices'] = Notice.objects.filter(deleted_at__isnull=True, display_in_marquee=True)[:20]
		context['home_popups'] = HomePagePopup.objects.filter(deleted_at__isnull=True, is_active=True)
		context['sliders'] = Slider.objects.filter(deleted_at__isnull=True)[:6]
		context['slider_hr'] = HR.objects.filter(show_in_slider=True, deleted_at__isnull=True, )
		context['hr'] = HR.objects.filter(suchana_adhikari=False, show_in_homepage=True, deleted_at__isnull=True).all()
		context['suchana_hr'] = HR.objects.filter(suchana_adhikari=True, deleted_at__isnull=True).first()
		context['news'] = News.objects.filter(deleted_at__isnull=True)[:3]
		context['press_releases'] = PressRelease.objects.filter(deleted_at__isnull=True)[:4]
		context['notices'] = Notice.objects.filter(deleted_at__isnull=True)[:4]
		context['albums'] = Album.objects.filter(deleted_at__isnull=True)[:3]
		context['events'] = Event.objects.filter(deleted_at__isnull=True)[:6]
		context['calendar_event'] = Event.objects.filter(deleted_at__isnull=True)

		# list category
		context['list_categories'] = ListCategory.objects.filter(deleted_at__isnull=True, show_in_suchana=True)  \
								.prefetch_related(
									Prefetch(
										'list',
										queryset=List.objects.filter(deleted_at__isnull=True),
									)
								) \
								.annotate(list_count=Count('list', filter=Q(list__deleted_at__isnull=True), ), ) \
								.exclude(list_count=0) \
								.order_by('-list_count')
		
		# bids category
		context['bid_categories'] = BidCategory.objects.filter(deleted_at__isnull=True)  \
								.prefetch_related(
									Prefetch(
										'bids',
										queryset=Bid.objects.filter(deleted_at__isnull=True),
									)
								) \
								.annotate(bid_count=Count('bids', filter=Q(bids__deleted_at__isnull=True), ), ) \
								.exclude(bid_count=0) \
								.order_by('-bid_count')[:5]

		# download category
		context['download_categories'] = DownloadCategory.objects.filter(deleted_at__isnull=True)  \
								.prefetch_related(
									Prefetch(
										'downloads',
										queryset=Download.objects.filter(deleted_at__isnull=True),
									)
								) \
								.annotate(download_count=Count('downloads', filter=Q(downloads__deleted_at__isnull=True), ), ) \
								.exclude(download_count=0) \
								.order_by('-download_count')[:5]

		# publication category
		context['publication_categories'] = PublicationCategory.objects.filter(deleted_at__isnull=True)  \
								.prefetch_related(
									Prefetch(
										'publications',
										queryset=Publication.objects.filter(deleted_at__isnull=True),
									)
								) \
								.annotate(publication_count=Count('publications', filter=Q(publications__deleted_at__isnull=True), ), ) \
								.exclude(publication_count=0) \
								.order_by('-publication_count')[:5]

		# policy category
		context['policy_categories'] = PolicyCategory.objects.filter(deleted_at__isnull=True)  \
								.prefetch_related(
									Prefetch(
										'policies',
										queryset=Policy.objects.filter(deleted_at__isnull=True),
									)
								) \
								.annotate(policy_count=Count('policies', filter=Q(policies__deleted_at__isnull=True), ), ) \
								.exclude(policy_count=0) \
								.order_by('-policy_count')[:5]

		return context


# News
class NewsListView(ListSearchMixin, RootContextMixin, ListView):
	template_name = 'home/news/list.html'
	model = News
	paginate_by = 24
	queryset = News.objects.filter(deleted_at__isnull=True)
	search_fields = ['title__icontains', 'sub_title__icontains', ]

class NewsDetailView(RootContextMixin, DetailView):
	template_name = 'home/news/detail.html'
	model = News
	queryset = News.objects.filter(deleted_at__isnull=True)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['other_news'] = News.objects.filter(deleted_at__isnull=True).exclude(pk=self.kwargs.get('pk'))[:12]
		return context	

# Notices
class NoticesListView(ListSearchMixin, RootContextMixin, ListView):
	template_name = 'home/notices/list.html'
	model = Notice
	paginate_by = 12
	queryset = Notice.objects.filter(deleted_at__isnull=True)
	search_fields = ['title__icontains']

	def get(self, *args, **kwargs):
		Notice.objects.filter(notice_date=None).update(notice_date=F('created_at'))
		return super().get(*args, **kwargs)

class NoticeDetailView(RootContextMixin, DetailView):
	template_name = 'home/notices/detail.html'
	model = Notice
	queryset = Notice.objects.filter(deleted_at__isnull=True)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['other_notices'] = Notice.objects.filter(deleted_at__isnull=True).exclude(pk=self.kwargs.get('pk'))[:4]
		return context	


# Press Release
class PressReleaseListView(ListSearchMixin, RootContextMixin, ListView):
	template_name = 'home/press-releases/list.html'
	model = PressRelease
	paginate_by = 12
	queryset = PressRelease.objects.filter(deleted_at__isnull=True)
	search_fields = ['title__icontains', ]

class PressReleaseDetailView(RootContextMixin, DetailView):
	template_name = 'home/press-releases/detail.html'
	model = PressRelease
	queryset = PressRelease.objects.filter(deleted_at__isnull=True)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['others'] = PressRelease.objects.filter(deleted_at__isnull=True).exclude(pk=self.kwargs.get('pk'))[:4]
		return context	

# Bid
class BidListView(ListSearchMixin, RootContextMixin, ListView):
	template_name = 'home/bids/list.html'
	model = Bid
	paginate_by = 12
	queryset = Bid.objects.filter(deleted_at__isnull=True)

class BidDetailView(RootContextMixin, DetailView):
	template_name = 'home/bids/detail.html'
	model = Bid
	queryset = Bid.objects.filter(deleted_at__isnull=True)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['others'] = Bid.objects.filter(deleted_at__isnull=True).exclude(pk=self.kwargs.get('pk'))[:4]
		return context	


# Download
class DownloadListView(ListSearchMixin, RootContextMixin, ListView):
	template_name = 'home/downloads/list.html'
	model = Download
	paginate_by = 12
	queryset = Download.objects.filter(deleted_at__isnull=True)

class DownloadDetailView(RootContextMixin, DetailView):
	template_name = 'home/downloads/detail.html'
	model = Download
	queryset = Download.objects.filter(deleted_at__isnull=True)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['others'] = Download.objects.filter(deleted_at__isnull=True).exclude(pk=self.kwargs.get('pk'))[:4]
		return context	


# Publication
class PublicationListView(ListSearchMixin, RootContextMixin, ListView):
	template_name = 'home/publications/list.html'
	model = Publication
	paginate_by = 12

	def get_queryset(self):
		queryset = super().get_queryset().filter(deleted_at__isnull=True)
		if 'category' in self.request.GET:
			queryset = queryset.filter(category__name=self.request.GET.get('category', ''))
		return queryset

class PublicationDetailView(RootContextMixin, DetailView):
	template_name = 'home/publications/detail.html'
	model = Publication
	queryset = Publication.objects.filter(deleted_at__isnull=True)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['others'] = Publication.objects.filter(deleted_at__isnull=True).exclude(pk=self.kwargs.get('pk'))[:4]
		return context	

# Project
class ProjectsListView(ListSearchMixin, RootContextMixin, ListView):
	template_name = 'home/projects/list.html'
	model = Project
	paginate_by = 12
	queryset = Project.objects.filter(deleted_at__isnull=True)
	search_fields = ['title__icontains']

class ProjectDetailView(RootContextMixin, DetailView):
	template_name = 'home/projects/detail.html'
	model = Project
	queryset = Project.objects.filter(deleted_at__isnull=True)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['others'] = Project.objects.filter(deleted_at__isnull=True).exclude(pk=self.kwargs.get('pk'))[:4]
		return context	

# Policy
class PolicyListView(ListSearchMixin, RootContextMixin, ListView):
	template_name = 'home/policies/list.html'
	model = Policy
	paginate_by = 12
	queryset = Policy.objects.filter(deleted_at__isnull=True)

class PolicyDetailView(RootContextMixin, DetailView):
	template_name = 'home/policies/detail.html'
	model = Policy
	queryset = Policy.objects.filter(deleted_at__isnull=True)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['others'] = Policy.objects.filter(deleted_at__isnull=True).exclude(pk=self.kwargs.get('pk'))[:4]
		return context	


# Events
class EventsListView(RootContextMixin, ListView):
	template_name = 'home/events/list.html'
	model = Event

	def get_queryset(self):
		return super().get_queryset().filter(deleted_at__isnull=True).filter( Q(end_date__isnull=True) | Q( end_date__gte=timezone.now()) )

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['other_events'] = self.get_queryset()
		return context	


class EventDetailView(RootContextMixin, DetailView):
	template_name = 'home/events/detail.html'
	model = Event
	queryset = Event.objects.filter(deleted_at__isnull=True)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['other_events'] = Event.objects.filter(deleted_at__isnull=True).filter( Q(end_date__isnull=True) | Q( end_date__gte=timezone.now()) ).exclude(pk=self.kwargs.get('pk'))
		return context	

# Albums
class AlbumsView(RootContextMixin, ListView):
	template_name = 'home/album/list.html'
	model = Album
	paginate_by = 12

	def get_queryset(self):
		return super().get_queryset().filter(deleted_at__isnull=True)

class AlbumDetailView(RootContextMixin, DetailView):
	template_name = 'home/album/detail.html'
	model = Album

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		self.object = self.get_object()
		context['photos'] = AlbumPhoto.objects.filter(album=self.object, deleted_at__isnull=True)
		return context

# HR
class HRListView(ListSearchMixin, RootContextMixin, ListView):
	template_name = 'home/hr/list.html'
	model = HR
	paginate_by = 24
	queryset = HR.objects.filter(deleted_at__isnull=True)
	search_fields = ['name__icontains']

class HRDetailView(RootContextMixin, DetailView):
	template_name = 'home/hr/detail.html'
	model = HR
	queryset = HR.objects.filter(deleted_at__isnull=True)


# Page detail view
class PageDetailView(RootContextMixin, DetailView):
	template_name = 'home/pages/detail.html'
	model = Page
	queryset = Page.objects.filter(deleted_at__isnull=True)



# Useful links list view
class UsefulLinkListView(RootContextMixin, TemplateView):
	template_name = 'home/useful-links/list.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['useful_links'] = UsefulLink.objects.filter(deleted_at__isnull=True)
		context['useful_detail'] = True
		return context	

# Message
class MessageCreateView(RootContextMixin, FormView):
    template_name = 'home/message/form.html'
    form_class = MessageForm
    model = Message
    success_url = reverse_lazy('home:message-create')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "सफलतापूर्वक सिर्जना गरियो !")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "त्यहाँ केहि समस्या देखिन्छ। कृपया तल हेर्नुहोस् !" )
        return super().form_invalid(form)


# List
class ListListView(ListSearchMixin, RootContextMixin, ListView):
	template_name = 'home/list/list.html'
	model = List
	paginate_by = 12

	def get_category(self):
		return get_object_or_404(ListCategory, name=self.kwargs.get('category'))

	def get_queryset(self):
		return super().get_queryset().filter(deleted_at__isnull=True, category__name=self.kwargs.get('category'))
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["category"] = self.get_category()
		return context
	

class ListDetailView(RootContextMixin, DetailView):
	template_name = 'home/list/detail.html'
	model = List
	queryset = List.objects.filter(deleted_at__isnull=True)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['others'] = List.objects.filter(deleted_at__isnull=True, category=self.get_object().category).exclude(pk=self.kwargs.get('pk'))[:4]
		return context	