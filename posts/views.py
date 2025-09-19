from django.urls import reverse_lazy
from django.views.generic import ( 
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.contrib.auth.models import User


# Crud -> Create, Read, Update and Delete
# The generic classes are ListView, CreateView, UpdateView, DeleteView and DetailView
#                          GET       POST         POST        POST           GET

# Create your views here.

"""
PostListView is going to retrieve all of the object from the Post table in the DB
"""
class PostListView(ListView):
    # template_name attribute is going to render a specific html file
    template_name = "posts/list.html"
    #model is going to  be from which table we want to retrieve the data
    model = Post

    #queryset is used to define the model used for the view
    #queryset = Post.objects.all()

    # context is a python dictionary that holds the data for the generic views
    #and this context travels to the htmls
    #by default the context name of ListView and DetailView is "Object" or "object_list"

    #context_object_name would allow us to modify the name and how to call it in the htmls
    context_object_name = "post_list"

"""
PostDetailView is going to retrieve a single object from the Post table in the DB
"""
class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"

"""
PostCreateView is going to allow us to create a new post and add it to the DB
"""
class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ['title', 'subtitle', 'body']

    def form_valid(self, form):
        print(form)
        print(User.objects.all())
        form.instance.author = User.objects.filter(is_superuser=True).first()
        return super().form_valid(form)

"""
PostUpdateView is going to allow us to update an existing record in the DB
"""

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy('posts')

    """
    PostUpdateView is going to allow us to update an existing record in the DB
    """

class PostUpdateView(UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ['title', 'subtitle', 'body']