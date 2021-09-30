from django.urls import path
from .views import index,detail,AddDoctors,AddNurse,AddPatient,register,signin,signout

urlpatterns = [
    path('',index,name='index'),
    path('detail/<int:pk>',detail,name='detail'),
    path('doctor/registration', AddDoctors.as_view(),name='adddoctor'),
    path('nurse/registration', AddNurse.as_view(),name ='addnurse'),
    path('patients/registration',AddPatient.as_view(),name='addpatient'),
    path('register/',register,name='register'),
    path("signin/",signin,name="signin"),
    path('signout/',signout,name='signout')
]
