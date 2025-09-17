# models.py
from django.db import models

class Tasks(models.Model):
    # Define the choices for status in a single, reusable location
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]
    
    # Define the choices for priority as a named attribute
    PRIORITY_CHOICES = [
        ('high', 'high'),
        ('medium', 'medium'),
        ('low', 'low'),
    ]
    
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    duedate = models.DateField()
    
    # Use the defined PRIORITY_CHOICES here
    priority = models.CharField(
        null=False,
        blank=False,
        choices=PRIORITY_CHOICES
    )
    
    status = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        choices=STATUS_CHOICES
    )
    
    def __str__(self):
        return self.title