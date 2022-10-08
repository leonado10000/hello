from audioop import reverse
from unicodedata import name
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms
from . import util
import random

class searchbox(forms.Form):
    box = forms.CharField(label="query")

def index(request):
    print(request.method)
    if request.method == "POST" :
        query = request.POST.get("query")
        list_of_entires = util.list_entries()
        if query in list_of_entires :
            return HttpResponseRedirect(reverse('page' , args =[query]))
        else :
            return HttpResponseRedirect(reverse("search" , args=[query]))
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request , name):
    return render(request , "encyclopedia/page.html", {
        "content" : util.get_entry(name) , "name" : name 
    })

def search(request, query):
    list_of_entries = util.list_entries()
    findings = []
    for x in list_of_entries:
        if query in x:
            findings.append(x)
    return render(request , "encyclopedia/search.html", {
            "query" : query , "list" : findings 
        })

def new_page(request):
    if request.method == "POST" :
        title = request.POST.get("heading")
        content = request.POST.get("content")
        list_of_entries = util.list_entries()
        if title not in list_of_entries:
            util.save_entry(title , content)
            return HttpResponseRedirect(reverse("page" , args=[title]))
        
    return render(request , "encyclopedia/new_page.html" )

def rand(request):
    list_of_entry = util.list_entries()
    R = random.choice(list_of_entry)
    return HttpResponseRedirect(reverse("page", args=[R]))