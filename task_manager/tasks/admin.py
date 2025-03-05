from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'due_date', 'status'] #displays the title, description, due datee 
    search_fields = ['title'] #searches the title in the search bar
    list_filter = ['status'] #filters the status in the admin page
    
admin.site.register(Task, TaskAdmin) #registers the Task model in the admin page

#for admin purposes onlyyyy