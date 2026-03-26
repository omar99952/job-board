from django.db import models

# Create your models here.

Job_Type = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)
class job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15,choices = Job_Type)
    description = models.TextField(max_length = 50)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)