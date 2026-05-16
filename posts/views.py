from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView 
)
from .models import post, Status 
from django.contrib.auth.models import User 
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    UserPassesTestMixin
)

# Create your views here.
class postListView(ListView): # GET request that returns the list
    #template_name is the attribute to render the html
    template_name = "posts/list.html"
    # models attribute lets django know from which model(table) we want to retrieve data
    #model = post
    published_status = Status.objects.get(name="published")
    # queryset attribute allows us to select data from the DB using the model class 
    # and also allows us to customize the data filtering it 
    queryset = post.objects.filter(status=published_status).order_by("created_on").reverse()

    #context_object_name allow us to change the 
    # variable on how we call it inside of the templates 
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_status"] = "Published"
        return context 

class PostArchiveListView(ListView):
    template_name = "posts/list.html"
    archived_status = Status.objects.get(name="archived")
    queryset = post.objects.filter(status=archived_status)
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_status"] = "Archived"
        return context

class PostDraftListView(ListView):
    template_name = "posts/list.html"
    draft_status = Status.objects.get(name="draft")
    queryset = post.objects.filter(status=draft_status)
    context_object_name = "posts"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_status"] = "Draft"
        return context



class PostDetailView(LoginRequiredMixin, DetailView): # GET Request -> Single element (object)
    template_name = "posts/detail.html"
    model = post 
    context_object_name = "single_post"

class PostCreateView(LoginRequiredMixin ,CreateView): # POST Request -> empty form in the HTML
    template_name = "posts/new.html"
    model = post 
    # fields attribute is a list that allows us to enable/disable the inputs to render in the html
    fields = ["title", "subtitle", "body", "status"]

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"
    model = post
    fields = ["title", "subtitle", "body", "status"]

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_authenticated:
            if self.request.user == post.author:
                return True
            else:
                return False
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"
    model = post

    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_authenticated:
            if self.request.user == post.author:
                return True
            else:
                return False
        else:
            return False