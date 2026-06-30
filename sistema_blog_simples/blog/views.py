from django.shortcuts import render,redirect
from .models import Postagem,Comentario
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ComentarioForm
from django.db.models import Q

class PostListView(LoginRequiredMixin, ListView):
    model = Postagem
    template_name = 'pages/home.html'
    context_object_name = 'posts'
    

    def get_queryset(self):
        pesquisa = self.request.GET.get('nome')
        if pesquisa:
            posts = Postagem.objects.filter(
                Q(titulo__icontains=pesquisa) | Q(conteudo__icontains=pesquisa)
            )
        else:
            posts = Postagem.objects.all()
        return posts.order_by('-data_postagem')

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Postagem
    template_name = 'pages/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        return context

    def post(self, request, *args, **kwargs):
        
        self.object = self.get_object() 
        form = ComentarioForm(request.POST)
        
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.postagem = self.object
            comentario.autor = request.user
            comentario.save()
            return redirect('blog-detail', pk=self.object.pk)
        
        # Se o formulário for inválido, recarrega a página com os erros
        context = self.get_context_data(object=self.object)
        context['form'] = form
        return self.render_to_response(context)



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