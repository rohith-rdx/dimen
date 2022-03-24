from xml.dom.minidom import Document
from django.urls import URLPattern, re_path,include
from django.contrib import admin
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path(r'^$', views.category, name="category"),
    re_path(r'^add_category$', views.add_category, name="add_category"),
    re_path(r'^cat_delete/(?P<cat_id>\d+)$', views.cat_delete, name="cat_delete"),

    
    
    
]