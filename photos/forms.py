from django import forms

from .models import Photo, Feed, FeedFile



class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('file', )


# Upload NFT Collection Folder Form
class FeedModelForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ['directories']
        widgets = {
            'directories': forms.TextInput(attrs={
                    'id': "directories", 'hidden': '',
                }),
        }


class FileModelForm(forms.ModelForm):
    class Meta:
        model = FeedFile
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={
                'type': "file", 'name': 'files[]', 'multiple': '', 'directory': '', 'webkitdirectory': '',
                'mozdirectory': '', 'id': "actual-btn",
                'style': 'width: 0.1px; height: 0.1px; opacity: 0; overflow: hidden; position: absolute; z-index: -1;',
                'onchange': 'selectFolder(event)',
            }),
        }
