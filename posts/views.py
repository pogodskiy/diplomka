from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm
from user.models import UserModel

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts.html')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def detail_posts(request, product_id):
    post = get_object_or_404(Post, id=product_id)
    if request.method == 'POST':
        context = {'post': post}
        return render(request, 'post_detail.html', context)
    else:
        redirect('posts.html')

@login_required
def post_update(request, product_id):
    post = get_object_or_404(Post, id=product_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(
                'posts:list')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_update.html', {'form': form, 'post': post})

@login_required
def post_delete(request, product_id):
    post = get_object_or_404(Post, id=product_id)
    if request.method == 'POST':
        post.delete()
        return redirect(
            'posts:list')  # Здесь 'posts:list' - это имя URL-пути, на который нужно перенаправить после успешного удаления поста
    return render(request, 'post_delete.html', {'post': post})


def posts_user(request, name):
    user = UserModel.objects.get(username=name)
    posts = Post.objects.filter(author=user)
    context = {'user': user, 'posts': posts}
    return render(request, 'post_user.html', context)