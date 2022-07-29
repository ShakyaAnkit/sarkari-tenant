from django.core import serializers

from ipware.ip import get_ip

from .models import AUDIT_CHOICES, AuditTrial

def store_audit(prevObj, changedObj, actionType, request):
    return
    aTrial = AuditTrial()
    aTrial.modelType = changedObj._meta.verbose_name.title()
    aTrial.objectId = changedObj.pk
    aTrial.action = actionType
    aTrial.user = request.user
    aTrial.ip = get_ip(request)
    
    if prevObj:
    	aTrial.fromObj = serializers.serialize("json", [prevObj])
    aTrial.toObj = serializers.serialize("json", [changedObj])
    aTrial.save()

def get_audit_key(name):
	for k, v in AUDIT_CHOICES.items():
		if v == name:
			return k
