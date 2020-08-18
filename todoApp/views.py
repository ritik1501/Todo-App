from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from todoApp.models import Todo, Vichar
from datetime import datetime
import random

# Create your views here.

def home(request):
    user = request.user
    if (user.is_anonymous):
        return render(request, 'first.html')
    todo = Todo.objects.filter(user=user)
    thoughts = Vichar.objects.all()
    thought = random.choices(thoughts)
    context = {'todos': todo, 'thoughts':thought}
    return render(request, 'home.html', context)

def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome Back {username} !!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials!! Please try again later.")
            return redirect('home')
    return render(request,'error.html')

def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['conpassword']

        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters.")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Password and Confirm Password not match.")
            return redirect('home')   

        if not username.isalnum():
            messages.error(request, "Username should only contain letter and numbers.")
            return redirect('home')     

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.save()

        user = authenticate(username = username, password=pass1)
        if user is not None:
            login(request, user)
            messages.success(request, "You are Successfully Signed-Up !!")
            return redirect('home')

        messages.success(request, "Your Account has been Successfully Created !!!")
        return redirect('home')
    else:
        return render(request,'error.html')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged out")
    return redirect('home')

def add(request):
    if request.method=='POST':
        title = request.POST['title']
        desc = request.POST['desc']
        datetime = request.POST['datetime']
        user = request.user
        
        todo = Todo(title = title, content=desc, user=user, timestamp=datetime)
        todo.save()
        messages.success(request, "Your work has been added...")
        return redirect('home')
    return render(request,'error.html')

def delete(request, pk):
        Todo.objects.get(pk=pk).delete()
        messages.success(request, 'You work has been deleted...')
        return redirect('home')

def edit(request, pk):
        todo = Todo.objects.get(pk=pk)
        title = todo.title
        content = str(todo.content)
        dates = todo.timestamp.strftime('%Y-%m-%d')
        times = todo.timestamp.strftime('%H:%M')
        time = dates+'T'+times
        id = todo.id
        context = {'title':title, 'content':content, 'time':time, 'id':id}
        return render(request, 'edit.html', context)

def save(request, id):
    if request.method=='POST':
        todo = Todo.objects.get(id=id)
        todo.title = request.POST['eTitle']
        todo.content = request.POST['eDesc']
        todo.timestamp = request.POST['eDateTime']
        todo.save()
        messages.success(request, 'Your work is edited Successfully...')
        return redirect('home')
    return render(request,'error.html')