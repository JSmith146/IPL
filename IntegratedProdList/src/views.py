from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from .choices import *
from .filters import ProjectFilter

# Create your views here.
def index(request):
    return render(request, 'base.html')

def show_login(request):
    return render(request, 'login_page.html')

def show_registration(request):
    return render(request, 'registration_page.html')

def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/registration')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id

        messages.success(request, "You have successfully registered!")
        return redirect('/all_projects')

def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id

    messages.success(request, "You have successfully logged in!")
    return redirect('/all_projects')

def logout(request):
    request.session.flush()
    return redirect('/')

def create_project(request):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/all_projects')
    else:
        form = ProjectForm()
        context = {
            'form':form
        }
        return render(request, 'new_project.html', context)

def edit_project(request,id):
    if 'user_id' not in request.session:
        return redirect('/')
    
    project_exists = Project.objects.filter(id=id)
    if len(project_exists) >0:
        project= Project.objects.get(id=id)
        if project.project_creator.id != request.session['user_id']:
            return redirect("/all_projects")
        if request.method == "POST":
            form = ProjectForm(request.POST, instance=project)
            if form.is_valid():
                form.save()
                return redirect(f'/project/{id}')
        else:
            form = ProjectForm(instance=project)
            context = {
                'project':project,
                'form':form
            }
            return render(request, 'edit_project.html', context)
    return redirect('/all_projects')

def show_project(request,id):
    if 'user_id' not in request.session:
        return redirect('/')
    project_exists = Project.objects.filter(id=id)
    if len(project_exists) > 0:
        project= Project.objects.get(id=id)
        if project.project_creator.id != request.session['user_id']:
            return redirect("/all_projects")
        all_comments = project.has_comments.all().order_by('-created_at')
        context={
            'project': project,
            'user': User.objects.get(id=request.session['user_id']),
            'comments':all_comments
        }
        return render(request,"project_page.html",context)
    return redirect('/all_projects')

def show_all(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    all_projects = Project.objects.filter(project_creator=user)
    context = {
        'user': user,
        'all_projects':all_projects
    }
    return render(request,'all_projects.html', context)

def show_flight(request,flight_name):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    flight_projects = Project.objects.filter(project_creator=user).filter(lead_office = flight_name)
    
    if len(flight_projects) > 0:
        print("Success")
        myFilter = ProjectFilter(request.GET, queryset=flight_projects)
        flight_projects = myFilter.qs
        context = {
            'user': User.objects.get(id = request.session['user_id']),
            'flight_projects':flight_projects.order_by("project_due_date"),
            'myFilter': myFilter,
            'flight_name':flight_name,
            'flight_title': FLIGHT_TITLE[flight_name]
        }
        return render(request,"flight_page.html",context)
    print("No matching projects")
    return redirect('/all_projects')

def add_comment(request,id):
    # def datetimeformat(value, format):
    if 'user_id' not in request.session:
        return redirect('/all_projects')
    errors = Comment.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect(f'/project/{id}')
    else:    
        if request.method == "POST":
            project_exists = Project.objects.filter(id=id)
            if len(project_exists) > 0:
                project = Project.objects.get(id = id)
            if project.project_creator.id != request.session['user_id']:
                return redirect("/all_projects")
            user = User.objects.get(id = request.session['user_id'])
            comment = Comment.objects.create(
                content = request.POST['comment'],
                comment_creator = user,
                comment_project = project
            )
            return redirect(f'/project/{id}')
    return redirect('/all_projects')

