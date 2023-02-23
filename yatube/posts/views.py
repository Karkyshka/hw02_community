from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from .models import Group, Post

User = get_user_model()


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts,
        'page_obj': page_obj
        }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author__username=username)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'author': author,
        #'username': username,
        'posts': posts,
        'page_obj': page_obj
    }
    return render(request, 'posts/profile.html', context)



def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    #author = Post.objects.all()
    #group = Group.objects.all()

    post_id = Post.objects.filter(author__posts=post_id)
    context = { 'post_id': post_id,
                'author': post.author,
                'post': post,
                #'group': group
                #'author': User

        }
    return render(request, 'posts/post_detail.html', context)
