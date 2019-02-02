from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.mail import send_mail
from django.views.generic.edit import FormView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from .forms import PostCreateForm
from django import forms

# Creating Post
def CreatePost(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST, request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user       

            form.save()
            return redirect('blog-home')
    else:
        form = PostCreateForm()
    return render(request, 'blog/post_form.html', {'form': form})


#  Category Posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):

        get_category = self.kwargs['category']
        context = Post.objects.filter(Q(category=get_category) | Q(category='all')).order_by('-date_posted')
        return context


# All Posts
class AllPostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10




# Files All Posts
def FilesListView(request):
    posts = Post.objects.all()
    users = User.objects.all()
    context = {'users': users, 'posts': posts}

    return render(request, 'blog/files.html', context)


<<<<<<< HEAD
=======
# User Files Posts
def UserFilesListView(request, username):
    posts = Post.objects.filter(author=username)
    users = User.objects.all()
    context = {'users': users, 'posts': posts}

    return render(request, 'blog/files.html', context)

>>>>>>> 1fb910eb7d74e7f3bc2e5e0b3acb92903188a3a6
#  Posts of users
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


#  Post Detail
class PostDetailView(DetailView):
    model = Post



#  Updating View
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def files(request):
    return render(request, 'blog/files.html', {'title': 'Files'})
