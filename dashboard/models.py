from django.db import models

# Create your models here.

class event_message_detail_agg_tbl(models.Model):
    id = models.AutoField(primary_key=True)
    event_country_code = models.CharField(max_length=100,null=True,blank=True)
    event_country_name = models.CharField(max_length=100,null=True,blank=True)
    event_city_name = models.CharField(max_length=20,null=True,blank=True)
    event_server_status_color_name = models.CharField(max_length=50,null=True,blank=True)
    event_server_status_severity_level = models.CharField(max_length=50,null=True,blank=True)
    total_estimated_resolution_time = models.IntegerField(null=True,blank=True)
    total_message_count = models.IntegerField(null=True,blank=True)
    # total_messages = models.IntegerField()
