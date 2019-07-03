# Import necessary classes
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import Category, Product, Client, Order
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from myapp.forms import OrderForm,InterestForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('base.html')
    else:
        form = NewUserForm()
    return render(request, 'myapp/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'myapp/myorders.html', {'myorder': myorder})
            else:
                return HttpResponse('Your account is disabled.')
        else:
                return HttpResponse('Invalid login details.')
    else:
                return render(request, 'registration/login.html')
@login_required
def user_logout(request):
    logout(request)
    return render(request, 'myapp/index.html')

class indexView(View):
    def get(self, request):
        cat_list = Category.objects.all().order_by('id')[:10]
        client = Client.objects.get(username="allenwang")
        return render(request, 'myapp/index.html', {'cat_list': cat_list,'client':client})

    '''
    for cat in cat_list:
        para = '<p>'+ str(cat.id) + ': ' + str(cat) + '</p>'
        response.write(para)
    return response
    '''# This one is subsituted by the above codes, I don't need this one.

def about(request):
    #response = HttpResponse()
    #heading1 = '<p>' + 'This is an Online Store APP.'+'</p>'
    #response.write(heading1)
    return render(request, 'myapp/about.html')

def products(request):
    prodlist = Product.objects.all().order_by('id')[:10]
    return render(request, 'myapp/products.html', {'prodlist': prodlist})

def place_order(request):
    msg = ''
    prodlist = Product.objects.all()
    if request.method == 'POST':
       form = OrderForm(request.POST)
       if form.is_valid():
          order = form.save(commit=False)
          if order.num_units <= order.product.stock:
              order.save()
              msg = 'Your order has been placed successfully.'
          else:
              msg = 'We do not have sufficient stock to fill your order.'
          return render(request, 'myapp/order_response.html', {'msg': msg})

    else:
       form = OrderForm()
    return render(request, 'myapp/placeorder.html', {'form':form, 'msg':msg,'prodlist':prodlist})


def productdetail(request, prod_id):
    item = Product.objects.get(id=prod_id)
    if request.method == 'GET':
        form = InterestForm(request.GET)
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid() and item.interested:
            item.interested=item.interested+1
            form.save()
            return render(request, 'myapp/index.html')
    return render(request, 'myapp/productdetail.html', {'item': item})


def detail(request, cat_no):
    obj=get_object_or_404(Category, id=cat_no)
    #warehouse = Category.objects.get(id=cat_no)
    #response = HttpResponse()
    #response.write(warehouse)
    category = Category.objects.get(id=cat_no)
    list = category.products.all()
    return render(request, 'myapp/detail.html', {'category': category, 'list': list})
    #return response


def myorder(request):
    #if request.method == 'GET':
    myorder = Order.objects.all().order_by('id')[:100]
    if request.user.is_authenticated:
        return render(request, 'myapp/myorders.html', {'myorder': myorder})
    else:
        return HttpResponseRedirect('/login/')
