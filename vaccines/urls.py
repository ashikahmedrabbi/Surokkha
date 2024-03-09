
from django.urls import path,include
from . import views
from .views import AddVaccines, EditVaccines, delete_vaccines, Detailvaccines, borrow_vaccines ,BorrowvaccinesList

urlpatterns = [
   
    path('add_vaccines/', AddVaccines.as_view(), name='add_vaccines'),
    path('edit_vaccines/<int:id>/',EditVaccines.as_view(), name='edit_vaccines'),
    path('delete_vaccines/<int:id>/',delete_vaccines.as_view(), name='delete_vaccines'),
    path('vaccines/', views.vaccines_list, name='vaccines'),
    path('patientsvaccines/', views.patients_vaccines_list, name='patientsvaccines'),
    path('details/<int:id>/', views.Detailvaccines.as_view(), name='details'),
    path('borrow/<int:id>/', views.borrow_vaccines.as_view(), name='borrow'),  
    path('borrowbook/', BorrowvaccinesList.as_view(), name='borrow_vaccines_lists'),

]