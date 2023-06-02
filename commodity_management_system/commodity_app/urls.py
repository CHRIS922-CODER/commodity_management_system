
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('add_product',views.add_product,name="add_product"),
    path('product_list',views.product_list,name="product_list"),
    path('product_edit/<int:id>/',views.product_edit,name="product_edit"),
    path('product_delete/<int:id>/',views.product_delete,name="product_delete"),

    path('add_category',views.add_category,name="add_category"),
    path('category_list',views.category_list,name="category_list"),
    path('category_edit/<int:id>/',views.category_edit,name="category_edit"),
    path('category_delete/<int:id>/',views.category_delete,name="category_delete"),

    path('add_staff',views.add_staff,name="add_staff"),
    path('staff_list',views.staff_list,name="staff_list"),
    path('staff_edit/<int:id>/',views.staff_edit,name="staff_edit"),
    path('staff_delete/<int:id>/',views.staff_delete,name="staff_delete"),

    path('add_department',views.add_department,name="add_department"),
    path('department_list',views.department_list,name="department_list"),
    path('department_edit/<int:id>/',views.department_edit,name="department_edit"),
    path('department_delete/<int:id>/',views.department_delete,name="department_delete"),

    path('add_issuance',views.add_issuance,name="add_issuance"),
    path('issuance_list',views.issuance_list,name="issuance_list"),
    path('issuance_edit/<int:id>/',views.issuance_edit,name="issuance_edit"),
    path('issuance_delete/<int:id>/',views.issuance_delete,name="issuance_delete"),

    path('export_to_pdf/', views.export_to_pdf, name='export_to_pdf'),
]

    