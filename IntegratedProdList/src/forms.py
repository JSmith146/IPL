from django import forms
from .models import *


class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('nod_problem', 'mission_line', 'secondary_mission_line','project_title','analytic_intent',
                'project_lead','lead_office','contributors','product_types','country','priority','project_status',
                'project_start_date','project_due_date')