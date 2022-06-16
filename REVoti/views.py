from REVoti.models import Subjects, Grades
from django.conf.urls import url
from django.http.response import JsonResponse
from REVoti.form import RegisterFormAjaxKey, LoginFormAjaxKey, AddSubject
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def HomePage(request):
    return render(request, "HomePage/HomePage.html")

def LoginPage(request):

    if request.is_ajax() and request.method == "POST":
        form = LoginFormAjaxKey(request.POST or None)
        if not form.is_valid():
            return JsonResponse({"errors":form.errors})
        else:
            if request.POST["method"] == "submit":
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user_auth = authenticate(username = username, password = password)
                if user_auth:
                    login(request, user=user_auth)
                else:
                    return JsonResponse({"errors":{"password":"Utente o password errati"}})
            
            return JsonResponse({"errors":["None"]})
    
    return render(request, "LoginPage/LoginPage.html")

def RegisterPage(request):
    
    if request.is_ajax() and request.method == "POST":

        form = RegisterFormAjaxKey(request.POST or None)
        if not form.is_valid():
            return JsonResponse({"errors":form.errors})
        else:
            if request.POST["method"] == "submit":
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password1"]
                User.objects.create_user(username = username, password = password)
                
            return JsonResponse({"errors":["None"]})

    return render(request, "RegisterPage/RegisterPage.html")

@login_required(login_url="/login/")
def TablePage(request):
    
    context = {}
    if request.method == "GET" and request.is_ajax():

        print("ajax -> ", request.GET)

        if "subjects_request" in request.GET:

            if request.user.subjects_set.all():
                return JsonResponse({"response": True})
            else:
                return JsonResponse({"response": False})

        elif "subject_name" in request.GET:

            form = AddSubject(request.GET)

            if form.is_valid():
                sub_qr = request.user.subjects_set.filter(subject_name = request.GET.get("subject_name"))

                if sub_qr.exists():
                    return JsonResponse({"response":{"subject_name": "Materia già inserita"}})
                else:
                    Subjects.objects.create(user = request.user, subject_name = request.GET.get("subject_name"))
                    return JsonResponse({"response":"None"})
            else:
                return JsonResponse({"response":form.errors})
        
        elif "subject-options" in request.GET:
            sub_qr = request.user.subjects_set.filter(subject_name = request.GET.get("subject-options"))
            if sub_qr:
                request.session["subject_" + request.user.username] = request.GET.get("subject-options")
                #print(request.session["subject_" + request.user.username], request.user.username)
                return JsonResponse({"response":True})
            else:
                return JsonResponse({"response":False})

        elif "update-name-subject" in request.GET:
            sub_qr = request.user.subjects_set.filter(subject_name = request.GET.get("update-name-subject"))
            if not sub_qr and request.GET.get("update-name-subject"):
                var = request.user.subjects_set.filter(subject_name = request.session.pop("subject_" + request.user.username)).first()
                var.subject_name = request.GET.get("update-name-subject")
                var.save()
                return JsonResponse({"response":True})
            else:
                return JsonResponse({"response":False})

        elif "save-grade" in request.GET:
            try:
                grade = float(request.GET.get("save-grade"))
            except ValueError:
                return JsonResponse({"response":False})

            if grade >= 0 and grade <= 10:
                var_sub = request.user.subjects_set.filter(subject_name = request.session.pop("subject_" + request.user.username)).first()
                Grades.objects.create(subject = var_sub, grade = grade, if_average = True)
                return JsonResponse({"response":True})
            else:
                return JsonResponse({"response":False})

        elif "reset-grades" in request.GET:
            var_sub = request.user.subjects_set.filter(subject_name = request.session.pop("subject_" + request.user.username)).first()
            for grade in var_sub.grades_set.all():
                grade.delete()
            return JsonResponse({"response":True})

        elif "delete-subject" in request.GET:
            var_sub = request.user.subjects_set.filter(subject_name = request.session.pop("subject_" + request.user.username)).first()
            var_sub.delete()
            return JsonResponse({"response":True})

    if request.user.subjects_set.all():
        context["materie"] = {}
        maxx = 10
        for sub in request.user.subjects_set.all():
            context["materie"][sub.subject_name] = []
            for grad in sub.grades_set.all():
                context["materie"][sub.subject_name].append(grad.grade)
            if maxx <= len(sub.grades_set.all()):
                maxx = len(sub.grades_set.all())
        context["maxx"] = range(maxx)

    return render(request, "TablePage/TablePage.html", context)



def LogoutPage(request):
    logout(request)
    return redirect("HomePage")
