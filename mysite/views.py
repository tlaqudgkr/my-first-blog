# from django.http import HttpResponse
# import datetime

from blog.models import Post

from board.models import Board

from django.shortcuts import render


def home(request):
    posts = Post.objects.order_by('-created_date')[:5]
    boards = Board.objects.order_by('-created_date')[:5]
    return render(request, 'post_home.html', {'post':posts, 'board':boards})


# def home(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body><html>" % now
#     return HttpResponse(html)