from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from collections import Counter
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


# Create your views here.
def Index(request):
    customers = Customer.objects.all()
    return render(request, 'index.html', {'customers': customers})


def Items(request):
    item = Item.objects.all()
    return render(request, 'item.html', {'item': item})


def Menus(request):
    menus = Menu.objects.all()
    return render(request, 'menus.html', {'menus': menus})


def OrderItem(request):
    orderitem = orderItem.objects.all()
    return render(request, 'order_item.html', {'orderitem': orderitem})


def Orders(request):
    order = Order.objects.all()
    return render(request, 'order.html', {'order': order})


def Restaurants(request):
    restaurant = Restaurant.objects.all()
    return render(request, 'restaurant.html', {'restaurant': restaurant})


def Feedbacks(request):
    feedback = Feedback.objects.all()
    return render(request, 'feedback.html', {'feedback': feedback})


def Register(request):
    return render(request, 'register.html')


def Login(request):
    return render(request, 'login.html')


def InsertDataCust(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'insert_data_cust.html', {'form': form})


def InsertDataItem(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'insert_data_item.html', {'form': form})


def InsertDataRes(request):
    form = RestaurantForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'insert_data_res.html', {'form': form})


def InsertDataMenu(request):
    form = MenuForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'insert_data_menu.html', {'form': form})


def Update_Data(request, id):
    customer = Customer.objects.get(id=id)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'insert_data_cust.html', {'customer': customer, 'form': form})


def Update_DataItem(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'insert_data_item.html', {'item': item, 'form': form})


def Update_DataRes(request, id):
    res = Restaurant.objects.get(id=id)
    form = RestaurantForm(request.POST or None, instance=res)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'insert_data_res.html', {'res': res, 'form': form})


def Update_DataMenu(request, id):
    mennu = Menu.objects.get(id=id)
    form = MenuForm(request.POST or None, instance=mennu)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'insert_data_menu.html', {'mennu': mennu, 'form': form})


def Delete_data(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()

    return redirect('index')


def Delete_data1(request, id):
    menuss = Menu.objects.get(id=id)
    menuss.delete()

    return redirect('index')


def Delete_data2(request, id):
    orders = Order.objects.get(id=id)
    orders.delete()
    return redirect('index')


def Delete_data3(request, id):
    orders = Order.objects.get(id=id)
    orders.delete()
    return redirect('index')


def Delete_data4(request, id):
    itemss = Item.objects.get(id=id)
    itemss.delete()
    return redirect('index')


def Delete_data5(request, id):
    restaurantss = Restaurant.objects.get(id=id)
    restaurantss.delete()
    return redirect('index')


def Delete_dataFeed(request, id):
    feedbackss = Feedback.objects.get(id=id)
    feedbackss.delete()
    return redirect('index')


# @login_required(login_url='custlogin')
def Index1(request):
    return render(request, 'index1.html')


# def Foodzone(request):
#     restaurant = Restaurant.objects.all()
#     return render(request, 'foodzone.html', {'restaurant': restaurant})

def Foodzone(request):
    r_object = Restaurant.objects.all()
    query = request.GET.get('q')
    if query:
        r_object = Restaurant.objects.filter(Q(Restaurant_Name__icontains=query)).distinct()
        return render(request, 'foodzone.html', {'r_object': r_object})
    return render(request, 'foodzone.html', {'r_object': r_object})


def About(request):
    return render(request, 'about.html')


def Service(request):
    return render(request, 'service.html')


def Gallery(request):
    return render(request, 'gallery.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        contact = Contact.objects.create(name=name, email=email, phone=phone, content=content)
        contact.save()
    return render(request, "contact.html")


def Feedback1(request):
    return render(request, 'feedback1.html')


def forsignup(request):
    return render(request, 'forsignup.html')


def customerRegister(request):
    form = CustomerSignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.is_customer = True
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("createcustomer")
    context = {
        'form': form
    }
    return render(request, 'signup1.html', context)


def customerLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("custprofile")
            else:
                return render(request, 'custlogin.html', {'error_message': 'Your account disable'})
        else:
            return render(request, 'custlogin.html', {'error_message': 'Invalid Login'})
    return render(request, 'custlogin.html')


def restaurantsRegister(request):
    form = ResSignupForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.is_restaurant = True
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("createrestaurant")
    context = {
        'form': form
    }

    return render(request, 'signup2.html', context)


def restLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('restprofile')
            else:
                return render(request, 'restlogin.html', {'error_message': 'Your account disable'})
        else:
            return render(request, 'restlogin.html', {'error_message': 'Invalid Login'})
    return render(request, 'restlogin.html')


def customerProfile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    return render(request, 'custprofile.html', {'user': user})


def CreateCustomer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect("custlogin")
    context = {
        'form': form,
        'title': "Complete Your profile"
    }
    return render(request, 'profile_form.html', context)


def updateCustomer(request, id):
    form = CustomerForm(request.POST or None, instance=request.user.customer)
    if form.is_valid():
        form.save()
        return redirect('custprofile')
    context = {
        'form': form,
        'title': "Update Your profile"
    }
    return render(request, 'profile_form.html', context)


def restaurantsProfile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    return render(request, 'restprofile.html', {'user': user})


# @login_required(login_url='restlogin')
class CreateRestaurant(CreateView):
    model = Restaurant
    template_name = 'resprofile_form.html'
    fields = '__all__'
    success_url = reverse_lazy('restlogin')

    def get_initial(self):
        return {'user': self.request.user}


@login_required(login_url='restlogin')
def updateRestaurant(request, id):
    form = RestaurantForm(request.POST or None, instance=request.user.restaurant)
    if form.is_valid():
        form.save()
        return redirect('restprofile')
    context = {
        'form': form,
        'title': "Update Your Restaurant profile"
    }
    return render(request, 'resprofile_form.html', context)


def Login1(request):
    return render(request, 'login1.html')


def rMenu(request, pk=None):
    menu = Menu.objects.filter(Restaurant_Names=pk)
    rest = Restaurant.objects.filter(id=pk)
    print(rest)
    items = []
    for i in menu:
        item = Item.objects.filter(First_Name=i.Item_Name)
        for content in item:
            temp = []
            temp.append(content.First_Name)
            temp.append(content.Category)
            temp.append(i.Price)
            temp.append(i.id)
            temp.append(rest[0].status)
            temp.append(i.Quantity)
            items.append(temp)
    context = {
        'items': items,
        'Restaurant_Names': pk,
        'rname': rest[0].Restaurant_Name,
        'rmin': rest[0].Min_order,
        'rinfo': rest[0].Info,
        'rlocation': rest[0].Location,
    }
    return render(request, 'rmenu.html', context)


# @login_required(login_url='/restlogin/')
@login_required(login_url='restlogin')
def menuManipulation(request):
    if not request.user.is_authenticated:
        return redirect("restlogin")

    rest = Restaurant.objects.filter(id=request.user.restaurant.id)
    rest = rest[0]
    if request.POST:
        type = request.POST['submit']
        if type == "Modify":
            menuid = int(request.POST['menuid'])
            memu = Menu.objects.filter(id=menuid). \
                update(Price=int(request.POST['Price']), Quantity=int(request.POST['Quantity']))
        elif type == "Add":
            itemid = int(request.POST['item'])
            item = Item.objects.filter(id=itemid)
            item = item[0]
            menu = Menu()
            menu.Item_Name = item
            menu.Restaurant_Names = rest
            menu.Price = int(request.POST['Price'])
            menu.Quantity = int(request.POST['Quantity'])
            menu.save()
        else:
            menuid = int(request.POST['menuid'])
            menu = Menu.objects.filter(id=menuid)
            menu[0].delete()

    menuitems = Menu.objects.filter(Restaurant_Names=rest)
    menu = []
    for x in menuitems:
        cmenu = []
        cmenu.append(x.Item_Name)
        cmenu.append(x.Price)
        cmenu.append(x.Quantity)
        cmenu.append(x.id)
        menu.append(cmenu)

    menuitems = Item.objects.all()
    items = []
    for y in menuitems:
        citem = []
        citem.append(y.id)
        citem.append(y.First_Name)
        items.append(citem)

    context = {
        "menu": menu,
        "items": items,
        "username": request.user.username,
    }
    return render(request, 'menu_modify.html', context)


@login_required(login_url='custlogin')
def checkOut(request):
    if request.method == "POST":
        address = request.POST['address']
        ordid = request.POST['oid']
        tp = request.POST['tp']
        order = Order.objects.filter(id=ordid).first()
        if order:
            order.Delivery_Address = address
            order.Total_amount = tp
            order.status = Order.ORDER_STATE_PLACED
            order.save()
        return redirect('payment')
    else:
        cart = request.COOKIES['cart'].split(",")
        cart = dict(Counter(cart))
        items = []
        totalprice = 0
        uid = User.objects.filter(username=request.user)
        oid = Order()
        oid.OrderedBy = uid[0]
        for x, y in cart.items():
            item = []
            it = Menu.objects.filter(id=int(x))
            if len(it):
                oiid = orderItem()
                oiid.Item_Name = it[0]
                oiid.Quantity = int(y)
                oid.Restaurant_Names = it[0].Restaurant_Names
                oid.save()
                oiid.Order_id = oid
                oiid.save()
                totalprice += int(y) * it[0].Price
                item.append(it[0].Item_Name.First_Name)
                it[0].Quantity = it[0].Quantity - y
                it[0].save()
                item.append(y)
                item.append(it[0].Price * int(y))
            items.append(item)
        print("-------- oid ==-----",oid)
        oid.Total_amount = totalprice
        oid.save()
        context = {
            "items": items,
            "totalprice": totalprice,
            "oid": oid.id
        }
        return render(request, 'checkout.html', context)


from django.views.generic.base import TemplateView


class PaymentView(TemplateView):
    template_name = 'payment.html'

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def orderPlaced(request):
    return render(request, 'orderplaced.html', {})


def orderList(request):
    if request.POST:
        total_price = 0
        oid = request.POST['orderid']
        select = request.POST['orderstatus']
        select = int(select)
        order = Order.objects.filter(id=oid).first()
        if len(order):
            x = Order.ORDER_STATE_PLACED
            if select == 1:
                x = Order.ORDER_STATE_PLACED
            elif select == 2:
                x = Order.ORDER_STATE_ACKNOWLEDGED
            elif select == 3:
                x = Order.ORDER_STATE_COMPLETED
            elif select == 4:
                x = Order.ORDER_STATE_DISPATCHED
            elif select == 5:
                x = Order.ORDER_STATE_CANCELLED
            else:
                x = Order.ORDER_STATE_WAITING
            order[0].status = x
            order.save()
    orders = Order.objects.filter(Restaurant_Names=request.user.restaurant).order_by('-Timestamp')
    corders = []

    for order in orders:
        user = User.objects.filter(username=order.OrderedBy)
        user = user[0]
        corder = []
        if user.is_restaurant:
            corder.append(user.restaurant.Restaurant_Name)
            corder.append(user.restaurant.Info)
        else:
            corder.append(user.customer.First_Name)
            corder.append(user.customer.Phone)
        items_list = orderItem.objects.filter(Order_id=order)

        items = []
        total_price = 0
        for item in items_list:
            citem = []
            citem.append(item.Item_Name)
            citem.append(item.Quantity)
            menu = Menu.objects.filter(id=item.Item_Name.id)
            citem.append(menu[0].Price * item.Quantity)
            total_price += menu[0].Price * item.Quantity
            menu = 0
            items.append(citem)

        corder.append(items)
        corder.append(total_price)
        corder.append(order.id)

        x = order.status
        if x == Order.ORDER_STATE_WAITING:
            x = 0
        elif x == Order.ORDER_STATE_PLACED:
            x = 1
        elif x == Order.ORDER_STATE_ACKNOWLEDGED:
            x = 2
        elif x == Order.ORDER_STATE_COMPLETED:
            x = 3
        elif x == Order.ORDER_STATE_DISPATCHED:
            x = 4
        elif x == Order.ORDER_STATE_CANCELLED:
            x = 5
        else:
            continue

        corder.append(x)
        corder.append(order.Delivery_Address)
        corders.append(corder)

    context = {
        'orders': corders
    }

    return render(request, "order_list.html", context)


def Logout(request):
    if request.user.is_restaurant:
        logout(request)
        return redirect("restlogin")
    else:
        logout(request)
        return redirect("custlogin")


def custorder(request):
    order = Order.objects.filter(OrderedBy=request.user)
    return render(request, "custorder.html", {'order': order})
