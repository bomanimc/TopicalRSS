from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.core import serializers
import elementtree.ElementTree as ET
from models import Episode

class HomeView(TemplateView):
	template_name = 'index.html'

#A function from Stack Overflow for printing in a formatted way.
#Maybe be better to switch to lxml pretty print option
def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def feed(request,slug):
	#Entered Function and captured slug
	print "Worked!"
	print slug

	template_name = 'xml.html'
	eps = Episode.objects.all().filter(episodeNum = 2)
	epsXML = []

	for ep in eps:
		print ep.xml
		tree = ET.XML(ep.xml)
		epsXML.append(ET.tostring(tree))


	print epsXML

	context = {"epsXML": epsXML}
	return render_to_response(template_name, context, content_type="application/rss+xml")