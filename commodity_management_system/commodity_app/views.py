from django.shortcuts import render,redirect
from .models import Product,Staff,Category,Department,Issuance
from .forms import ProductForm, StaffForm,CategoryForm,IssuanceForm,DepartmentForm

from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import BytesIO
# Create your views here.

def home(request):
    issuances = Issuance.objects.all()
    context = {'issuances':issuances}
    return render(request, 'commodity_app/mytemplate.html',context=context)

# PRODUCT VIEWS
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("product_list")
            except:
                pass
    else:
        form = ProductForm()
    return render(request,'product/product_add.html',{'form':form})

def product_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        context = {'products':products}
        return render(request,"product/product_list.html",context)




def product_edit(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else :
        form = ProductForm(instance=product)
        return render(request,'product/product_edit.html',{'product':product})
    
def product_delete(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("product_list")


        


# PRODUCT CATEGORY VIEWS
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if  form.is_valid():
            try:
                form.save()
                return redirect("category_list")
            except:
                pass
    else:
        form = CategoryForm()
        return render(request,"category/category_add.html",{'form':form})
def category_list(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request,'category/category_list.html',context)

def category_edit(request,id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm(instance=category)
        return render(request,"category/category_edit.html",{'form':form})
    
def category_delete(request,id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect("category_list")

# STAFF VIEWS
def add_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("staff_list")
            except:
                  pass
    else:
        form = StaffForm()
        return render(request, "staff/staff_add.html", {'form': form})
    
def staff_list(request):
    staffs = Staff.objects.all()
    context = {'staffs':staffs}
    return render(request,'staff/staff_list.html',context)
    
def staff_edit(request,id):
    staff = Staff.objects.get(id=id)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect("staff_list")
    else:
        form = StaffForm(instance=staff)
        return render(request,'staff/staff_edit.html',{'form':form})
def staff_delete(request,id):
    staff = Staff.objects.get(id=id)
    staff.delete()
    return redirect("staff_list")

# DEPARTMENT VIEWS
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("department_list")
            except:
                pass
    else:
        form = DepartmentForm()
        return render(request,"department/department_add.html",{'form':form})

def department_list(request):
    departments = Department.objects.all()
    context = {'departments':departments}
    return render(request,"department/department_list.html",context)

def department_edit(request,id):
    department = Department.objects.get(id=id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect("department_list")
    else:
        form = DepartmentForm(instance=department)
        return render(request,"department/department_edit.html",{'form':form})
    
def department_delete(request,id):
    department = Department.objects.get(id=id)
    department.delete()
    return redirect("department_list")


# ISSUANCE VIEWS
def add_issuance(request):
    if request.method == 'POST':
        form = IssuanceForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("issuance_list")
            except:
                pass
    else:
        form = IssuanceForm()
        return render(request,'issuance/issuance_add.html',{'form':form})
def issuance_list(request):
    issuances = Issuance.objects.all()
    context = {'issuances':issuances}
    return render(request,'issuance/issuance_list.html',context)

def issuance_edit(request,id):
    issuance = Issuance.objects.get(id=id)
    if request.form == 'POST':
        form = IssuanceForm(request.POST,instance=issuance)
        if form.is_valid():
            form.save()
            return redirect("issuance_list")
    else:
        form = IssuanceForm(instance=issuance)
        return render(request,'issuance/issuance_edit.html',{'form':form})
def issuance_delete(request,id):
    issuance = Issuance.objects.get(id=id)
    issuance.delete()
    return redirect("issuance_list")



def export_to_pdf(request):
    # Fetch the issuance records from your data source
    issuances = Issuance.objects.all()  # Replace with your code to fetch the records
    
    # Create a file-like buffer to receive PDF data
    buffer = BytesIO()
    
    # Create the PDF object, using the buffer as its "file"
    p = canvas.Canvas(buffer)
    
    # Set up the PDF document
    p.setFont("Helvetica", 12)
    p.setTitle("Issuance Records")
    
    # Write the table headers
    table_headers = ["Product", "Quantity", "Date","status","staff","department"]
    row_height = 20
    y = 700  # Starting y position for the table
    for header in table_headers:
        p.drawString(50, y, header)
        y -= row_height
    
    # Write the table rows
    y -= row_height
    for issuance in issuances:
        p.drawString(50, y, str(issuance.product))
        p.drawString(150, y, issuance.quantity_issued)
        p.drawString(250, y, str(issuance.date_issued))
        p.drawString(350, y, str(issuance.status))
        p.drawString(450, y, str(issuance.staff))
        p.drawString(550, y, str(issuance.department))
        y -= row_height
    
    # Close the PDF object cleanly and finalize the document
    p.showPage()
    p.save()
    
    # File buffer position is reset to the beginning
    buffer.seek(0)
    
    # Set the response content type as PDF
    response = HttpResponse(content_type='application/pdf')
    
    # Force the PDF to be downloaded as an attachment
    response['Content-Disposition'] = 'attachment; filename="issuance_records.pdf"'
    
    # Write the PDF buffer to the response
    response.write(buffer.getvalue())
    
    return response

#VIEWS TO BE VIEWED BY THE STAFF


