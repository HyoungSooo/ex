
from django.shortcuts import render

from django.views.generic import View, ListView, DetailView, TemplateView

from core.models import Post, Purpose, Professor, Timeline, AboutUs, Publictions

# Create your views here.


class AboutView(ListView):
    model = AboutUs
    template_name = 'team.html'
    context_object_name = 'about_us'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs.get('category') == 'LA':
            context['professor'] = AboutUs.objects.filter(
                position='Professor').order_by('name')
            context['phd'] = AboutUs.objects.filter(
                position='PhD').order_by('name')
            context['ms'] = AboutUs.objects.filter(
                position='MS').order_by('name')
            context['undergraduate'] = AboutUs.objects.filter(
                position='Undergraduate').order_by('name')
            context['LA'] = True
        else:
            context['alumni'] = AboutUs.objects.filter(
                category='AL').order_by('name')
            context['LA'] = False
        return context


class PurposeView(ListView):
    model = Purpose
    template_name = 'purpose.html'
    context_object_name = 'purpose'

    def get_queryset(self):
        return Purpose.objects.all().first()


class PublicationsView(ListView):
    model = Publictions
    template_name = 'publications.html'
    context_object_name = 'publictions'


class PrincipleView(ListView):
    model = Professor
    template_name = 'principle.html'
    context_object_name = 'obj'

    def get_queryset(self):
        if self.kwargs['prof_name'] == 'default':
            return Professor.objects.order_by('ordering').first()
        else:
            return Professor.objects.get(name=self.kwargs['prof_name'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['professor'] = Professor.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = Post.objects.filter(id__gt=self.object.id)[:2]
        context['prev'] = Post.objects.filter(
            id__lt=self.object.id).order_by('-id')[:2]
        return context


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self):
        if self.kwargs['category'] == 'news':
            return Post.objects.filter(category='News').order_by('-created_at')
        elif self.kwargs['category'] == 'research':
            return Post.objects.filter(category='Research').order_by('-created_at')
        else:
            return Post.objects.all().order_by('-created_at')


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["News"] = Post.objects.filter(
            category='News').order_by('-created_at')[:5]
        return context
