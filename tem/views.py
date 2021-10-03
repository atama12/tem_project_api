from tem.models import Report
import django_filters.rest_framework
from rest_framework import viewsets
from tem.serializer import ReportSerializer

class ReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['report_id','version']

