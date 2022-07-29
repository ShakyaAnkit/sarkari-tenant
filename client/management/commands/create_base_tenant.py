import getpass

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.core.validators import validate_email

from client.models import Client

base_domain = 'sarkari.prixa.net'

class Command(BaseCommand):
    help = 'Creates initial base company'

    def email_input(self):
        try:
            validate_email(self.email)
        except:
            print('Please Enter a valid Email Address')
            self.email = input('Email Address : ')
            self.email_input()

    def validate_username(self):
        if User.objects.filter(username=self.username).exists():
            print('Username already exists')
            self.username = input('New Username Again : ')
            self.validate_username()

    def match_password(self):
        if self.password != self.confirm_password:
            print('Password do not match ')
            self.confirm_password = getpass.getpass('Password Retype : ')
            self.match_password()


    def create_user(self, *args, **options):
        self.username = input('Username: ')
        self.validate_username()
        self.email = input('Email Address: ')
        self.email_input()
        self.password = getpass.getpass('Password : ')
        self.confirm_password = getpass.getpass('Confirm Password : ')
        self.match_password()

        try:
            user = User.objects.create_user(username=self.username, email=self.email, password=self.password, 
                is_active=True, is_staff=True, is_superuser=True)
            user.save()
            print('User with superuser access is created')
        except Exception as e:
            print(type(e), e)
            print('Unable to create superuser')

    def handle(self, *args, **options):
        
        if not Client.objects.all().exists():
            domain_url = str(input('Enter base domain (eg. {}): '.format(base_domain)))
            Client.objects.get_or_create(
                domain_url=domain_url,
                schema_name='public',
                name='public'
            )
            self.create_user()
            print('Base Tenant created successfully')
        else:
            print('Base Tenant already exists')