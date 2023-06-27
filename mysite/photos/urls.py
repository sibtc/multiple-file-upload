from django.conf.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^clear/$', views.clear_database, name='clear_database'),
    re_path(r'^basic-upload/$', views.BasicUploadView.as_view(), name='basic_upload'),
    re_path(r'^progress-bar-upload/$', views.ProgressBarUploadView.as_view(), name='progress_bar_upload'),
    re_path(r'^drag-and-drop-upload/$', views.DragAndDropUploadView.as_view(), name='drag_and_drop_upload'),
]
