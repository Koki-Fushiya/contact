from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .forms import OrderForm, CreateUserForm, CustomerForm
from .filters import *
from .models import *
from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def registerPage(request):
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')


                messages.success(request, 'Account was successfully created for ' + username)

                return redirect('login')

        context = {'form': form}
        return render(request, 'parts/register.html', context)

@unauthenticated_user
def loginPage(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'ユーザーネームまたはパスワードが正しくありません')

        context = {}
        return render(request, 'parts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only 
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    outOfStock = orders.filter(status='在庫切れ').count()
    isEnough = orders.filter(status='在庫数正常').count()


    context = {'orders': orders, 'customers': customers, 'outOfStock': outOfStock,
    'total_orders': total_orders, 'isEnough': isEnough}

    return render(request, 'parts/dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()
    
    total_orders = orders.count()
    outOfStock = orders.filter(status='在庫切れ').count()
    isEnough = orders.filter(status='在庫数正常').count()

    print('ORDERS:', orders)

    context = {'orders': orders, 'outOfStock': outOfStock,
    'total_orders': total_orders, 'isEnough': isEnough}
    return render(request, 'parts/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'parts/account_settings.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def parts(request):
    parts = Parts.objects.all()

    return render(request, 'parts/parts.html', {'parts':parts})

@login_required(login_url='login')
def trouble(request):
    troubles = Trouble.objects.all()


    context = {'troubles': troubles}

    return render(request, 'parts/trouble.html', context)


@login_required(login_url='login')
def troubleDetail(request):
    troubles = Trouble.objects.all()

    return render(request, 'parts/troubleDetail.html', {'troubles': troubles})

@login_required(login_url='login')
def manual(request):
    manuals = Manual.objects.all()
    return render(request, 'parts/manual.html', {'manuals': manuals})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customer': customer, 'orders': orders, 'order_count': order_count, 'myFilter': myFilter}
    return render(request, 'parts/customer.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('parts', 'status'), extra=8)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    # form = OrderForm(initial={'customer': customer})  
    if request.method == 'POST':
        # print('Printing POST', request.POST)
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}

    return render(request, 'parts/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'parts/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item': order}

    return render(request, 'parts/delete.html', context)