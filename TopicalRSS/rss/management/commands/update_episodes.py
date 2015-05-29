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
        allFeeds = Feed.objects.all()

        def get_episodes(feed):  
            #Open URL and get the stuff
            url = feed.url
            doc = urllib2.urlopen(url)
            rssXML = doc.read()
            doc.close()
            tree = ET.XML(rssXML)
            episodes = tree.findall('channel/item')
            episodesTitles = tree.findall('channel/item/title')
            for j in xrange(len(episodes)):
                n = episodesTitles[j]
                n = n.text
                epN = ((len(episodes)) - j)
                epXML = episodes[j]
                epXML = ET.tostring(epXML)
                newEp = models.Episode(name = n, episodeNum = epN, xml = epXML)
                newEp.save()
        
        for feed in allFeeds:  
                self.stdout.write('Entered Function')
                get_episodes(feed)
            
            
        