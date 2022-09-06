from unicodedata import name
from django.urls import path, include
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("team/<str:category>", AboutView.as_view(), name="team"),
    path("teamDetail/<int:pk>", MemberDetailView.as_view(), name="teamDetail"),
    path("contect/", TemplateView.as_view(template_name="contect.html"), name="contect"),
    path("Photos&Video/<str:category>",
         PostListView.as_view(template_name="Photo.html"), name="Photo"),
    path("prof_list/", TemplateView.as_view(template_name="prof_list.html"),
         name="prof_list"),
    path("News/<str:category>", PostListView.as_view(), name="News"),
    path("principle/<str:prof_name>", PrincipleView.as_view(), name="principle"),
    path("post_list/<str:category>", PostListView.as_view(), name="post_list"),
    # path("publications/", PublicationsView.as_view(),
    #      name="publications"),
    path("researcharena/", ResearchArenaView.as_view(), name='RA'),
    path("research/<int:pk>/", ResearchArenaDetailView.as_view(),
         name="research"),
    path("project", ProjectView.as_view(), name="project"),
    path("post_detail/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("journallist/<str:category>/",
         PublictionsView.as_view(), name='journal'),
]
