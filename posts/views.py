from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView 
)
from .models import post
from django.contrib.auth.models import User 
from django.urls import reverse_lazy 

# Create your views here.
class postListView(ListView): # GET request that returns the list
    #template_name is the attribute to render the html
    template_name = "posts/list.html"
    # models attribute lets django know from which model(table) we want to retrieve data
    model = post
    #context_object_name allow us to change the 
    # variable on how we call it inside of the templates 
    context_object_name = "posts"

class PostDetailView(DetailView): # GET Request -> Single element (object)
    template_name = "posts/detail.html"
    model = post 
    context_object_name = "single_post"

class PostCreateView(CreateView): # POST Request -> empty form in the HTML
    template_name = "posts/new.html"
    model = post 
    # fields attribute is a list that allows us to enable/disable the inputs to render in the html
    fields = ["title", "subtitle", "body"]

    def form_valid(self, form):
        form.instance.author = User.objects.last()
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    template_name = "posts/edit.html"
    model = post
    fields = ["title", "subtitle", "body"]

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = post

    success_url = reverse_lazy("post_list")