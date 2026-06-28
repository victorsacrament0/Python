from django.shortcuts import render
from .models import Postagem
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostListView(LoginRequiredMixin, ListView):
    model = Postagem
    template_name = 'pages/home.html'
    context_object_name = 'posts'
    ordering = ['-data_postagem']

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Postagem
    template_name ='pages/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Postagem
    fields = ['titulo','conteudo']
    template_name = 'pages/postagem_form.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Postagem
    fields = ['titulo','conteudo']
    template_name = 'pages/update_form.html'
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False
    
class PostDeleteView(DeleteView):
    model = Postagem
    template_name = 'pages/postagem_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False


def sobre(request):
    return render(request, "pages/sobre.html")