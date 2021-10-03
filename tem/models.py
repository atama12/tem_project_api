from djongo import models # djongoのモデルを利用する

class Report(models.Model):
    report_id = models.IntegerField(blank=False)
    version = models.IntegerField(blank=False)
    report_name = models.TextField()
