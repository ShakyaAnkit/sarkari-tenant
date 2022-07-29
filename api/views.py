from .serializers import NoticeSerializer
from rest_framework.generics import ListAPIView
from dashboard.models import Notice

class NoticeListApiView(ListAPIView):
    model = Notice
    queryset = Notice.objects.filter(deleted_at__isnull=True)
    serializer_class = NoticeSerializer