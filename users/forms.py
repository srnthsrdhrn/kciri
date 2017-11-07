from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from entry.models import DataEntry
from users.models import User, Employee


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'account_type']

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit("submit", "Submit"))


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['username', 'password', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(EmployeeCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit("submit", "Submit"))
