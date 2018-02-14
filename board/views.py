from django.shortcuts import render

from board.models import Board, Category, File
from board.forms import BoardForm, FileForm

from django.shortcuts import redirect, get_object_or_404
# Create your views here.

# def post_list(request):
#     board = Board.objects.all()
#     return render(request, 'board/post_list.html', {'boards': board})

# def post_list(request, ctgry):
#     cat = Category.objects.all()
#     if ctgry == 'news':
#         posts = Board.objects.filter(category = 1)
#     elif ctgry == 'free':
#         posts = Board.objects.filter(category = 2)
#     else:
#         posts = Board.objects.all()
#
#     return render(request, 'board/post_list.html', {'posts': posts, 'cat':cat})


def post_list(request):
    cat = Category.objects.all()
    ctgry = request.GET.get('category')
    # 파라미터에 있는 값을 가져와서 해달 게시글을 검색하고
    # 없으면 모든 글을 반환한다.
    if ctgry != None:
        posts = Board.objects.filter(category__name = ctgry)
    else:
        posts = Board.objects.all()

    return render(request, 'board/post_list.html', {'posts': posts, 'cat':cat})


def post_detail(request, pk):
    cat = Category.objects.all()
    post = get_object_or_404(Board, pk=pk)
    file = post.file_set.all()
    return render(request,'board/post_detail.html', {'post': post, 'cat':cat, 'file':file})


def post_new(request):
    cat = Category.objects.all()
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()

            upfls = request.FILES.getlist('file')
            for upfl in upfls:
                file = File()
                file.file = upfl
                file.post = post
                file.save()

            return redirect('board:post_detail', pk=post.pk)
    else:
        form = BoardForm()
        file = FileForm()
    return render(request, 'board/post_edit.html', {'form': form, 'cat':cat, 'file': file})


def post_edit(request,pk):
    cat = Category.objects.all()
    post = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = BoardForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'cat':cat})