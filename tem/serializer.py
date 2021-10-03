from tem.models import Report
from rest_framework import serializers

class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = ['report_id', 'version','report_name']
