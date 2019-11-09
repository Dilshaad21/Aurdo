from products.models import Restaurant
from django import forms
from products.models import Audio_Bill

class resForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = "__all__"

class Bill_View(forms.ModelForm):

    class Meta:
        model=Audio_Bill
        fields='__all__'
