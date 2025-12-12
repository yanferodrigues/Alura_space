from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    
    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()
            
            usuario = auth.authenticate(
                request,
                username= nome,
                password= senha
            )
            
            if usuario is not None:
                auth.login(request,usuario)
                return redirect('index')
                
            else:
                messages.error(request,'Usuário não existe')
                return redirect('login') 
    
    form = LoginForms()
    
    return render(request,'usuarios/login.html',{'form':form})

def cadastro(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha'].value()
             
            usuario = User.objects.create_user(
                username=nome,
                password=senha,
                email=email
            )
            usuario.save()
            messages.success(request,'Usuário criado com sucesso')
            return redirect('login')
            
    else:
        form = CadastroForms()
    
    return render(request,'usuarios/cadastro.html', {'form':form})

def logout(request):
    if not request.user.is_authenticated:
        messages.error(request,'Impossivel fazer logout sem login')
        return redirect('login')
    
    auth.logout(request)
    messages.success(request,'Logout feito com sucesso')
    return redirect('login')
