from django.shortcuts import render,redirect
import time
from .models import types,items,save_order
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_protect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .forms import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
#creating methods........
#create home page......


def save_details(request):

    if request.method=='POST':
        item_id=request.POST['id1']
        types1=request.POST['types1']
        item_name=request.POST['item_name1']
        rate1=int(request.POST['rate'])
        quantity=int(request.POST['quantity'])

        total=rate1*quantity
        #image=request.POST['image']

        name1=request.POST['name']

        contact1 = request.POST['contact_number1']

        contact2 = request.POST['contact_number2']
        state1=request.POST['state']
        district1=request.POST['district']
        if contact2=='':
            contact2=contact1

        address = request.POST['address']

        pincode = int(request.POST['pincode'])
        y=time.strftime('%y')
        m=time.strftime('%m')

        d=time.strftime('%d')

        date=('20'+y+'-'+m+'-'+d)
        print(pincode)
        if (len(contact1)==10 and quantity>=1 and len(str(pincode))==6):
            form=save_order.objects.create(state1=state1,district=district1,item_id=item_id,rate=rate1 ,pincode=pincode ,date=date,contact1=contact1,contact2=contact2,item_name=item_name,types1=types1,quantity=quantity,total=total,name1=name1,address=address)
            form.save()

            messages.info(request,'your order saved you will get call soon')
            return render(request,'saved_order.html',{'total':total,'item_id':item_id,'quantity':quantity,'rate1':rate1,'name':name1,'id':form.id})

        else:
            messages.info(request,'not saved details check once again')
            return redirect('order/'+item_id)
def delete(request,id):
    form=save_order.objects.get(id=id)
    form.delete()
    messages.info(request,'your order was cancelled visit again')
    return redirect('/show')
def categeries(request):
    cat=types.objects.all()
    return render(request,'/show_orders.html',{'cat':cat})
def home(request):

    return render(request,'home.html')
def register1(request):
    form=register()
    if request.method=='POST':
        form=register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/register')
    return render(request,'register.html',{'form':form})
def show(request):
    form=items.objects.all()
    cat = types.objects.all()
    if request.method=='POST':
        product_name=request.POST['item_name']
        try:
            if items.objects.filter(item_name=product_name).exists():
                form=items.objects.filter(item_name=product_name)
                return render(request, 'show_products.html', {"form": form, 'cat': cat})

            elif types.objects.filter(types1=product_name).exists():
                form=types.objects.get(types1=product_name)
                return redirect('/show_categery/'+str(form.id))
        except:
            messages.info(request,'Product Not Avilable')
            return render('/show')

    return render(request,'show_products.html',{"form":form,'cat':cat})
@login_required(login_url='/login')
def product_add(request):
    form=product_add_form()
    if request.method=='POST':
        form=product_add_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/product_add')
    return render(request,'product_add.html',{'form':form})

def show_categery(request,id):
    cat=types.objects.all()
    product_type=types.objects.get(id=id)

    form=items.objects.filter(product_type=product_type)

    return render(request,'show_products.html',{"form":form,'cat':cat})
def order(request,id):
    form = items.objects.get(id=id)

    return render(request,'order.html',{'form':form})
@csrf_protect
@ensure_csrf_cookie
def login(request):
    if request.method=='POST':
        user_name=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=user_name,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request, 'successfully loged in')

            return redirect('/show_orders')
        else:
            messages.info(request, 'Enter correct username and password')
            return redirect('/login')

    return render(request,'login_page.html')
@login_required(login_url='/login')
def logout_page(request):
    logout(request)
    return redirect('/login')
@login_required(login_url='/login')
def show_orders(request):
    y = time.strftime('%y')
    m = time.strftime('%m')

    d = time.strftime('%d')

    date1 = ('20' + y + '-' + m + '-' + str(d))
    print(date1)
    form = save_order.objects.filter(date=date1)
    total_amount = []
    for i in form:
        total_amount.append(int(i.total))

    total_amount = sum(total_amount)
    number_of_orders = len(form)

    if len(form)==0:
        form=''
    return render(request, 'show_orders.html', {'form': form, 'number_of_orders': number_of_orders, 'total_amount': total_amount})

@login_required(login_url='/login')
def deliver(request,id):
    form1=save_order.objects.get(id=id)
    form1.completed=False
    form1.save()
    return redirect('/show_orders')

@login_required(login_url='/login')
def pending(request,id):
    form1=save_order.objects.get(id=id)
    form1.completed=True
    form1.save()
    return redirect('/show_orders')
@login_required(login_url='/login')
def count_all(request):
    delivery=save_order.objects.filter(completed=True)
    pending=save_order.objects.filter(completed=False)
    number_of_delivery_orders=len(delivery)
    number_of_pending_orders=len(pending)


    return render(request,'total_products.html',{'delivery':delivery,'pending':pending,'number_of_delivery_orders':number_of_delivery_orders,'number_of_pending_orders':number_of_pending_orders})
