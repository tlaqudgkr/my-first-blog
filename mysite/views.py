from blog.models import Post

from board.models import Board

from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

def home(request):
    posts = Post.objects.order_by('-created_date')[:5]
    boards = Board.objects.order_by('-created_date')[:5]
    return render(request, 'post_home.html', {'post':posts, 'board':boards})

class Home(TemplateView):
    template_name = 'home.html'


class UserRegister(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserRegisterDone(TemplateView):
    template_name = 'registration/register_done.html'