from UCoE.models import Course, Session_Year,Student, CustomUser, Staff, Subject, Staff_Notification, Staff_Leave, Staff_Feedback, \
    Student_Notification,Student_Feedback,Student_Leave
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    student_gender_male = Student.objects.filter(gender='Male').count()
    student_gender_female = Student.objects.filter(gender='Female').count()
    context = {
        'student_count': student_count,
        'staff_count': staff_count,
        'course_count': course_count,
        'student_gender_male': student_gender_male,
        'student_gender_female': student_gender_female,
    }
    return render(request, 'HOD/HOME.html', context)


@login_required(login_url='/')
def ADD_STUDENT(request, messages=None):
    course = Course.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists')
            return redirect('add_student')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is already in use')
            return redirect('add_student')



        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)

            student = Student(
                admin=user,
                address=address,
                course_id=course,
                gender=gender,

            )
            student.save()
            messages.success(request, user.first_name + "  " + user.last_name + " Are Successfully Added !")
            return redirect('add_student')


    context = {
        'course': course,
    }
    return render(request, 'HOD/AddStudent.html', context)


@login_required(login_url='/')
def VIEW_STUDENT(request):
    student = Student.objects.all()

    context = {
        'student': student,
    }
    return render(request, 'HOD/View_Student.html', context)


@login_required(login_url='/')
def EDIT_STUDENT(request, id):
    student = Student.objects.filter(id=id)
    course = Course.objects.all()
    context = {
        'student': student,
        'course': course,
    }
    return render(request, 'HOD/EditStudent.html', context)


@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')

        user = CustomUser.objects.get(id=student_id)
        user.profile_pic = profile_pic
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        if password != None and password != "":
            user.set_password(password)
            if profile_pic != None and profile_pic != "":
                user.profile_pic = profile_pic

        student = Student.objects.get(admin=student_id)
        student.address = address
        student.gender = gender

        course = Course.objects.get(id=course_id)
        student.course_id = course

        student.save()
        messages.success(request, 'Records are successfully updated')
        return redirect('view_student')
    return render(request, 'HOD/EditStudent.html')


@login_required(login_url='/')
def DELETE_STUDENT(request, admin):
    student = CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request, 'Records are succesfully deleted')
    return redirect('view_student')


@login_required(login_url='/')
def ADD_COURSE(request):
        if request.method == "POST":
            course_name = request.POST.get('course_name')

            course = Course(
                name=course_name,
            )
            course.save()
            messages.success(request, 'Course Are Successfully Created ')
            return redirect('view_course')

        return render(request, 'Hod/add_course.html')


@login_required(login_url='/')
def VIEW_COURSE(request):
    course = Course.objects.all()
    context = {
        'course': course,
    }
    return render(request, 'HOD/view_course.html', context)


@login_required(login_url='/')
def EDIT_COURSE(request, id):
    course = Course.objects.get(id=id)

    context = {
        'course': course,
    }
    return render(request, 'HOD/edit_course.html', context)


@login_required(login_url='/')
def UPDATE_COURSE(request):
    if request.method == 'POST':
        name = request.POST.get('course_name')
        course_id = request.POST.get('course_id')

        course = Course.objects.get(id=course_id)
        course.name = name
        messages.success(request, 'Course are successfully updated')
        return redirect('view_course')

    return render(request, 'HOD/edit_course.html')


@login_required(login_url='/')
def DELETE_COURSE(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, 'Course is deleted successfully')
    return redirect('view_course')


@login_required(login_url='/')
def ADD_STAFF(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists')
            return redirect('add_staff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is already in use')
            return redirect('add_staff')

        else:
            user = CustomUser(first_name=first_name, last_name=last_name, email=email, username=username,
                              profile_pic=profile_pic, user_type=2, )
            user.set_password(password)
            user.save()
            staff = Staff(
                admin=user,
                address=address,
                gender=gender,
            )
            staff.save()
            messages.success(request, 'Staff are successfully added')
            return redirect('add_student')

    return render(request, 'HOD/add_staff.html')


@login_required(login_url='/')
def VIEW_STAFF(request):
    staff = Staff.objects.all()

    context = {
        'staff': staff,

    }
    return render(request, 'HOD/view_staff.html', context)


@login_required(login_url='/')
def EDIT_STAFF(request, id):
    staff = Staff.objects.get(id=id)

    context = {
        'staff': staff
    }
    return render(request, 'HOD/edit_staff.html', context)


@login_required(login_url='/')
def UPDATE_STAFF(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id=staff_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if password != None and password != "":
            user.set_password(password)
            if profile_pic != None and profile_pic != "":
                user.profile_pic = profile_pic

        user.save()
        staff = Staff.objects.get(admin=staff_id)
        staff.address = address
        staff.gender = gender

        staff.save()
        messages.success(request, 'Staff is Successfully Updated')
        return redirect('view_staff')

    return render(request, 'HOD/edit_staff.html')


@login_required(login_url='/')
def DELETE_STAFF(request, id):
    staff = CustomUser.objects.get(id=admin)
    staff.delete()
    messages.success(request, 'Records are successfully deleted')

    return redirect('view_staff')


@login_required(login_url='/')
def ADD_SUBJECT(request):
    course = Course.objects.all()
    staff=Staff.objects.all()

    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id=request.POST.get('staff_id')

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject(
            name=subject_name,
            course=course,
            staff=staff,

        )
        subject.save()
        messages.success(request,'Subject is successfully added')
        return redirect('add_subject')

    context = {
        'course': course,
        'staff':staff,
    }
    return render(request, 'HOD/add_subject.html', context)


@login_required(login_url='/')
def VIEW_SUBJECT(request):
    subject = Subject.objects.all()
    staff=Staff.objects.all()
    context = {
        'subject': subject,
        'staff':staff,
    }
    return render(request, 'HOD/view_subject.html', context)


@login_required(login_url='/')
def EDIT_SUBJECT(request, id):
    subject = Subject.objects.get(id=id)
    course=Course.objects.all()
    staff=Staff.objects.all()
    context = {
        'subject': subject,
        'course':course,
        'staff':staff,
    }
    return render(request, 'HOD/edit_subject.html', context)



@login_required(login_url='/')
def UPDATE_SUBJECT(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id=request.POST.get('staff_id')
        subject_name=request.POST.get('subject_name')

        course = Course.objects.get(id=course_id)
        staff=Staff.objects.get(id=staff_id)
        subject = Subject(
            id=subject_id,
            name=subject_name,
            course=course,
            staff=staff,
        )
        subject.save()
        messages.success(request,'Subjects is successfully updated')
        return redirect('view_subject')
    return render(request, 'HOD/edit_subject.html')


@login_required(login_url='/')
def STAFF_SEND_NOTIFICATION(request):
    staff = Staff.objects.all()
    see_notification = Staff_Notification.objects.all().order_by('-id')[0:10]

    context = {
        'staff': staff,
        'see_notification': see_notification,
    }
    return render(request, 'HOD/staff_notification.html', context)


@login_required(login_url='/')
def STAFF_SAVE_NOTIFICATIONS(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')

        staff = Staff.objects.get(admin=staff_id)
        notifications = Staff_Notification(
            staff_id=staff,
            message=message,

        )
        notifications.save()
        messages.success(request, 'Notification is successfully sent')
        return redirect('staff_send_notification')


@login_required(login_url='/')
def STAFF_LEAVE_VIEW(request):
    staff_leave = Staff_Leave.objects.all()
    context = {
        'staff_leave': staff_leave,
    }
    return render(request, 'HOD/staff_leave.html', context)


@login_required(login_url='/')
def STAFF_APPROVE_LEAVE(request, id):
    leave = Staff_Leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect('staff_leave_view')


@login_required(login_url='/')
def STAFF_DISAPPROVE_LEAVE(request, id):
    leave = Staff_Leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('staff_leave_view')


@login_required(login_url='/')
def STAFF_FEEDBACK_REPLY(request):
    feedback = Staff_Feedback.objects.all()
    feedback_history = Staff_Feedback.objects.all().order_by('-id')[0:10]
    context = {
        'feedback': feedback,
        'feedback_history': feedback_history,
    }

    return render(request, 'HOD/staff_feedback_reply.html', context)


@login_required(login_url='/')
def STAFF_FEEDBACK_REPLY_SAVE(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Staff_Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()
        return redirect('staff_feedback_reply')


@login_required(login_url='/')
def STUDENT_SEND_NOTIFICATIONS(request):
    student = Student.objects.all()
    student_notifications = Student_Notification.objects.all()
    context = {
        'student': student,
        'student_notifications': student_notifications,
    }
    return render(request, 'HOD/student_notifications.html', context)


@login_required(login_url='/')
def STUDENT_SAVE_NOTIFICATIONS(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        message = request.POST.get('message')

        student = Student.objects.get(admin=student_id)

        stud_notification = Student_Notification(
            student_id=student,
            message=message,
        )
        stud_notification.save()
        messages.success(request, 'Your Notification is Successfully Sent!')
        return redirect('student_send_notifications')

@login_required(login_url='/')
def STUDENT_FEEDBACK(request):
    feedback = Student_Feedback.objects.all()
    feedback_history=Student_Feedback.objects.all().order_by('-id')[0:10]
    context={
        'feedback':feedback,
        'feedback_history':feedback_history,
    }
    return render(request,'HOD/student_feedback.html', context)

@login_required(login_url='/')
def STUDENT_FEEDBACK_REPLY_SAVE(request):
    if request.method=="POST":
        feedback_id=request.POST.get('feedback_id')
        feedback_reply=request.POST.get('feedback_reply')
        feedback = Student_Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()
        return redirect('get_student_feedback')


def STUDENT_LEAVE_VIEW(request):
    student_leave=Student_Leave.objects.all()
    context={
        'student_leave':student_leave,
    }
    return render(request,'HOD/student_leave.html', context)


def STUDENT_APPROVE_LEAVE(request,id):
    leave = Student_Leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect('student_leave_view')


def STUDENT_DISAPPROVE_LEAVE(request,id):
    leave = Student_Leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('student_leave_view')


def ADD_SESSION(request):
    if request.method=="POST":
        session_start=request.POST.get('session_start')
        session_end=request.POST.get('session_end')

        session=Session_Year(
            session_start=session_start,
            session_end=session_end,
        )
        session.save()
        messages.success(request,'Your Session is successfully added!')
        return redirect('add_session')
    return render(request,'HOD/add_session.html')


def VIEW_SESSION(request):
    session=Session_Year.objects.all()


    context={
        'session':session,
    }
    return render(request,'HOD/view_session.html',context)


def EDIT_SESSION(request,id):
    session=Session_Year.objects.filter(id=id)
    context={
        'session':session,
    }

    return render(request,'HOD/edit_session.html',context)


def UPDATE_SESSION(request):
    if request.method=="POST":
        session_id=request.POST.get('session_id')
        session_start=request.POST.get('session_start')
        session_end=request.POST.get('session_end')

        session=Session_Year(
            id=session_id,
            session_start=session_start,
            session_end=session_end,

        )
        session.save()
        messages.success(request,'Session is Successfully Updated')
        return redirect('view_session')


def DELETE_SESSION(request,id):
    session=Session_Year.objects.get(id=id)
    session.delete()
    messages.success(request,'Session is Successfully Deleted!')

    return redirect('view_session')