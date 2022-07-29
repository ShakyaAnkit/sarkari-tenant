from django.urls import path

from . import views
from api import views as api_view

urlpatterns = [

	path('', views.HomeView.as_view(), name='home'),

	#Album	  
	path('albums', views.AlbumsView.as_view(), name='album-list'),
	path('album/<int:pk>', views.AlbumDetailView.as_view(), name='album-detail'),

	# news
	path('news', views.NewsListView.as_view(), name='news-list'),
	path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),

	# notices
	path('notices', views.NoticesListView.as_view(), name='notices-list'),
	path('notice/<int:pk>', views.NoticeDetailView.as_view(), name='notice-detail'),

	# press-releases
	path('press-releases', views.PressReleaseListView.as_view(), name='press-releases-list'),
	path('press-releases/<int:pk>', views.PressReleaseDetailView.as_view(), name='press-releases-detail'),

	# bids
	path('bids', views.BidListView.as_view(), name='bids-list'),
	path('bids/<int:pk>', views.BidDetailView.as_view(), name='bids-detail'),

	# downloads
	path('downloads', views.DownloadListView.as_view(), name='downloads-list'),
	path('downloads/<int:pk>', views.DownloadDetailView.as_view(), name='downloads-detail'),

	# publications
	path('publications', views.PublicationListView.as_view(), name='publications-list'),
	path('publications/<int:pk>', views.PublicationDetailView.as_view(), name='publications-detail'),

	# policies
	path('policies', views.PolicyListView.as_view(), name='policies-list'),
	path('policies/<int:pk>', views.PolicyDetailView.as_view(), name='policies-detail'),

	# events
	path('events', views.EventsListView.as_view(), name='events-list'),
	path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),

	# projects
	path('projects', views.ProjectsListView.as_view(), name='projects-list'),
	path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),

	# hr
	path('members', views.HRListView.as_view(), name='hr-list'),
	path('members/<int:pk>', views.HRDetailView.as_view(), name='hr-detail'),

	# pages
	path('pages/<str:slug>', views.PageDetailView.as_view(), name='pages-detail'),

	# useful links
	path('useful-links', views.UsefulLinkListView.as_view(), name='useful-links-list'),

	# message
	path('message', views.MessageCreateView.as_view(), name='message-create'),


	# list
	# path('list', views.ListListView.as_view(), name='list-list'),
	path('list/<int:pk>', views.ListDetailView.as_view(), name='list-detail'),
	path('list/<str:category>', views.ListListView.as_view(), name='list-category'),

	# api 
	path('api/notices', api_view.NoticeListApiView.as_view(), name='notices-api'),
]