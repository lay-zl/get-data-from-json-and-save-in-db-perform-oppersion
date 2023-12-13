from django.db import models

# Create your models here.

class ApiData(models.Model):
    end_yr = models.CharField(max_length=100)
    intensity = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    insight = models.TextField()
    url = models.TextField()
    region = models.CharField(max_length=100)
    start_year = models.CharField(max_length=100)
    impact = models.CharField(max_length=255)
    added = models.CharField(max_length=100)
    published = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    relevance = models.CharField(max_length=255)
    pestle = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    title = models.TextField()
    likelihood = models.CharField(max_length=100)

    def __str__(self):
        return self.title