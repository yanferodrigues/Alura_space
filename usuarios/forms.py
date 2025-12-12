from django import forms
from django.contrib.auth.models import User
    
class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome',
        required= True,
        max_length= 30,
        widget= forms.TextInput(
        attrs={'class':'form-control',
               'placeholder':'Digite seu nome',
               'autocomplete':'new-username'}
        )
        )
    senha = forms.CharField(
        label='Senha',
        required= True,
        min_length= 5,
        max_length= 30,
        widget= forms.PasswordInput(
        attrs={'class':'form-control',
               'placeholder': 'Digite sua senha (min: 5 digitos)',
               'autocomplete':'new-password'}
        )
        )
    
class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label= 'Nome',
        max_length= 30,
        required=True,
        widget= forms.TextInput(
        attrs={'class':'form-control',
               'placeholder': 'Digite seu username',
               'autocomplete':'new-username'}
        )
        )
    email = forms.CharField(
        label= 'Email',
        max_length= 100,
        required=True,
        widget= forms.EmailInput(
        attrs={'class':'form-control',
               'placeholder': 'Digite seu email',
               'autocomplete':'new-email'}
        )
        )
    senha = forms.CharField(
        label= 'Senha',
        max_length= 30,
        required=True,
        min_length= 5,
        widget= forms.PasswordInput(
        attrs={'class':'form-control',
               'placeholder': 'Digite sua senha (min: 5 digitos)',
               'autocomplete':'new-password'}
        )
        )
    confirmacao = forms.CharField(
        label= 'Confirme sua senha',
        max_length= 30,
        required=True,
        min_length= 5,
        widget= forms.PasswordInput(
        attrs={'class':'form-control',
               'placeholder': 'Confirme sua senha'}
        )
        )
    
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')
        
        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Esse campo não aceita espaços')
            if User.objects.filter(username=nome):
                raise forms.ValidationError('Nome de usuário já cadastrado')
            
            else:
                return nome
            
    def clean_email(self):
        email_ = self.cleaned_data.get('email')
        
        email_ = email_.strip().lower()
        if User.objects.filter(email= email_).exists():
            raise forms.ValidationError('Esse email já está sendo usado')
        
        else:
            return email_
        
    def clean_confirmacao(self):
        confirmacao = self.cleaned_data.get('confirmacao')
        senha = self.cleaned_data.get('senha')
        
        if confirmacao != senha:
            raise forms.ValidationError('As senhas devem ser exatamente iguais')
        else:
            return confirmacao
        
        
        

        
        
