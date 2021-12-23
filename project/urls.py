from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from .views import *


urlpatterns = [
    path('',index),
    path('add/',add_project),
    path('project/<int:project_id>',project_view),
    path('edit/<int:project_id>',edit_project),
    path('delete/<int:project_id>',delete_project),
    path('project/<int:project_id>/task/add/',add_task),
    path('project/<int:project_id>/task/<int:task_id>/edit/',edit_task),
    path('project/<int:project_id>/task/<int:task_id>/delete/',delete_task),
    path('project/<int:project_id>/task/<int:task_id>/',view_task),
    # path('projects/<int:id>/task/add/',add_task),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
