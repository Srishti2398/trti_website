from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf.urls import url


urlpatterns = [
    path('',views.home, name = 'home'),
    path('gallery/',views.gallery, name = 'gallery'),
    path('map/',views.map, name = 'map'),
     path('aboutus/',views.aboutus, name = 'aboutus'),
     path('villages/',views.villages, name = 'villages'),
     path('whoswho/',views.whoswho, name = 'whoswho'),
     path('umainstitutes/',views.umainstitutes, name = 'umainstitutes'),
     path('proposedschemes/',views.proposedschemes, name = 'proposedschemes'),
     path('contactus/',views.contactus, name = 'contactus'),
     path('background/',views.background, name = 'background'),
     path('vision/',views.vision, name = 'vision'),
     path('coursesdetails/',views.coursesdetails, name = 'coursesdetails'),
     path('reports/',views.reports, name = 'reports'),
     path('links/',views.links, name = 'links'),
    
]
