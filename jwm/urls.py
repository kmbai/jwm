from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='jwm-home'),
    path('Services/', views.services,name='jwm-services'),
    path('Financial/', views.financial,name='jwm-financial'),
    path('Taxation/', views.taxation,name='jwm-taxation'),
    path('CompanySecretary/', views.companysecretary,name='jwm-companysecretary'),
    path('Audit/', views.audit,name='jwm-audit'),
    path('HumanResource/', views.hr,name='jwm-hr'),
    path('Administration/', views.administration,name='jwm-administration'),
    path('Contact/', views.contact,name='jwm-contact'),
    path('AboutUs/', views.aboutus,name='jwm-aboutus'),
    path('Bookkeeping&Accounting/', views.bookkeeping,name='jwm-bookkeeping'),
    path('Other_Services/', views.others,name='jwm-other'),
    path('Careers/', views.careers,name='jwm-careers'),
    path('Location/', views.location,name='jwm-location'),
   
   
    
]