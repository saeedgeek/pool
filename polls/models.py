from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pool(models.Model):
    question=models.CharField(max_length=100)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

class Choice(models.Model):
    poll=models.ForeignKey(Pool,related_name='choices',on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.choice_text
    
class Vote(models.Model):
    poll=models.ForeignKey(Pool,on_delete=models.CASCADE,related_name='vote')
    choice=models.ForeignKey(Choice,on_delete=models.CASCADE,related_name='vote')
    voted_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='vote')

    class Meta:
        unique_together=('poll','voted_by')
