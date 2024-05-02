from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone

def list(request):
    # Phone 객체의 이름을 오름차순(이름순으로)으로 정렬
    phones = Phone.objects.all().order_by('name')
    return render(request, 'contacts/list.html', {'phones':phones})
    

def search(request):
    data = request.GET['searchtext']

    # 쿼리셋 사용 (contains)
    phones = Phone.objects.filter(name__contains = data)
    return render(request, 'contacts/search.html', {'phones':phones, 'data':data})

# CRUD - Create
def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone_num = request.POST.get('phone_num')
        email = request.POST.get('email')

        phones = Phone.objects.create(
            name = name,
            phone_num = phone_num,
            email = email,
        )
        return redirect('list')
    return render(request, 'contacts/create.html')

# CRUD - Read
def detail(request, id):
    phone = get_object_or_404(Phone, id = id)    
    return render(request, 'contacts/detail.html', {'phone' : phone})

# CRUD - Update
def update(request, id):
    phone = get_object_or_404(Phone, id = id)
    if request.method == "POST":
        phone.name = request.POST.get('name')
        phone.phone_num = request.POST.get('phone_num')
        phone.email = request.POST.get('email')
        phone.save()
        return redirect('detail', id)
    return render(request, 'contacts/update.html', {'phone' : phone})

# CRUD - Delete
def delete(request, id):
    phone = get_object_or_404(Phone, id = id)
    if request.method == "POST":
        phone.delete()
        return redirect('list')
    return render(request, 'contacts/delete.html', {'phone' : phone})