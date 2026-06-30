from .models import Postagem  # Altere para o nome correto do seu modelo

def ultimos_posts(request):
   
    return {
        'ultimas_postagens_globais': Postagem.objects.all().order_by('-data_postagem')[:3]
    }