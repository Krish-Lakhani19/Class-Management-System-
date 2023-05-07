from django.shortcuts import render, redirect
from UCoE.models import Staff, Staff_Notification, Staff_Leave,Staff_Feedback,Student,Course,Subject,Session_Year,Student_Result
from django.contrib import messages
from django.contrib.auth.decorators import login_required



@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    student_gender_male = Student.objects.filter(gender='Male').count()
    student_gender_female = Student.objects.filter(gender='Female').count()
    context = {
        'student_count': student_count,
        'student_gender_male': student_gender_male,
        'student_gender_female': student_gender_female,
    }
    return render(request, 'STAFF/home.html',context)


@login_required(login_url='/')
def NOTIFICATIONS(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id

        notifications = Staff_Notification.objects.filter(staff_id=staff_id)

        context = {
            'notifications': notifications,

        }
        return render(request, 'STAFF/NOTIFICATIONS.html', context)


@login_required(login_url='/')
def STAFF_MARK_AS_DONE(request, status):
    notifications = Staff_Notification.objects.get(id=status)
    notifications.status = 1
    notifications.save()
    return redirect('notifications')


@login_required(login_url='/')
def STAFF_APPLY_LEAVE(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id
        staff_leave_history = Staff_Leave.objects.filter(staff_id=staff_id)

        context = {
            'staff_leave_history': staff_leave_history,
        }
        return render(request, 'STAFF/Apply_Leave.html', context)

@login_required(login_url='/')
def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        reason_for_leave = request.POST.get('reason_for_leave')

        staff = Staff.objects.get(admin=request.user.id)

        leave = Staff_Leave(
            staff_id=staff,
            data=leave_date,
            message=reason_for_leave,

        )
        leave.save()
        messages.success(request, 'Your Leave is Successfully Applied')
        return redirect('staff_apply_leave')


@login_required(login_url='/')
def STAFF_FEEDBACK(request):
    staff_id=Staff.objects.get(admin=request.user.id)
    feedback_history = Staff_Feedback.objects.filter(staff_id=staff_id)

    context = {
        'feedback_history': feedback_history,

    }
    return render(request, 'STAFF/Feedback.html', context)

@login_required(login_url='/')
def STAFF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')

        staff=Staff.objects.get(admin=request.user.id)

        feedback = Staff_Feedback(
            staff_id=staff,
            feedback=feedback,
            feedback_reply="",
        )
        feedback.save()
        messages.success(request,'Your Feedback has been recorded')
        return redirect('staff_feedback')

@login_required(login_url='/')
def STAFF_ADD_RESULT(request):
    staff=Staff.objects.get(admin=request.user.id)
    subjects=Subject.objects.filter(staffs_id= staff)
    session_year=Session_Year.objects.all()
    action=request.GET.get('action')
    get_subject=None
    get_session=None
    students=None
    if action is not None:
        if request.method=="POST":
            subject_id=request.POST.get('subject_id')
            session_year=request.POST.get('session_year_id')
            get_subject=Subject.objects.get(id=subject_id)
            get_session=Session_Year.objects.get(id=session_year)
            subjects=Subject.objects.filter(id=subject_id)
            for i in subjects:
                student_id=i.course_id
                students=Student.objects.filter(course_id=student_id)
    context={
        'subjects':subjects,
        'session_year':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_session':get_session,
        'students':students,
    }

    return render(request,'STAFF/add_result.html',context)


def STAFF_SAVE_RESULT(request):
    if request.method=="POST":
        subject_id=request.POST.get('subject_id')
        session_year_id=request.POST.get('session_year_id')
        student_id=request.POST.get('student_id')
        assignment_mark=request.POST.get('assignment_mark')
        Exam_mark=request.POST.get('Exam_mark')

        get_student=Student.objects.get(admin=student_id)
        get_subject=Subject.objects.get(id=subject_id)

        check_exists=Student_Result.objects.filter(subject_id=get_subject,student_id=get_student).exists
        if check_exists:
            result=Student_Result.objects.get(subject_id=get_subject,student_id=get_student)
            result.assignment_marks=assignment_mark
            result.exam_marks=Exam_mark
            result.save()
            messages.success(request,'Result is successfully Updated1')
            return redirect('staff_add_result')
        else:
            result=Student_Result(
                student_id=get_student,
                subject_id=get_subject,
                exam_marks=Exam_mark,
                assignment_marks=assignment_mark,
            )
            result.save()
            messages.success(request,'Result is Successfully Added!')
            return redirect('staff_add_result')