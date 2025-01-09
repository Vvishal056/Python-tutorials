from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseNotFound, Http404,HttpResponseRedirect
# Create your views here.
articles = {
   'sports':'sports page',
   'finance':'finance page',
   'polities':'politics page'
}

def news_view(request,topic):
   try:
      result = articles[topic]
      return HttpResponse(articles[topic])
   except:
      raise Http404("404 error")

def num_page_view(request,num_page):
      topic_list = list(articles.keys())
      topic = topic_list[num_page]

      return HttpResponseRedirect(topic)