from django.db import models
# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField(max_length=100)
    duedate = models.DateField()
    priority = models.CharField(null=True, blank=True)  
    status = models.CharField()  
    #status = models.CharField(max_length=20, choices=[("Pending", "Pending"), ("Completed", "Completed")], default="Pending")
    completed = models.BooleanField(default=False)  

    def __str__(self):
        return self.title