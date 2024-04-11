from django.shortcuts import render
from django.views.generic import ListView
from .models import Phone

class list(ListView):
    # Phone 객체의 이름을 오름차순(이름순으로)으로 정렬
    queryset = Phone.objects.all().order_by('name')
    model = Phone
    template_name = 'list.html'
    context_object_name = 'phones'

def search(request):
    data = request.GET['searchtext']

    # 쿼리셋 사용 (contains)
    phones = Phone.objects.filter(name__contains = data)
    return render(request, 'search.html', {'phones':phones, 'data':data})