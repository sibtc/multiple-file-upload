from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View

from .forms import PhotoForm, FeedModelForm, FileModelForm
from .models import Photo, FeedFile

import ast
import time


class BasicUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'photos/basic_upload/index.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


class ProgressBarUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'photos/progress_bar_upload/index.html', {'photos': photos_list})

    def post(self, request):
        time.sleep(
            1)  # You don't need this line. This is just to delay the process so you can see the progress bar testing locally.
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


class DragAndDropUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'photos/drag_and_drop_upload/index.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


class DirectoryUploadView(View):
    def get(self, request):
        form = FeedModelForm()
        file_form = FileModelForm()

        file_list = FeedFile.objects.all()

        context = {
            'file_form': file_form,
            'form': form,
            'files': file_list,
        }

        return render(self.request, 'photos/multi_file_upload_progress_bar/index.html', context)

    def post(self, request):
        form = FeedModelForm(self.request.POST)
        file_form = FileModelForm(self.request.POST, self.request.FILES)
        files = request.FILES.getlist('file')

        if form.is_valid() and file_form.is_valid():
            feed_instance = form.save()

            directories = form.cleaned_data.get('directories')
            directories = ast.literal_eval(directories)

            for file in files:
                base_dir = ''
                for directory in list(directories.keys()):
                    if str(file) == directory:
                        base_dir = directories[directory].removesuffix(directory) + str(file)
                        break

                file_instance = FeedFile(file=file, base_dir=base_dir, feed=feed_instance)
                file_instance.save()

                data = {'is_valid': True, 'name': file_instance.file.name, 'url': file_instance.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


def clear_database(request):
    for photo in Photo.objects.all():
        photo.file.delete()
        photo.delete()

    for file in FeedFile.objects.all():
        file.file.delete()
        file.delete()
    return redirect(request.POST.get('next'))
