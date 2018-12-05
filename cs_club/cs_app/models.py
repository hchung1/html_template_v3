from django.db import models

# Create your models here.
class display(models.Model):
    Place_Choices = (
        ('home',"Home"),
        ('about',"About"),
    )
    place=models.CharField(max_length=5, choices=Place_Choices,default='home',)
    image=models.CharField(max_length=255)
    text=models.CharField(max_length=255)


class member(models.Model):
    Position_Choices = (
        ('Member','Member'),
        ('Secretary','Secretary'),
        ('Treasurer','Treasurer'),
        ('Vice President','Vice President'),
        ('President','President'),
        ('Former-Secretary','Former-Secretary'),
        ('Former-Treasurer','Former-Treasurer'),
        ('Former-Vice President','Former-Vice President'),
        ('Former-President','Former-President'),
    )
    member_id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    position=models.CharField(max_length=25,choices=Position_Choices,default='Member',)
    phone=models.IntegerField()
    email=models.CharField(max_length=100)
    image=models.CharField(max_length=255)


class trip(models.Model):
    trip_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=255)
    restriction=models.CharField(max_length=255)
    deadline=models.DateField()
    registrar=models.CharField(max_length=255)
    image=models.CharField(max_length=255, null=True)


class project(models.Model):
    project_id=models.AutoField(primary_key=True)
    image=models.CharField(max_length=255)
    date = models.DateField()
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=255)



