from django.urls import path

from . import views

urlpatterns = [
    path('clear/', views.clear_database, name='clear_database'),
    path('basic-upload/', views.BasicUploadView.as_view(), name='basic_upload'),
    path('progress-bar-upload/', views.ProgressBarUploadView.as_view(), name='progress_bar_upload'),
    path('drag-and-drop-upload/', views.DragAndDropUploadView.as_view(), name='drag_and_drop_upload'),
    path('directory-upload-progress-bar/', views.DirectoryUploadView.as_view(), name='directory_upload_progress_bar'),
]
