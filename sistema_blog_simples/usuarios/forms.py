from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class CadastroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
   
    class Meta:
        model = User
        fields = ['username','email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        # 1. Verifica no Model se já existe usuário com este e-mail
        # 2. Ignora o e-mail do próprio usuário atual caso esteja editando (se aplicável)
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError("Este e-mail já está cadastrado.")
            
        return email
