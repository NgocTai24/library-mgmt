from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import RegisterForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

@user_passes_test(lambda u: u.is_staff)
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

def register(request):
    if request.method == 'POST':
       form = RegisterForm(request.POST)
       if form.is_valid():
           user = form.save(commit=False)
           user.set_password(form.cleaned_data['password'])
           user.save()
           return redirect('user_list')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_list')
        else:
            error = "Sai tài khoản hoặc mật khẩu"
            return render(request, 'users/login.html', {'error': error})
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'users/user_detail.html', {'user': user})

@api_view(['GET'])
def api_user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)