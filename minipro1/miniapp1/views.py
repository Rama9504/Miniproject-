from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from miniapp1.models import student,HonorsSub,BTSubject,BTStudentRegistrations,HonorsRegistration,BTmarks,HonorsMarks
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    return render(request,"index.html")

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        conpassword=request.POST['password1']
        if User.objects.filter(username=username):
            messages.error(request,"username already exists")
        elif User.objects.filter(email=email):
            messages.error(request,"Email already registered")
        elif len(username)>10:
            messages.error(request,"username must be under 10 characters")
        elif password!=conpassword:
            messages.error(request,"password didn't match")
        elif not username.isalnum():
            messages.error(request,"username must be a alpha numeric")
        else:
            myuser = User.objects.create_user(username, email, password)
            myuser.save()
            messages.success(request, "Your Account has been created succesfully!!")
            return redirect('signin')
    return render(request,"signup.html")

def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password1=request.POST['password']
        user=student.objects.filter(Username=username,Password=password1).first()
        if user is not None:
            user=authenticate(request=request,username=username,password=password1)
            login(request,user)
            return render(request,"main.html")
        
        else:
            messages.error(request,"you entered wrong credentials")
            return render( request,"signin.html")
        
    return render(request,"signin.html")


def acadregistration(request):
    if request.method=="POST":
        username=request.POST['username']
        sem=request.POST['semester']
        branch=request.POST['branch']
        password1=request.POST['password']
        user=student.objects.filter(Username=username,Sem=sem,Dept=branch,Password=password1).first()
        if user is not None:
            users = get_object_or_404(student, Username=username)
            ins=BTStudentRegistrations(student_id=users,branch=branch,semester=sem)
            ins.save() 
        else:
            messages.error(request,"you entered wrong Credentials")
            return render( request,"acadregistration.html")
    return render(request,"acadregistration.html")

def main(request):
    return render(request,"main2.html")

def honregistration(request):
    sub=HonorsSub.objects.all()
    context ={'subs':sub}
    if request.method=="POST":
        username=request.POST['username']
        sem=request.POST['semester']
        branch=request.POST['branch']
        honors_id=request.POST['honorssub']
        password1=request.POST['password']
        user=student.objects.filter(Username=username,Sem=sem,Dept=branch,Password=password1).first()
        subs=HonorsSub.objects.filter(honors_id=honors_id).first()
        print(subs.branch)
        print(branch)
        if subs.branch==branch:
            if user is not None:
                honors=get_object_or_404(HonorsSub,honors_id=honors_id)
                users = get_object_or_404(student, Username=username)
                ins=HonorsRegistration(student_id=users,honors_id=honors,branch=branch,semester=sem)
                ins.save() 
                return render(request,"honregistration2.html",{'branch':branch})
            else:
                messages.error(request,"you entered wrong Credentials")
                return render( request,"honregistration.html")
        else:
            messages.error(request,"You should select your branch courses only")
    return render(request,"honregistration.html",context)

def honregistration2(request):
    return render(request,"honregistration2.html")


#def result(request):
#    logged_in_student = request.user.username
#    student_marks_by_semester = {}
#    all_student_marks = BTmarks.objects.filter(Username=logged_in_student).order_by('semester')
#    for mark in all_student_marks:
#        semester = mark.semester
#        if semester not in student_marks_by_semester:
#            student_marks_by_semester[semester] = []
#        student_marks_by_semester[semester].append(mark)
#    semester_sgpa = {}
#    for semester, marks in student_marks_by_semester.items():
#        total_credits = 0
#        weighted_grade_points = 0
#        for mark in marks:
#            subject = BTSubject.objects.get(Sub_id=mark.Course_id.Sub_id)
#            credits = subject.Credits
#            grade_point = mark.grade
#            total_credits += credits
#            weighted_grade_points += credits * grade_point
#        
#        sgpa = weighted_grade_points / total_credits
#        semester_sgpa[semester] = sgpa
#        context = {'semester_sgpa': semester_sgpa}
#    return render(request, "result.html", context)
#
#
#
#from django.db.models import Sum, Count

#def result(request):
#    # Fetch all the courses of the student for the given semester
#    logged_student=request.user.username
#    logged_in_student = request.user.Sem
#    courses = BTmarks.objects.filter(Username_id=logged_student)
#    total_credits = courses.aggregate(Sum('Course_id__Credits'))['Course_id__Credits__sum']
#    if total_credits is None:
#        return 0.0
#
#    # Calculate total grade points earned by the student
#    total_grade_points = courses.aggregate(Sum('grade'))['grade__sum']
#    
#    # Calculate SGPA
#    sgpa = total_grade_points / total_credits
#
#    # Check if the student is registered for Honors in this semester
#    honors_registered = HonorsRegistration.objects.filter(student_id_id=logged_student, semester=logged_in_student).exists()
#    if honors_registered:
#        # Fetch the Honors course for this semester
#        honors_course = HonorsRegistration.objects.get(student_id_id=logged_student, semester=logged_in_student).honors_id
#        # Add the Honors course credits and grade points to the total
#        sgpa = (sgpa * total_credits + honors_course.credits * honors_course.grades) / (total_credits + honors_course.credits)
#        # Update the total credits with the Honors course credits
#        total_credits += honors_course.credits
#        print(sgpa)
#
#    return sgpa

def result(request):
    logged_in_student = request.user.username
    student_marks_by_semester = {}
    all_student_marks = BTmarks.objects.filter(Username=logged_in_student).order_by('semester')
    for mark in all_student_marks:
        semester = mark.semester
        if semester not in student_marks_by_semester:
            student_marks_by_semester[semester] = []
        student_marks_by_semester[semester].append(mark)
    honors_marks_by_semester = {}
    all_honors_marks = HonorsMarks.objects.filter(Username=logged_in_student).order_by('semester')
    for mark in all_honors_marks:
        semester = mark.semester
        if semester not in honors_marks_by_semester:
            honors_marks_by_semester[semester] = []
        honors_marks_by_semester[semester].append(mark)
    
    semester_sgpa = {}
    for semester, marks in student_marks_by_semester.items():
        total_credits = 0
        weighted_grade_points = 0    
        for mark in marks:
            subject = BTSubject.objects.get(Sub_id=mark.Course_id.Sub_id)
            credits = subject.Credits
            grade_point = mark.grade
            total_credits += credits
            weighted_grade_points += credits * grade_point
            
        if semester in honors_marks_by_semester:
            print("hi")
            for mark in honors_marks_by_semester[semester]:
                honors_subject = HonorsSub.objects.get(honors_id=mark.Honors_id.honors_id)
                credits = honors_subject.credits
                grade_point = mark.grades
                total_credits += credits
                weighted_grade_points += credits * grade_point
        
        sgpa = weighted_grade_points / total_credits
        semester_sgpa[semester] = sgpa
    context = {'semester_sgpa': semester_sgpa,'data':all_student_marks,'hondata':all_honors_marks}
    return render(request, "result.html", context)

def signout(request):
    return render(request,"signin.html")







