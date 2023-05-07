from django.shortcuts import render,redirect
from UCoE.models import Student_Notification,Student,Student_Feedback,Student_Leave,Student_Result
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='/')
def STUDENT_HOME(request):
    result_count=Student_Result.objects.all().count()

    assignment_marks = Student_Result.objects.all().count()
    exam_marks = Student_Result.objects.all().count()
    context={
        'assignment_marks':assignment_marks,
        'exam_marks':exam_marks,
        'result_count':result_count,

    }
    return render(request,'STUDENT/home.html',context)

@login_required(login_url='/')
def STUDENT_NOTIFICATIONS(request):
    student=Student.objects.filter(admin = request.user.id)
    for i in student:
        student_id=i.id
        notification=Student_Notification.objects.filter(student_id=student_id)

        context = {

            'notification':notification,
        }
        return render(request,'STUDENT/student_notifications.html', context)

@login_required(login_url='/')
def STUDENT_MARK_AS_DONE(request,status):
    notifications = Student_Notification.objects.get(id = status)
    notifications.status= 1
    notifications.save()
    return redirect('student_notifications')

@login_required(login_url='/')
def STUDENT_FEEDBACK(request):
    student_id=Student.objects.get(admin = request.user.id)
    feedback_history=Student_Feedback.objects.filter(student_id=student_id)
    context={
        'feedback_history':feedback_history
    }
    return render(request,'STUDENT/student_feedback.html',context)

@login_required(login_url='/')
def STUDENT_FEEDBACK_SAVE(request):
    if request.method=="POST":
        student = Student.objects.get(admin=request.user.id)
        feedback=request.POST.get('feedback')

        feedbacks=Student_Feedback(
            student_id=student,
            feedback=feedback,
            feedback_reply=""

        )
        feedbacks.save()
        messages.success(request, 'Your Feedback has been recorded')
        return redirect('student_feedback')

@login_required(login_url='/')
def STUDENT_LEAVE(request):
    student = Student.objects.get(admin=request.user.id)
    student_leave_history = Student_Leave.objects.filter(student_id=student)
    context = {
        'student_leave_history': student_leave_history,
    }
    return render(request,'STUDENT/student_leave.html', context)

@login_required(login_url='/')
def STUDENT_LEAVE_SAVE(request):
    if request.method=="POST":
        leave_date=request.POST.get('leave_date')
        reason_for_leave=request.POST.get('reason_for_leave')
        student_id=Student.objects.get(admin =request.user.id)
        student_leave=Student_Leave(
            student_id=student_id,
            data=leave_date,
            message=reason_for_leave,

        )
        student_leave.save()
        messages.success(request,'Your Application for leave is successfully applied')

        return redirect('student_leave')

@login_required(login_url='/')
def STUDENT_VIEW_RESULT(request):

    student=Student.objects.get(admin=request.user.id)
    marks=None

    result=Student_Result.objects.filter(student_id=student)
    for i in result:
        assignment_mark=i.assignment_marks
        exam_marks=i.exam_marks

        marks=assignment_mark+exam_marks

    context={
        'result':result,
        'marks':marks,
    }
    return render(request,'STUDENT/View_Result.html',context)