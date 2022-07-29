from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

from .views import *


app_name = 'client'

urlpatterns = [
		url(r'^$',DashboardView.as_view(),name='dashboard'),

		# url(r'^client/signup/$',SignUp.as_view(),name='signup'),
		url(r'^login/$', LoginPage.as_view(), name='login'),
		url(r'^logout/$', LogoutView.as_view(), name='logout'),
		
		url(r'^clients/$', ClientListView.as_view(), name='clients-list'),
		url(r'^clients/create$',ClientCreateView.as_view(),name='clients-create'),
		url(r'^clients/(?P<pk>\d+)/update$',ClientUpdateView.as_view(),name='clients-update'),
		url(r'^clients/(?P<pk>\d+)/user-create$',ClientUserCreateView.as_view(),name='clients-user-create'),
		url(r'^clients/(?P<pk>\d+)/delete$',ClientDeleteView.as_view(),name='clients-delete'),
		
		url(r'^clients/accept/(?P<pk>\d+)/$',AcceptClientView.as_view(), name= 'acceptclient'),
		url(r'^clients/reject/(?P<pk>\d+)$',RejectClientView.as_view(), name='rejectclient'),
		
		url(r'^requested-client/create$',RequestedClientCreateView.as_view(),name='requestedclientcreate'),
		url(r'^requested-client/list$',RequestedClientListView.as_view(),name='requestedclientlist'),
		
    ]