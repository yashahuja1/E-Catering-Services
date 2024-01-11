from django import forms
from .models import *


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["First_Name","Last_Name","City","Phone","Address"]
        # widgets = {'user': forms.HiddenInput(attrs={'id': 'user_label'})}


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'


class orderItemForm(forms.ModelForm):
    class Meta:
        model = orderItem
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ["Restaurant_Name","Info","Min_order","Location","Restaurant_Logo"]


class CustomerSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        def save(self, commit=True):
            user = super().save(commit=False)
            user.is_manufactures = True
            if commit:
                user.save()
            return user


class ResSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        def save(self, commit=True):
            user = super().save(commit=False)
            user.is_manufactures = True
            if commit:
                user.save()
            return user
