from django.urls import re_path, include
from rest_framework import routers
from . import views

app_name = "amdax_app"

router = routers.DefaultRouter()
router.register(r'api/photos', views.PhotoViewSet)


urlpatterns = [
    re_path(r'^clear/$', views.clear_database, name='clear_database'),
    re_path(r'^basic-upload/$', views.BasicUploadView.as_view(), name='basic_upload'),
    re_path(r'^progress-bar-upload/$', views.ProgressBarUploadView.as_view(), name='progress_bar_upload'),
    re_path(r'^drag-and-drop-upload/$', views.DragAndDropUploadView.as_view(), name='drag_and_drop_upload'),
    re_path('', include(router.urls)),
    re_path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
