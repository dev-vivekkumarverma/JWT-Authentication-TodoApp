from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User
import datetime
# Create your models here.

class TodoTask(models.Model):
    title=models.CharField(max_length=200,null=False)
    description=models.TextField(verbose_name='Enter the task description')
    createdOn=models.DateField(default=datetime.date.today())
    deadLine=models.DateField(default=datetime.date.today())  
    createdBy=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title
=======

# Create your models here.
>>>>>>> 80bc9ff6232c54c345c73b938e0ac50b391fc199
