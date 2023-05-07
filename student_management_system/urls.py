
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import VIEWS, HOD_VIEWS, STUDENT_VIEWS, STAFF_VIEWS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', VIEWS.BASE, name='base'),
     #LOGIN page

    path('',VIEWS.LOGIN , name='login'),
    path('dologin',VIEWS.dologin,name='dologin'),
    path('dologout',VIEWS.dologout,name='dologout'),
    path('doregister',VIEWS.doregister,name='doregister'),

    #Profile Update
    path('profile',VIEWS.PROFILE,name='profile'),
    path('Profile/Update',VIEWS.PROFILE_UPDATE,name='profile_update'),

    #This is HOD panel url
    path('HOD/HOME',HOD_VIEWS.HOME,name='HOD_HOME'),
    path('HOD/Student/ADD_STUDENT',HOD_VIEWS.ADD_STUDENT,name='add_student'),
    path('HOD/Student/View',HOD_VIEWS.VIEW_STUDENT,name='view_student'),
    path('HOD/Student/Edit/<str:id>',HOD_VIEWS.EDIT_STUDENT,name='edit_student'),
    path('HOD/Student/Update',HOD_VIEWS.UPDATE_STUDENT,name='update_student'),
    path('HOD/Student/Delete/<str:admin>',HOD_VIEWS.DELETE_STUDENT,name='delete_student'),
    path('HOD/Staff/Add',HOD_VIEWS.ADD_STAFF,name='add_staff'),
    path('HOD/Staff/View',HOD_VIEWS.VIEW_STAFF,name='view_staff'),
    path('HOD/Staff/Edit/<str:id>',HOD_VIEWS.EDIT_STAFF,name='edit_staff'),
    path('HOD/Staff/Update',HOD_VIEWS.UPDATE_STAFF,name='update_staff'),
    path('HOD/Staff/Delete/<str:id>',HOD_VIEWS.DELETE_STAFF,name='delete_staff'),
    path('HOD/Course/Add',HOD_VIEWS.ADD_COURSE,name='add_course'),
    path('HOD/Course/View',HOD_VIEWS.VIEW_COURSE,name='view_course'),
    path('HOD/Course/Edit/<str:id>',HOD_VIEWS.EDIT_COURSE,name='edit_course'),
    path('HOD/Course/Update',HOD_VIEWS.UPDATE_COURSE,name='update_course'),
    path('HOD/Course/Delete/<str:id>',HOD_VIEWS.DELETE_COURSE,name='delete_course'),
    path('HOD/Subject/Add',HOD_VIEWS.ADD_SUBJECT,name='add_subject'),
    path('HOD/Subject/View',HOD_VIEWS.VIEW_SUBJECT,name='view_subject'),
    path('HOD/Subject/Edit/<str:id>',HOD_VIEWS.EDIT_SUBJECT,name='edit_subject'),
    path('HOD/Subject/Update',HOD_VIEWS.UPDATE_SUBJECT,name='update_subject'),
    path('HOD/Session/Add',HOD_VIEWS.ADD_SESSION,name='add_session'),
    path('HOD/Session/View',HOD_VIEWS.VIEW_SESSION,name='view_session'),
    path('HOD/Session/Edit/<str:id>',HOD_VIEWS.EDIT_SESSION,name='edit_session'),
    path('HOD/Session/Update',HOD_VIEWS.UPDATE_SESSION,name='update_session'),
    path('HOD/Session/Delete/<str:id>',HOD_VIEWS.DELETE_SESSION,name='delete_session'),
    path('HOD/Staff/Send_Notification',HOD_VIEWS.STAFF_SEND_NOTIFICATION,name='staff_send_notification'),
    path('HOD/Staff/Save_Notifications',HOD_VIEWS.STAFF_SAVE_NOTIFICATIONS,name='staff_save_notifications'),
    path('HOD/Staff/Leave_View',HOD_VIEWS.STAFF_LEAVE_VIEW,name='staff_leave_view'),
    path('HOD/Staff/Approve_Leave/<str:id>',HOD_VIEWS.STAFF_APPROVE_LEAVE,name='staff_approve_leave'),
    path('HOD/Staff/Disapprove_Leave/<str:id>',HOD_VIEWS.STAFF_DISAPPROVE_LEAVE,name='staff_disapprove_leave'),
    path('HOD/Staff/Feedback',HOD_VIEWS.STAFF_FEEDBACK_REPLY,name='staff_feedback_reply'),
    path('HOD/Staff/Feedback/save',HOD_VIEWS.STAFF_FEEDBACK_REPLY_SAVE,name='staff_feedback_reply_save'),
    path('HOD/Student/Send_Notifications',HOD_VIEWS.STUDENT_SEND_NOTIFICATIONS,name='student_send_notifications'),
    path('HOD/Student/Save_Notifications',HOD_VIEWS.STUDENT_SAVE_NOTIFICATIONS,name='student_save_notifications'),
    path('HOD/Student/Feedback',HOD_VIEWS.STUDENT_FEEDBACK,name='get_student_feedback'),
    path('HOD/Student/Feedback/Reply/Save',HOD_VIEWS.STUDENT_FEEDBACK_REPLY_SAVE,name='get_student_feedback_reply_save'),
    path('HOD/Student/Leave_View',HOD_VIEWS.STUDENT_LEAVE_VIEW,name='student_leave_view'),
    path('HOD/Student/Approve_Leave/<str:id>',HOD_VIEWS.STUDENT_APPROVE_LEAVE,name='student_approve_leave'),
    path('HOD/Student/Disapprove_Leave/<str:id>',HOD_VIEWS.STUDENT_DISAPPROVE_LEAVE,name='student_disapprove_leave'),


    #This is Staff Panel

    path('Staff/Home',STAFF_VIEWS.HOME,name='staff_home'),
    path('Staff/Notifications',STAFF_VIEWS.NOTIFICATIONS,name='notifications'),
    path('Staff/MarkAsDone/<str:status>',STAFF_VIEWS.STAFF_MARK_AS_DONE,name='staff_mark_as_done'),
    path('Staff/Apply_Leave',STAFF_VIEWS.STAFF_APPLY_LEAVE,name='staff_apply_leave'),
    path('Staff/Apply_LeaveSave',STAFF_VIEWS.STAFF_APPLY_LEAVE_SAVE,name='staff_apply_leave_save'),
    path('Staff/FeedBack',STAFF_VIEWS.STAFF_FEEDBACK,name='staff_feedback'),
    path('Staff/Feedback/Save',STAFF_VIEWS.STAFF_FEEDBACK_SAVE,name='staff_feedback_save'),
    path('Staff/Add/Result',STAFF_VIEWS.STAFF_ADD_RESULT,name='staff_add_result'),
    path('Staff/Save/Result',STAFF_VIEWS.STAFF_SAVE_RESULT,name='staff_save_result'),



    #This is Student Panel

    path('Student/Home',STUDENT_VIEWS.STUDENT_HOME,name='student_home'),
    path('Student/Notifications',STUDENT_VIEWS.STUDENT_NOTIFICATIONS,name='student_notifications'),
    path('Student/MarkAsDone/<str:status>',STUDENT_VIEWS.STUDENT_MARK_AS_DONE,name='student_mark_as_done'),
    path('Student/FeedBack',STUDENT_VIEWS.STUDENT_FEEDBACK,name='student_feedback'),
    path('Student/Feedback/Save', STUDENT_VIEWS.STUDENT_FEEDBACK_SAVE, name='student_feedback_save'),
    path('Student/Apply_For_Leave',STUDENT_VIEWS.STUDENT_LEAVE,name='student_leave'),
    path('Student/Leave_Save',STUDENT_VIEWS.STUDENT_LEAVE_SAVE,name='student_leave_save'),
    path('Student/View_Result',STUDENT_VIEWS.STUDENT_VIEW_RESULT,name='student_view_result'),




]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
