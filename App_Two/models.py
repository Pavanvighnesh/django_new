from django.db import models

class Topic(models.Model):
    top_name=models.CharField(max_length=100,unique=True)
    date1=models.DateTimeField()
    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic=models.ForeignKey(Topic,models.CASCADE)
    name=models.CharField(max_length=100,unique=True)   
    url=models.URLField(unique=True) 

    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,models.CASCADE)
    date=models.DateField()

    def __str__(self):
        return str(self.name)  
    

class user(models.Model):
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=120)
    email_id=models.EmailField()   

    def __str__(self):
        return self.First_name 
    


