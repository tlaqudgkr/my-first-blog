from django.shortcuts import render

from board.models import Board
from board.forms import BoardForm

from django.shortcuts import redirect, get_object_or_404
# Create your views here.

def post_list(request):
    board = Board.objects.all()
    return render(request, 'board/post_list.html', {'boards': board})

def post_detail(request, pk):
    post = get_object_or_404(Board, pk=pk)
    return render(request,'board/post_detail.html', {'post':post})


def post_new(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('board:post_detail', pk=post.pk)
    else:
        form = BoardForm()
    return render(request, 'board/post_edit.html', {'form': form})