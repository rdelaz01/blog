from django.urls import path
from .views import (
    postListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostArchiveListView,
    PostDraftListView

)

urlpatterns = [
    path("", postListView.as_view(), name="post_list"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("new/", PostCreateView.as_view(), name="post_new"),
    path("edit/<int:pk>/", PostUpdateView.as_view(), name="post_edit"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="post_delete"),
    path("archive/", PostArchiveListView.as_view(), name="post_archive_list"),
    path("drafts/", PostDraftListView.as_view(), name="post_draft_list"),
]