from datetime import date

from django.shortcuts import render
from django.http import Http404

from django.views.generic import View, ListView, DetailView, TemplateView

from core.models import Post, Purpose, Professor, Timeline, AboutUs, Publications, ResearchArena, Project, PictureCa, ProfTimeline, IndexResearch, MembersTimeline

# Create your views here.


class AboutView(ListView):
    model = AboutUs
    template_name = 'team.html'
    context_object_name = 'about_us'

    def get_queryset(self):
        return AboutUs.objects.filter(position=self.kwargs['category'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs['category']
        return context

# class PublicationsView(ListView):
#     model = Publictions
#     template_name = 'publications.html'
#     context_object_name = 'publictions'


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
        prof = super().get_queryset()
        context['professor'] = Professor.objects.all()
        context['RItimeline'] = ProfTimeline.objects.filter(
            member=prof[0].id, category='Interest').order_by('-start_date')
        context['EDtimeline'] = ProfTimeline.objects.filter(
            member=prof[0].id, category='Education').order_by('-start_date')
        context['EXtimeline'] = ProfTimeline.objects.filter(
            member=prof[0].id, category='Experience').order_by('-start_date')
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
    template_name = 'News.html'
    context_object_name = 'posts'
    paginate_by = 20

    def get_queryset(self):
        if self.kwargs['category'] == 'news':
            return Post.objects.filter(category='News').order_by('-created_at')
        elif self.kwargs['category'] == 'research':
            return Post.objects.filter(category='Research').order_by('-created_at')
        elif self.kwargs['category'] == 'Os':
            return Post.objects.filter(category='Outstanding').order_by('-created_at')
        else:
            return Post.objects.all().order_by('-created_at')


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["News"] = Post.objects.filter(
            category='News').order_by('-created_at')[:3]
        context["pic"] = PictureCa.objects.all()[1:]
        context["firstpic"] = PictureCa.objects.all().first()
        context['Re'] = IndexResearch.objects.all()[:4]
        return context


class ResearchArenaView(ListView):
    template_name = 'researcharena.html'
    model = ResearchArena
    context_object_name = 'obj'


class ResearchArenaDetailView(DetailView):
    template_name = 'research.html'
    model = ResearchArena
    context_object_name = 'purpose'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = ResearchArena.objects.all()

        return context


class MemberDetailView(DetailView):
    model = AboutUs
    template_name = 'memberdetail.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mem = super().get_queryset()
        category = AboutUs.objects.get(id=self.kwargs['pk']).position
        context['others'] = AboutUs.objects.filter(position=category)
        context['RItimeline'] = MembersTimeline.objects.filter(
            member=mem[0].id, category='Interest').order_by('-start_date')
        context['EDtimeline'] = MembersTimeline.objects.filter(
            member=mem[0].id, category='Education').order_by('-start_date')
        context['EXtimeline'] = MembersTimeline.objects.filter(
            member=mem[0].id, category='Experience').order_by('-start_date')
        return context


class PublictionsView(ListView):
    template_name = 'journal.html'
    model = Publications
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs['category'] == 'default':
            data = Publications.objects.all()
        else:
            if self.kwargs['category'] in ('International Papers', 'International Conference', 'Domestic Papers', 'Domestic Conference', 'Patents'):
                data = Publications.objects.filter(
                    category=self.kwargs['category'])
            else:
                raise Http404
        sub = set()

        context['0010data'] = Publications.objects.filter(
            date__gte=date(2000, 1, 1), date__lte=date(2010, 12, 31))
        context['1120data'] = Publications.objects.filter(
            date__gte=date(2011, 1, 1), date__lte=date(2020, 12, 31)
        )

        l = []
        preprocessing = data.filter(date__gte=date(2021, 1, 1))
        for i in preprocessing:
            new = False
            if i.date.year not in sub:
                new = True
                sub.add(i.date.year)
                p = i.date.year
                context[str(p)] = Publications.objects.filter(
                    date__gte=date(p, 1, 1), date__lte=date(p, 12, 31))

            if context[str(p)] and new:
                l.append((str(p), context[str(p)]))

        context['data'] = l
        return context


class ProjectView(ListView):
    model = Project
    template_name = 'project.html'
    context_object_name = 'obj'
