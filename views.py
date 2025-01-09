from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseNotFound, Http404
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


def add_view(request,num1,num2):
   add_result = num1 + num2
   result =  "{num1} + {num2}= {add_result}"
   return HttpResponse(str(result))