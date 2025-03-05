from django.db import models
from django.utils import timezone

class Task(models.Model):
    my_status = [
        ('overdue', 'Overdue'),
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

    id = models.AutoField(primary_key=True) #primary key
    title = models.CharField(max_length=100) #title is required
    description = models.TextField(blank=True, null=True) #optional input for description
    due_date = models.DateField() #due date is required
    status = models.CharField(max_length=20, choices=my_status, default='pending') #default status is set to pending,

    def save(self, *args, **kwargs):
        today = timezone.now().date()
        if self.due_date < today: #if due date is less than today the status will be overdue
            self.status = 'overdue'
        elif self.due_date == today: #if exactly equal, then its complete
            self.status = 'completed'
        else:
            self.status = 'pending'  #if its greater than today then it is pending
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title