from django import forms
from .models import Product, Staff, Category, Issuance, Department

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class IssuanceForm(forms.ModelForm):
    class Meta:
        model = Issuance
        fields = "__all__"

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"
