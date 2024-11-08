from django.forms import ModelForm, Textarea
from .models import Review

# from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
#
# class ReviewForm(UserCreationForm) :
#     def __init__(self, *args, **kwargs) :
#         super(ModelForm, self).__init__(*args, **kwargs)
#         for fieldname in['username','password1','password2']:
#             self.fields[fieldname].help_text=None
#             self.fields[fieldname].widget.attrs.update({'class': 'form-control'})
#
#             self.fields['text'].widget.attrs.update({'class':'form-control'})
#             self.fields['watchAgain'].widget.attrs.update({'class':'form-check-input'})
#
# class ReviewForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super(ModelForm, self).__init__(*args, **kwargs)
#         for fieldname in ['username', 'password1', 'password2']:
#             self.fields[fieldname].help_text = None
#             self.fields[fieldname].widget.attrs.update({'class': 'form-control'})

class ReviewForm(ModelForm) :
    def __init__(self, *args, **kwargs) :
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class':'form-control'})
        self.fields['watchAgain'].widget.attrs.update({'class':'form-check-input'})

    class Meta:
        model = Review
        fields = ['text', 'watchAgain']
        labels = {
            'text':('说说你看过之后的感受吧...'),
            'watchAgain':('是否会再次观看'),
        }
        widgets = {
            'text':Textarea(attrs={'rows':4}),
        }