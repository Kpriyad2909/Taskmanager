from django.db import models
# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    duedate = models.DateField()
    priority = models.CharField(null=False,blank=False, choices=[('high', 'high'),('medium', 'medium'),('low', 'low')])  
    status = models.CharField(max_length=20)   
<<<<<<< HEAD
    Task_status = models.CharField(null=False,blank=False,max_length=20, choices=[("Pending", "Pending"), ("In Progress", "In Progress"),("Completed", "Completed")]) 
=======
    completed = models.CharField(null=False,blank=False,max_length=20, choices=[("Pending", "Pending"), ("In Progress", "In Progress"),("Completed", "Completed")]) 
>>>>>>> 243e48f1faac87284f54b9eda3acb04c14e4f464
    

    def __str__(self):
        return self.title