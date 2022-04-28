from django.http.response import JsonResponse
from django.shortcuts import render
from .models import User
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    all_student = User.objects.all()
    return render(request, 'Crud/index.html', {'students':all_student})
# @csrf_exempt
def save_data(request):
    if request.method == 'POST':
        sid = request.POST.get('stuid')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            if(sid == ''):
                user = User(name=name, email=email, password= password)
            else:
                user = User(id=sid, name=name, email=email, password= password)

            user.save()
            stud = User.objects.values()
            # print('student', stud)
            student_data = list(stud)
            # print('student data', student_data)
            return JsonResponse({'status':'Save', 'student_data':student_data})
        except Exception as e:
            print(e)
            return JsonResponse({'status':'0'})

# Delete Data 
def delete_data(request):
    if request.method == "POST":
        try:
            id = request.POST.get('sid')
            print(id)
            pi = User.objects.get(pk=id)
            pi.delete()
            return JsonResponse({'status':1})
        except Exception as e:
            return JsonResponse({"status":0})
    else:
        return JsonResponse({"status":0})

# Edit Data 
def edit_data(request):
    if request.method == "POST":
        try:
            id = request.POST.get('sid')
            print(id)
            student = User.objects.get(pk=id)
            student_data = {'id':student.id, 'name':student.name, 'email':student.email, 'password':student.password}
            return JsonResponse(student_data)
        except Exception as e:
            print(e)
    
