from django.urls import path, include
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("team/<str:category>", AboutView.as_view(), name="team"),
    path("contect/", TemplateView.as_view(template_name="contect.html"), name="contect"),
    path("principle/<str:prof_name>", PrincipleView.as_view(), name="principle"),
    path("post_list/<str:category>", PostListView.as_view(), name="post_list"),
    path("publications/", PublicationsView.as_view(),
         name="publications"),
    path("research/", TemplateView.as_view(template_name="research.html"),
         name="research"),
    path("purpose/", PurposeView.as_view(), name="purpose"),
    path("post_detail/<int:pk>", PostDetailView.as_view(), name="post_detail"),
]
