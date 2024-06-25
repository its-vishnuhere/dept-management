import datetime
from django.db import models

# Create your models here.

class users(models.Model):
    namep=models.CharField(max_length=50,default='null')
    emailid=models.CharField(max_length=50)
    typeur=models.CharField(max_length=12)
    phoneno=models.CharField(max_length=10)
    deptm=models.CharField(max_length=30,default='null')
    passwd=models.CharField(max_length=15,default='null')
    reg_no=models.CharField(max_length=10,default='null')
    dob=models.DateField(default=datetime.date.today())
    gender=models.CharField(max_length=10,default='null')
    address=models.CharField(max_length=50,default='null')
    blooddgp=models.CharField(max_length=10,default='null')
    

class stdprofiledata(models.Model):
    name_sp=models.CharField(max_length=50,default='null')
    reg_no_sp=models.CharField(max_length=10,default='null')
    email_sp=models.CharField(max_length=50,default='null')
    dept_sp=models.CharField(max_length=30,default='null')
    phoneno_sp=models.CharField(max_length=10,default='null')
    bloodgp_sp=models.CharField(max_length=6,default='null')
    batchyr_sp=models.CharField(max_length=12,default='null')  
    dob_sp=models.DateField(max_length=10,default='null')  
    gender_sp=models.CharField(max_length=10,default='null')
    course_sp=models.CharField(max_length=15,default='null')
    address_sp=models.CharField(max_length=50,default='null')
    passwd_sp=models.CharField(max_length=10,default='null')

class trprofiledata(models.Model):
    name_tr=models.CharField(max_length=50,default='null')
    email_tr=models.CharField(max_length=50,default='null')
    dept_tr=models.CharField(max_length=30,default='null')
    phoneno_tr=models.CharField(max_length=10,default='null')
    bloodgp_tr=models.CharField(max_length=6,default='null')
    dob_tr=models.DateField(max_length=10,default='null')
    gender_tr=models.CharField(max_length=10,default='null')
    address_tr=models.CharField(max_length=50,default='null')
    passwd_tr=models.CharField(max_length=10,default='null')


class stdattends(models.Model):
    nameatt=models.CharField(max_length=50,default='null')
    emailidatt=models.CharField(max_length=50)
    regnoatt=models.CharField(max_length=15)
    dateatt=models.DateField(max_length=10,default='null')
    checklistmor=models.CharField(max_length=5,default='null')
    checklisteve=models.CharField(max_length=5,default='null')
    courseatt=models.CharField(max_length=20,default='null')
    batchatt=models.CharField(max_length=12,default='null')

class stdNotifications(models.Model):
    notifydate=models.DateField(max_length=10,default='null')
    notifymsg=models.CharField(max_length=600)
    notifydept=models.CharField(max_length=20)

class time_table(models.Model):
    
    course_t_t=models.CharField(max_length=20,default='null')
    batch_t_t=models.CharField(max_length=12,default='null')
    doc_t_t=models.FileField(upload_to='timetable/')


class study_material(models.Model):
    doc_name=models.CharField(max_length=25,default='null')
    course_doc_1=models.CharField(max_length=20,default='null')
    batch_doc_1=models.CharField(max_length=12,default='null')
    doc_mat=models.FileField(upload_to='material/')

class marks(models.Model):
    name_m=models.CharField(max_length=25)
    email_m=models.CharField(max_length=25)
    course_m=models.CharField(max_length=20)
    sem_m=models.CharField(max_length=20)
    reg_m=models.CharField(max_length=15)
    sgpa_m=models.CharField(max_length=10)