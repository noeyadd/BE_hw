from django.shortcuts import render
from .models import Phone

def list(request):
    # Phone 객체의 이름을 오름차순(이름순으로)으로 정렬
    phones = Phone.objects.all().order_by('name')
    return render(request, 'list.html', {'phones':phones})

def search(request):
    data = request.GET['searchtext']

    # 쿼리셋 사용 (contains)
    phones = Phone.objects.filter(name__contains = data)
    
    return render(request, 'search.html', {'phones':phones, 'data':data})