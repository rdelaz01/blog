from django.shortcuts import render
from django.views.generic import (
    ListView
)
from .models import post

# Create your views here.
class postListView(ListView):
    #template_name is the attribute to render the html
    template_name = "posts/list.html"
    # models attribute lets django know from which model(table) we want to retrieve data
    model = post
    #context_object_name allow us to change the 
    # variable on how we call it inside of the templates 
    context_object_name = "posts"