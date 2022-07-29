from django.contrib.auth.models import User,Group
from django.shortcuts import (
	render, redirect, get_object_or_404)
from django.urls import reverse_lazy, reverse
from .utils import *
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin


class TenantClientMixin:
    root_url = '/' # home page of clementine

    def dispatch(self, request, *args, **kwargs):
        if(is_root(request)):
            # raise Http404
            return redirect('client:dashboard')

        if self.requires_setup():
            return self.setup_tenant()

        return super().dispatch(request, *args, **kwargs)

    def requires_setup(self):
        return False
        return  not User.objects.filter(is_superuser=True).exists()

    def setup_tenant(self):
        print('INITAL SETUP')
        if not User.objects.filter(username='admin').exists():
            # # Creating groups
            # print('CREATING GROUPS')
            # g_list = [
            #     'ChiefHR','accounts', 'sales_and_marketings',
            #     'developers', 'customer_supports'
            # ]
            # for grp_name in g_list:
            #     Group.objects.get_or_create(name=grp_name)

            # Creating admin
            print('CREATING ADMIN')
            user = User(username='admin', is_staff=True, is_active=True, is_superuser=True)
            user.set_password('admin@123')
            user.save()

            # group = Group.objects.get(name="ChiefHR")
            # user.groups.add(group)

        return redirect('dashboard:index')    




class RootClientMixin:
    
    def dispatch(self, request, *args, **kwargs):
        if not is_root(request):
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class AuthMixin(LoginRequiredMixin):
    login_url = reverse_lazy('client:login')