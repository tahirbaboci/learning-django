from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Employee


all_employee = Employee.objects.all()


def index(request):
    return render(request, 'personel/index.html', {})

def listData(request):
    context = {
        'all_employee' : all_employee
    }

    return render(request, 'personel/list.html', context)


def detail(request, Employee_id):

    try:
        Emp = Employee.objects.get(pk=Employee_id)
    except Exception as e:
        message = 'emp was not found. Error: ' + str(e)
        return JsonResponse({'status': 'false', 'message': message}, status=404)

    return render(request, 'personel/detail.html', {'Emp' : Emp})


def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': Employee.objects.filter(email=email).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)



def add(request):
    return render(request, 'personel/add.html', {})



def add_me(request):

    nome = request.GET.get('nome', None)
    email = request.GET.get('email', None)

    a = Employee()
    a.nome = nome
    a.email = email
    a.save()
    html = '<h1> data has been saved</h1>'
    return HttpResponse(html)

