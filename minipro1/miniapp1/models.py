from django.db import models

# Create your models here.
class student(models.Model):

    CYCLE_CHOICES = ( 
        (10, 'PHYSICS'),
        (9, 'CHEMISTRY')
    )

    Username = models.CharField(primary_key=True,max_length=10)
    RollNo = models.IntegerField()
    Name = models.CharField(max_length=255)
    Dept = models.CharField(default="null",max_length=50)
    AdmissionYear = models.IntegerField()
    Gender = models.CharField(max_length=10)
    Phone = models.BigIntegerField(default=0)
    Sem =models.IntegerField(default=1)
    Email= models.CharField(default=0,max_length=50)
    Address1 = models.TextField()
    Cycle = models.IntegerField(default=0, choices=CYCLE_CHOICES)
    Password=models.CharField(max_length=10)
    

    class Meta:
        db_table = 'student'
        constraints = [
            models.UniqueConstraint(fields=['Username'], name='unique_studentRegNo'),
            models.UniqueConstraint(fields=['RollNo'], name='unique_studentRollNo'),
        ]
    managed = True
    
    
class HonorsSub(models.Model):
    honors_id=models.CharField(max_length=7)
    honors_name=models.CharField(max_length=50)
    credits=models.IntegerField(null=True)
    semester=models.IntegerField(null=True)
    branch=models.CharField(max_length=50)
    
class BTSubject(models.Model): 
    BYear = models.IntegerField()
    BSem = models.IntegerField() 
    Dept = models.CharField(default="Null",max_length=10)
    Sub_id = models.CharField(primary_key=True,max_length=10)
    SubCode = models.CharField(max_length=10)
    SubName = models.CharField(max_length=100)
    Credits = models.IntegerField()
    
class BTStudentRegistrations(models.Model):
    student_id=models.ForeignKey('miniapp1.student',on_delete=models.CASCADE)
    branch=models.CharField(max_length=30)
    semester=models.IntegerField()
    class Meta:
        db_table = 'BTStudentRegistrations'
        managed=True
        
class HonorsRegistration(models.Model):
    student_id=models.ForeignKey('miniapp1.student',on_delete=models.CASCADE)
    honors_id=models.ForeignKey('miniapp1.HonorsSub',on_delete=models.CASCADE,null=True)
    branch=models.CharField(max_length=30)
    semester=models.IntegerField()
    class Meta:
        db_table='HonorsRegistration'
        unique_together=(('student_id','honors_id'))
        managed=True
        
        
class BTmarks(models.Model):
    Username=models.ForeignKey('miniapp1.student',on_delete=models.CASCADE)
    Course_id=models.ForeignKey('miniapp1.BTSubject',on_delete=models.CASCADE)
    marks=models.IntegerField()
    grade=models.IntegerField()
    semester=models.IntegerField()
    
class HonorsMarks(models.Model):
    Username=models.ForeignKey('miniapp1.student',on_delete=models.CASCADE)
    Honors_id=models.ForeignKey('miniapp1.HonorsSub',on_delete=models.CASCADE)
    marks=models.IntegerField()
    grades=models.IntegerField()
    semester=models.IntegerField()
    Branch=models.CharField(max_length=30)
    class Meta:
        db_table='HonorsMarks'
        managed=True
    