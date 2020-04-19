from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import Snippet
from django.core.validators import RegexValidator


class NameWidget(forms.MultiWidget):

    def __init__(self, attrs=None):
        super().__init__([
            forms.TextInput(),
            forms.TextInput()
        ], attrs)

    def decompress(self, value):
        if value:
            return value.split(' ')
        return ['', '']

class NameField(forms.MultiValueField):

    widget = NameWidget

    def __init__(self, *args, **kwargs):

        fields = (
            forms.CharField(validators=[
                RegexValidator(r'[a-zA-Z]+', 'Enter a valid first name (only letters)')
            ]),
            forms.CharField(validators=[
                RegexValidator(r'[a-zA-Z]+', 'Enter a valid second name (only letters)')
            ])
        )

        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        return f'{data_list[0]} {data_list[1]}'


class ContactForm(forms.Form):
    name = NameField()
    date = forms.DateField(widget=forms.SelectDateWidget())
    report = forms.ChoiceField(choices=[ ("Daily", "Daily"), 
    ("Weekly", "Weekly"), 
    ("Monthly", "Monthly")])
    lead= forms.ChoiceField(choices=[  ("Raktima Mitra", "Raktima Mitra"), 
    ("Akanksha", "Akanksha"), 
    ("Amitesh Ranjan", "Amitesh Ranjan"), 
    ("Sheetal Kanika", "Sheetal Kanika"), 
    ("Ajeet", "Ajeet"), 
    ("Shekhar", "Shekhar")])
    hours = forms.IntegerField()
    body= forms.CharField(widget=forms.Textarea)
    progfile = forms.FileField(required=False)
    concern = forms.CharField(widget=forms.Textarea)
    next_plan = forms.CharField(required=False,widget=forms.Textarea)
    planfile = forms.FileField(required=False) 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'name',
            'date',
            'report',
            'lead',
            'hours',
            'body',
            'progfile',
            'concern',
            'next_plan',
            'planfile',
            Submit('submit', 'Submit', css_class='btn-success')
        )


class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('name','body')
