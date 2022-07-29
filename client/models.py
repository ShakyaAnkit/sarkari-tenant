from django.db import models

# Create your models here.


from tenant_schemas.models import TenantMixin


class RequestedClient(models.Model):
    subdomain = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    accepted_at = models.DateTimeField(null=True, blank=True)
    rejected_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Requested Client"
        verbose_name_plural = "Requested Clients"

    def __str__(self):
         return 'Requested for '+self.organization+' by '+self.name

    def is_accepted(self):
        return self.accepted_at != None

    def is_rejected(self):
        return self.rejected_at != None

    def is_new(self):
        return self.accepted_at == None and self.rejected_at == None

    def save(self, *args, **kwargs):
        # self.subdomain = 
        return super().save(*args, **kwargs)

    def new_requests_count():
        return RequestedClient.objects.filter(accepted_at=None, rejected_at=None).count()

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

    def __str__(self):
        return self.name

