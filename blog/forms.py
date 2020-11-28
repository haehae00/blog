from django import forms
from .models import Posting
from ckeditor_uploader.widgets import CKEditorUploadingWidget

REVIEW_POINT_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)
class Create(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ['title', 'body', 'grade']

        widgets = {
                    'title': forms.TextInput(
                        attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
                    ),

                    'body': forms.CharField(widget=CKEditorUploadingWidget()),

                    'grade':  forms.Select(choices=REVIEW_POINT_CHOICES),

                }


