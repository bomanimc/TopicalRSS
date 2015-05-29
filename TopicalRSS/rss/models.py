from django.db import models
import elementtree.ElementTree as ET
import urllib2

# Create your models here.
class Feed(models.Model):
	url = models.CharField(max_length=250, blank=True, null=True)
	title = models.CharField(max_length=250, blank=True, null=True)
	description = models.CharField(max_length=5000, blank=True, null=True)
	#pass

class Episode(models.Model):
	parentFeed = models.ForeignKey(Feed, null=True)
	name = models.CharField(max_length=250, blank=True, null=True)
	episodeNum = models.IntegerField();
	xml = models.CharField(max_length=10000, blank=True, null=True)


