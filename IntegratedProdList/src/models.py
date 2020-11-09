from django.db import models
import re
import bcrypt
import csv
# import pandas as pd
# import numpy
# from numpy.core import _multiarray_umath

def MEMBER_CHOICES(file):
    person_list = []
    with open(fileName, newline='',encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['lastName'].upper()+", "+row['firstName'].upper()
            item = tuple([name, name])
            person_list.append(item)
        return tuple(person_list)

fileName = "./data/personnelData.csv"
# data = pd.read_excel(fileName)
# def MEMBER_CHOICES(df):
#     return tuple(tuple([row['id'],row['lastName'].upper()+", "+row['firstName'].upper()]) for ind, row in data.iterrows())

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['first_name']) < 2:
            errors['first_name'] = 'First Name must be at least 2 characters'

        if len(form['last_name']) < 2:
            errors['last_name'] = 'Last Name must be at least 2 characters'

        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Invalid Email Address'
        
        email_check = self.filter(email=form['email'])
        if email_check:
            errors['email'] = "Email already in use"

        if len(form['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        
        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'
        
        return errors
    
    def authenticate(self, email, password):
        users = self.filter(email=email)
        if not users:
            return False

        user = users[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())

    def register(self, form):
        pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name = form['first_name'],
            last_name = form['last_name'],
            email = form['email'],
            password = pw,
        )
        
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    objects = UserManager()

class ProjectManager(models.Manager):
    pass

class Project(models.Model):
    NOD_CHOICES = (
        ('Nod Problem 1','Nod Problem 1'),
        ('Nod Problem 2','Nod Problem 2'),
        ('Nod Problem 3','Nod Problem 3'),
        ('Nod Problem 4','Nod Problem 4'),
        ('Nod Problem 5','Nod Problem 5'),
        )
    ML_CHOICES = (
        ("Mission Line 1", "Mission Line 1"),
        ("Mission Line 2", "Mission Line 2"),
        ("Mission Line 3", "Mission Line 3"),
        ("Mission Line 4", "Mission Line 4"),
        ("Mission Line 5", "Mission Line 5"),
    )
    PRI_CHOICES = (
        ("HIGH","HIGH"),
        ("MED","MED"),
        ("LOW", "LOW")
    )

    STATUS_CHOICES = (
        ("WORKING","WORKING"),
        ("ON HOLD","ON HOLD"),
        ("CANCELLED","CANCELLED")
    )

    ORG_CHOICES = (
        ("ACN","ACN"),
        ("ACNA","ACNA"),
        ("ACNI","ACNI"),
        ("ACNL","ACNL"),
        ("ACNQ","ACNQ"),
        ("ACNS","ACNS"),
        ("ACNW","ACNW"),
    )
    
    nod_problem = models.CharField(max_length=20, choices=NOD_CHOICES)
    mission_line = models.CharField(max_length = 30, choices=ML_CHOICES)
    secondary_mission_line = models.CharField(max_length=30, choices=ML_CHOICES, blank=True, null=True)
    project_title = models.CharField(max_length=255)
    analytic_intent = models.TextField(blank=True)
    project_lead = models.CharField(max_length = 100, choices=MEMBER_CHOICES(fileName)) #, 
    lead_office = models.CharField(max_length=50, choices=ORG_CHOICES)
    contributors = models.CharField(max_length=255,blank=True)
    product_types = models.CharField(max_length=255,blank=True) #add choices
    country = models.CharField(max_length=100,blank=True)  #add choices
    priority = models.CharField(max_length = 10, choices =PRI_CHOICES,blank=True)
    project_status = models.CharField(max_length=10, choices=STATUS_CHOICES, blank=True)
    project_start_date = models.DateField(blank=True, null=True)
    project_due_date = models.DateField(blank=True, null=True)
    project_complete_date = models.DateField(blank=True, null=True)
    project_creator = models.ForeignKey(User, related_name="created_projects",on_delete=models.CASCADE,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CommentManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['comment']) ==0:
            errors['comment'] = 'Comments cannot be empty'
        return errors

class Comment(models.Model):
    content = models.TextField()
    comment_creator = models.ForeignKey(User, related_name="has_created_comments", on_delete=models.CASCADE)
    comment_project = models.ForeignKey(Project, related_name="has_comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()
    