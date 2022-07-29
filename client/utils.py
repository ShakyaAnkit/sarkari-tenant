from .models import *

def get_request():
    import sys
    f = sys._getframe()
    while f:
        request = f.f_locals.get("request")
        if request:
            return request
        f = f.f_back
    return None

def hostname_from_request(request):
    """ returns hosts name from request """
    return request.get_host().split(':')[0].lower()

def root_client():
    return Client.objects.filter(schema_name='public').first()

def client_from_request(request):
    """ returns client from current request """
    hostname = hostname_from_request(request)
    return Client.objects.filter(domain_url=hostname).first()

def is_root(request):
    """ checks if current request is of root client or not """
    client = client_from_request(request)
    if not client:
        False
    return client.schema_name == 'public'

def get_client_url(request):
    client = client_from_request(request)
    if client:
        if request.is_secure():
            return 'https://'+client.domain_url
        return 'http://'+client.domain_url
    else:
        return root_client().domain_url

def get_client_domain(request):
    client = client_from_request(request)
    if client:
        return client.domain_url
    else:
        return root_client().domain_url