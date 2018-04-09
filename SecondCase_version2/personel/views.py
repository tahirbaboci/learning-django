from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Employee


all_employee = Employee.objects.all()


def index(request):
    html = ''
    urllist = '/personel/list/'
    urladd = '/personel/add/'
    list = 'click if you want to list Employees'
    add = 'click if you want to add a new employee'
    html += '<a href="' + urllist + '"> ' + list + '</a><br>' + '<a href="' + urladd + '"> ' + add + '</a><br>'

    return HttpResponse(html)


def listData(request):
    context = {
        'all_employee' : all_employee
    }

    html = ''
    for employee in all_employee:
        url = '/personel/list/' + str(employee.id) + '/'
        html += '<a href="' + url + '"> ' + employee.nome + '</a><br>'

    return HttpResponse(html)


def detail(request, Employee_id):
    try:
        emp = Employee.objects.filter(id = Employee_id).exists()
    except Employee.DoesNotExist:
        raise Http404("Employee does not exists")

    '''
    html = ''
    for employee in all_employee:
        if employee.id == Employee_id:
            html += "details for employee with id : " + str(employee.id)  + "<br><br>" + "Nome : " + employee.nome + " <br>" + "Email : " + employee.email + "<br><br><br>"
        else:
            html = 'Empty!'

    '''
    if emp:
        return render(request, "personel/detail.html", {'Emp' : emp})
    return render(request, "personel/detail.html", '')




def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': Employee.objects.filter(email=email).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)

def add(request):
    html = ''

    html += '''
         <html>
            <head>
                <script type="text/javascript" src="static/jquery-3.3.1.js"></script>
                <script type="text/javascript" src="static/jquery-3.3.1.min.js"></script>
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
            </head>
            <body>
               <p> Nome : </p>
               <input type="input" id="nome"/>

               <p> Email : </p>
               <input type="input" id="email"/>
               </br>
               <input type="submit" value = 'test button' id="submit"/></input><br><br>
               <p id = "message"></p>

               <script type="text/javascript" src="static/js/ajax_JQuery.js"></script>

               <script type="text/javascript">

                     $(document).ready(function(){
                             $('#submit').click(function(event){
                                alert("hello");
                                event.preventDefault();
                                var nome = $("#nome").data();
                                var email = $("#email").data();
                                var data = {
                                   "nome" : nome,
                                   "email" : email,
                                };
                                $.ajax({
                                  type: "POST",
                                  url: "/add_me/",
                                  data: data,
                                  success: function(){ $('#message').html("<h2>Contact Form Submitted!</h2>")},
                                  dataType: "json",
                                  contentType : "application/json"

                                });
                                document.location = '/personel/add_me/';
                                return false;
                             });

                            $('#email').change(function () {
                              var validateEmail = $(this).val();

                              $.ajax({
                                url: '/add/validate_email/',
                                data: {
                                  'email': validateEmail,
                                },
                                dataType: 'json',
                                success: function (data) {
                                  if (data.is_taken) {
                                    alert("A user with this username already exists.");
                                  }
                                }
                              });

                            });
                     });

               </script>
            </body>

        </html>
    '''
    return HttpResponse(html)



def add_me(request):

    nome = request.GET.get('nome', None)
    email = request.GET.get('email', None)

    a = Employee()
    a.nome = nome
    a.email = email
    a.save()
    html = '<h1> data has been saved</h1>'
    return HttpResponse(html)

