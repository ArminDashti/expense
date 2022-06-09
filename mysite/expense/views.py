from django.shortcuts import render, redirect
from .forms import login_form, expense
from django.contrib.auth import authenticate
from django.contrib.auth import login as _login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def login(request):
    if request.method == 'POST':
        from_login_form = login_form(request.POST)
        username = from_login_form['get_username'].value()
        password = from_login_form['get_pass'].value()
        user = authenticate(username=username, password=password)
        if user is not None:
            _login(request, user)
            return redirect("/expense/")
        else:
            return redirect("/expense/login/")
    
    if request.method == 'GET':
        from_login_form = login_form()
        return render(request, 'expense/login.html', {'form': from_login_form})

@login_required(login_url='/expense/login/')
def index(request):
    if request.method == 'POST':
        from_expense_form = expense(request.POST)
        if from_expense_form.is_valid():
            from_expense_form.save()
            return redirect("/expense/")
 
    if request.method == 'GET':
        from_expense_form = expense()
        return render(request, 'expense/expense.html', {'form': from_expense_form})
# Create your views here.
