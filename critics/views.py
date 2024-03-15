from django.shortcuts import render,redirect
from .models import User,Critic
from .forms import CriticForm,RegisterForm,LoginForm
# Create your views here.
def createc(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = CriticForm(request.POST)
            if form.is_valid():
                user = User.objects.get(id = request.user.id)
                c = Critic.objects.create(
                    title = form.cleaned_data['title'],
                    text = form.cleaned_data['text'],
                    creator = user
                )
                return redirect(f'critics:read:{c.id}')
            
            else:
                return render(request,'create.html',{'form':form})
        else:
            return render(request,'create.html',{'form':CriticForm()})
    else:
        return redirect('critics:login')

def readc(request):
    pass

def listc(requests):
    pass

def deletec(request):
    pass

def usersingup(request):
    pass

def userlogin(request):
    pass

def userlogout(request):
    pass
