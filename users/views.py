from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages
from users.forms import RegisterForms,LoginForms

# Create your views here.

def register (request):
    form = RegisterForms()

    if (request.method == 'POST'):
        form = RegisterForms(request.POST)

        if form.is_valid():
            name = form["loginName"].value()
            password = form["password"].value()
            email = form["email"].value()

            if (User.objects.filter(username=name).exists()):
                messages.error(request,'Usuário já cadastrado!')
                return redirect('cadastro')

            user = User.objects.create_user(
                username=name,
                email = email,
                password=password
            )

            user.save()
            messages.success(request,'Usuario cadastrado com sucesso')
            return redirect('login')

       
    return render(request,'users/register.html',{"form":form})

def login (request):
    form = LoginForms()

    if(request.method == 'POST'):
        form = LoginForms(request.POST)

        if form.is_valid():
            name = form["loginName"].value()
            password = form["password"].value()

            user = auth.authenticate(
                request,
                username = name,
                password = password
            )
            if user is not None:
                auth.login(request,user)
                messages.success(request,"Usuario logado com sucesso!")
                return redirect('index')
            else:
                messages.error(request,"Não foi possível realizar o login do usuário!")
                return redirect('login')
       
    return render(request,'users/login.html',{"form":form})

def logout(request):
    pass