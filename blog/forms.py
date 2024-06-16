# blog/forms.py
from django import forms
from .models import Post
import zipfile
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'video', 'file', 'is_paid_content', 'is_published', 'is_scheduled', 'scheduled_time']

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            if file.name.endswith('.zip'):
                try:
                    with zipfile.ZipFile(file) as zip_file:
                        if zip_file.testzip() is not None:
                            raise forms.ValidationError("Invalid zip file.")
                except zipfile.BadZipFile:
                    raise forms.ValidationError("Invalid zip file.")
        return file
