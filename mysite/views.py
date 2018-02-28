from blog.models import Post

from board.models import Board

from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from taggit.models import Tag
from django.views.generic.list import ListView

def home(request):
    posts = Post.objects.order_by('-created_date')
    boards = Board.objects.order_by('-created_date')
    tags=Tag.objects.all()
    return render(request, 'post_home.html', {'post': posts, 'board': boards,'tags':tags})


# class Home(TemplateView):
#     template_name = 'home.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['tags'] = Tag.objects.all()
#         return context


class UserRegister(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserRegisterDone(TemplateView):
    template_name = 'registration/register_done.html'


class TagListView(ListView):
    template_name = 'search_tags.html'

    def get_queryset(self):
        tag_list = self.kwargs['tag'].split(",")
        return Post.objects.filter(tags__name__in=tag_list)

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context['tags'] = self.kwargs['tag']
        return context
