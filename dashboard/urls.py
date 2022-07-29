from django.conf.urls import url
from . import views

app_name = 'dashboard'

urlpatterns = [
	
	# Login & Logout
	url(r'^login$', views.LoginView.as_view(), name='login'),
	url(r'^logout$', views.LogoutView.as_view(), name='logout'),

	# Dashboard index
	url(r'^$', views.DashboardIndex.as_view(), name='index'),

	# Notices
	url(r'^notices/$', views.NoticeListView.as_view(), name='notices-list'),
	url(r'^notices/create$', views.NoticeCreateView.as_view(),name='notices-create'),
	url(r'^notices/(?P<pk>\d+)/update$', views.NoticeUpdateView.as_view(),name='notices-update'),
	url(r'^notices/(?P<pk>\d+)/delete$', views.NoticeDeleteView.as_view(),name='notices-delete'),
	url(r'notices/detail/(?P<pk>[0-9]+)/$', views.NoticeDetailView.as_view(), name='notices-detail'),

	# Press release
	url(r'^press-releases/$', views.PressReleaseListView.as_view(), name='press-releases-list'),
	url(r'^press-releases/create$', views.PressReleaseCreateView.as_view(),name='press-releases-create'),
	url(r'^press-releases/(?P<pk>\d+)/update$', views.PressReleaseUpdateView.as_view(),name='press-releases-update'),
	url(r'^press-releases/(?P<pk>\d+)/delete$', views.PressReleaseDeleteView.as_view(),name='press-releases-delete'),
	url(r'press-releases/detail/(?P<pk>[0-9]+)/$', views.PressReleaseDetailView.as_view(), name='press-releases-detail'),

	# Bid
	url(r'^bids/$', views.BidListView.as_view(), name='bids-list'),
	url(r'^bids/create$', views.BidCreateView.as_view(),name='bids-create'),
	url(r'^bids/(?P<pk>\d+)/update$', views.BidUpdateView.as_view(),name='bids-update'),
	url(r'^bids/(?P<pk>\d+)/delete$', views.BidDeleteView.as_view(),name='bids-delete'),
	url(r'bids/detail/(?P<pk>[0-9]+)/$', views.BidDetailView.as_view(), name='bids-detail'),

	# Publications
	url(r'^publications/$', views.PublicationListView.as_view(), name='publications-list'),
	url(r'^publications/create$', views.PublicationCreateView.as_view(),name='publications-create'),
	url(r'^publications/(?P<pk>\d+)/update$', views.PublicationUpdateView.as_view(),name='publications-update'),
	url(r'^publications/(?P<pk>\d+)/delete$', views.PublicationDeleteView.as_view(),name='publications-delete'),
	url(r'publications/detail/(?P<pk>[0-9]+)/$', views.PublicationDetailView.as_view(), name='publications-detail'),

	# Policies
	url(r'^policies/$', views.PolicyListView.as_view(), name='policies-list'),
	url(r'^policies/create$', views.PolicyCreateView.as_view(),name='policies-create'),
	url(r'^policies/(?P<pk>\d+)/update$', views.PolicyUpdateView.as_view(),name='policies-update'),
	url(r'^policies/(?P<pk>\d+)/delete$', views.PolicyDeleteView.as_view(),name='policies-delete'),
	url(r'policies/detail/(?P<pk>[0-9]+)/$', views.PolicyDetailView.as_view(), name='policies-detail'),

	# Downloads
	url(r'^downloads/$', views.DownloadListView.as_view(), name='downloads-list'),
	url(r'^downloads/create$', views.DownloadCreateView.as_view(),name='downloads-create'),
	url(r'^downloads/(?P<pk>\d+)/update$', views.DownloadUpdateView.as_view(),name='downloads-update'),
	url(r'^downloads/(?P<pk>\d+)/delete$', views.DownloadDeleteView.as_view(),name='downloads-delete'),
	url(r'downloads/detail/(?P<pk>[0-9]+)/$', views.DownloadDetailView.as_view(), name='downloads-detail'),

	# Project
	url(r'^projects/$', views.ProjectListView.as_view(), name='projects-list'),
	url(r'^projects/create$', views.ProjectCreateView.as_view(),name='projects-create'),
	url(r'^projects/(?P<pk>\d+)/update$', views.ProjectUpdateView.as_view(),name='projects-update'),
	url(r'^projects/(?P<pk>\d+)/delete$', views.ProjectDeleteView.as_view(),name='projects-delete'),
	url(r'projects/detail/(?P<pk>[0-9]+)/$', views.ProjectDetailView.as_view(), name='projects-detail'),

	# Event
	url(r'^events/$', views.EventListView.as_view(), name='events-list'),
	url(r'^events/create$', views.EventCreateView.as_view(),name='events-create'),
	url(r'^events/(?P<pk>\d+)/update$', views.EventUpdateView.as_view(),name='events-update'),
	url(r'^events/(?P<pk>\d+)/delete$', views.EventDeleteView.as_view(),name='events-delete'),
	url(r'events/detail/(?P<pk>[0-9]+)/$', views.EventDetailView.as_view(), name='events-detail'),
	
	# News
	url(r'^news/$', views.NewsListView.as_view(), name='news-list'),
	url(r'^news/create$', views.NewsCreateView.as_view(),name='news-create'),
	url(r'^news/(?P<pk>\d+)/update$', views.NewsUpdateView.as_view(),name='news-update'),
	url(r'^news/(?P<pk>\d+)/delete$', views.NewsDeleteView.as_view(),name='news-delete'),
	url(r'news/detail/(?P<pk>[0-9]+)/$', views.NewsDetailView.as_view(), name='news-detail'),

	# HR
	url(r'^hr/$', views.HRListView.as_view(), name='hr-list'),
	url(r'^hr/sort$', views.HRSortView.as_view(),name='hr-sort'),
	url(r'^hr/create$', views.HRCreateView.as_view(),name='hr-create'),
	url(r'^hr/(?P<pk>\d+)/update$', views.HRUpdateView.as_view(),name='hr-update'),
	url(r'^hr/(?P<pk>\d+)/delete$', views.HRDeleteView.as_view(),name='hr-delete'),
	url(r'hr/detail/(?P<pk>[0-9]+)/$', views.HRDetailView.as_view(), name='hr-detail'),

	# Slider
	url(r'^sliders/$', views.SliderListView.as_view(), name='sliders-list'),
	url(r'^sliders/create$', views.SliderCreateView.as_view(),name='sliders-create'),
	url(r'^sliders/(?P<pk>\d+)/update$', views.SliderUpdateView.as_view(),name='sliders-update'),
	url(r'^sliders/(?P<pk>\d+)/delete$', views.SliderDeleteView.as_view(),name='sliders-delete'),
	url(r'sliders/detail/(?P<pk>[0-9]+)/$', views.SliderDetailView.as_view(), name='sliders-detail'),

	# Album
	url(r'^albums/$', views.AlbumListView.as_view(), name='albums-list'),
	url(r'^albums/create$', views.AlbumCreateView.as_view(),name='albums-create'),
	url(r'^albums/(?P<pk>\d+)/update$', views.AlbumUpdateView.as_view(),name='albums-update'),
	url(r'^albums/(?P<pk>\d+)/delete$', views.AlbumDeleteView.as_view(),name='albums-delete'),

	# AlbumPhoto
	url(r'^albums/(?P<album_pk>\d+)/photos/$', views.AlbumPhotoListView.as_view(), name='albums-photos-list'),
	url(r'^albums/(?P<album_pk>\d+)/photos/create$', views.AlbumPhotoCreateView.as_view(),name='albums-photos-create'),
	url(r'^albums/(?P<album_pk>\d+)/photos/(?P<pk>\d+)/update$', views.AlbumPhotoUpdateView.as_view(),name='albums-photos-update'),
	url(r'^albums/(?P<album_pk>\d+)/photos/(?P<pk>\d+)/delete$', views.AlbumPhotoDeleteView.as_view(),name='albums-photos-delete'),

	# Department
	url(r'^departments/$', views.DepartmentListView.as_view(), name='departments-list'),
	url(r'^departments/create$', views.DepartmentCreateView.as_view(),name='departments-create'),
	url(r'^departments/(?P<pk>\d+)/update$', views.DepartmentUpdateView.as_view(),name='departments-update'),
	url(r'^departments/(?P<pk>\d+)/delete$', views.DepartmentDeleteView.as_view(),name='departments-delete'),
	url(r'departments/detail/(?P<pk>[0-9]+)/$', views.DepartmentDetailView.as_view(), name='departments-detail'),

	# UsefulLink
	url(r'^useful-links/$', views.UsefulLinkListView.as_view(), name='useful-links-list'),
	url(r'^useful-links/create$', views.UsefulLinkCreateView.as_view(),name='useful-links-create'),
	url(r'^useful-links/(?P<pk>\d+)/update$', views.UsefulLinkUpdateView.as_view(),name='useful-links-update'),
	url(r'^useful-links/(?P<pk>\d+)/delete$', views.UsefulLinkDeleteView.as_view(),name='useful-links-delete'),
	url(r'useful-links/detail/(?P<pk>[0-9]+)/$', views.UsefulLinkDetailView.as_view(), name='useful-links-detail'),

	# Message
	url(r'^messages/$', views.MessageListView.as_view(), name='messages-list'),
	url(r'^messages/create$', views.MessageCreateView.as_view(),name='messages-create'),
	url(r'^messages/(?P<pk>\d+)/update$', views.MessageUpdateView.as_view(),name='messages-update'),
	url(r'^messages/(?P<pk>\d+)/delete$', views.MessageDeleteView.as_view(),name='messages-delete'),
	url(r'messages/detail/(?P<pk>[0-9]+)/$', views.MessageDetailView.as_view(), name='messages-detail'),

	# Page
	url(r'^pages/$', views.PageListView.as_view(), name='pages-list'),
	url(r'^pages/create$', views.PageCreateView.as_view(),name='pages-create'),
	url(r'^pages/(?P<pk>\d+)/update$', views.PageUpdateView.as_view(),name='pages-update'),
	url(r'^pages/(?P<pk>\d+)/delete$', views.PageDeleteView.as_view(),name='pages-delete'),
	url(r'pages/detail/(?P<pk>[0-9]+)/$', views.PageDetailView.as_view(), name='pages-detail'),

	# Navbar
	url(r'^navbar/$', views.NavbarListView.as_view(), name='navbar-list'),
	url(r'^navbar/sort$', views.NavbarSortView.as_view(), name='navbar-sort'),
	url(r'^navbar/create$', views.NavbarCreateView.as_view(),name='navbar-create'),
	url(r'^navbar/(?P<pk>\d+)/update$', views.NavbarUpdateView.as_view(),name='navbar-update'),
	url(r'^navbar/(?P<pk>\d+)/delete$', views.NavbarDeleteView.as_view(),name='navbar-delete'),
	url(r'navbar/detail/(?P<pk>[0-9]+)/$', views.NavbarDetailView.as_view(), name='navbar-detail'),


	# HomePagePopup
	url(r'^home-page-popup/$', views.HomePagePopupListView.as_view(), name='home-page-popup-list'),
	url(r'^home-page-popup/create$', views.HomePagePopupCreateView.as_view(),name='home-page-popup-create'),
	url(r'^home-page-popup/(?P<pk>\d+)/update$', views.HomePagePopupUpdateView.as_view(),name='home-page-popup-update'),
	url(r'^home-page-popup/(?P<pk>\d+)/delete$', views.HomePagePopupDeleteView.as_view(),name='home-page-popup-delete'),
	url(r'^home-page-popup/(?P<pk>[0-9]+)/detail/$', views.HomePagePopupDetailView.as_view(), name='home-page-popup-detail'),
	url(r'^home-page-popup/(?P<pk>\d+)/status-change$', views.HomePagePopupStatusChangeView.as_view(),name='home-page-popup-status-change'),

	# SiteConfig
	url(r'^site-config/$', views.SiteConfigListView.as_view(), name='site-config-list'),
	url(r'^site-config/update$', views.SiteConfigUpdateView.as_view(),name='site-config-update'),


	# List
	url(r'^list/$', views.ListListView.as_view(), name='list-list'),
	url(r'^list/create$', views.ListCreateView.as_view(),name='list-create'),
	url(r'^list/(?P<pk>\d+)/update$', views.ListUpdateView.as_view(),name='list-update'),
	url(r'^list/(?P<pk>\d+)/delete$', views.ListDeleteView.as_view(),name='list-delete'),
	url(r'list/detail/(?P<pk>[0-9]+)/$', views.ListDetailView.as_view(), name='list-detail'),

	url(r'^users/$', views.UserListView.as_view(), name='users-list'),
	url(r'^users/create$', views.UserCreateView.as_view(),name='users-create'),
	url(r'^users/(?P<pk>\d+)/update$', views.UserUpdateView.as_view(),name='users-update'),
	url(r'^users/(?P<pk>\d+)/status$', views.UserStatusView.as_view(),name='users-status'),
	url(r'^users/(?P<pk>\d+)/password-reset$', views.UserPasswordResetView.as_view(), name='users-password-reset'),

]