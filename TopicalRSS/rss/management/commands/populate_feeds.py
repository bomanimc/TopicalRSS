from django.core.management.base import BaseCommand, CommandError
from django.core.management.base import NoArgsCommand
from django.db import models
from TopicalRSS.rss import models
from TopicalRSS.rss.models import Feed
import elementtree.ElementTree as ET
import urllib2

class Command(NoArgsCommand):
    help = "Updates the Database with parsed episodes"
    def handle_noargs(self, **options):
        self.stdout.write('Entered Main')
        feedsList = ['http://feeds.theallusionist.org/Allusionist', 'http://feeds.feedburner.com/AudioSmut', 'http://ohnostorytime.com/rss.xml']

        def add_feeds():  
            #Open URL and get the stuff
            for i in xrange(len(feedsList)):    
                feedUrl = feedsList[i]       
                doc = urllib2.urlopen(feedUrl)
                rssXML = doc.read()
                doc.close()
                tree = ET.XML(rssXML)
                feedTitle = (tree.findall('channel/title')[0]).text
                feedDescription = (tree.findall('channel/description')[0]).text

                newFeed = models.Feed(parentFeed = feed, url = feedUrl, title = feedTitle, description = feedDescription)
                
                #Only adds feed if URL is not already in DB
                if not Feed.objects.filter(url = feedUrl).exists():                
                    newFeed.save();
                    self.stdout.write('Added Feed ' + feedTitle)

        add_feeds()


            
            