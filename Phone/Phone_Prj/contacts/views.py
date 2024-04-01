from django.shortcuts import render
from .models import Phone

def list(request):
    # Phone 객체의 이름을 오름차순(이름순으로)으로 정렬
    phones = Phone.objects.all().order_by('name')
    return render(request, 'list.html', {'phones':phones})

def search(request):
    data = request.GET['searchtext']

    # 쿼리셋 사용
    phones = Phone.objects.filter(name__contains = data)

    if (phones.exists() == False):
        data = "이름없음"
    
    return render(request, 'search.html', {'phones':phones, 'data':data})