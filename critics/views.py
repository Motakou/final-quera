from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import User, Critic
from .forms import CriticForm, RegisterForm, LoginForm

def createc(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CriticForm(request.POST)
            if form.is_valid():
                user = User.objects.get(id=request.user.id)
                c = Critic.objects.create(
                    title = form.cleaned_data['title'],
                    text = form.cleaned_data['text'],
                    movie_title = form.cleaned_data['movie_title'],
                    creator_first_name = form.cleaned_data['creator_first_name'],
                    creator_last_name = form.cleaned_data['creator_last_name'],
                    creator = user
                )
                return redirect('read', id=c.id)
            else:
                return render (request, 'create.html', {'form': form})
        else:
            return render (request, 'create.html', {'form': CriticForm()})
    else:
        return redirect('login')

def readc(request, id):
    c = Critic.objects.get(id=id)
    return render(request, 'read.html', {'object':c})

def listc(request):
    cqs = Critic.objects.all()
    return render (request, 'list.html', {'objs' :cqs})

def deletec(request, id):
    c = Critic.objects.get(id=id)
    if request.user.id == c.creator.id:
        c.delete()
        return redirect('create')

def usersignup(request):
    if request.user.is_authenticated:
        return redirect ('logout')
    else:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(
                    username = form.cleaned_data['username'],
                    email = form.cleaned_data['email'],
                    password = form.cleaned_data['password'],
                )
                login(request, user)
                return redirect('login')
            else:
                return render(request, 'create.html', {'form':form})
        else:
            return render (request, 'create.html', {'form':RegisterForm()})

def userlogin(request):
    if request.user.is_authenticated:
        return redirect('logout')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(
                request,
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
                )
                if user:
                    login(request, user)
                    return redirect('list')
                else:
                    return render(request, 'create.html', {'form': form})
            else:
               return render(request, 'create.html', {'form': form}) 
        else:
            return render (request, 'create.html', {'form':LoginForm})

def userlogout(request):
    logout(request)
    return redirect ('login')