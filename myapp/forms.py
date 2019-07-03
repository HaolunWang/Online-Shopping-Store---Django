from django import forms
from myapp.models import Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
VALUE_CHOICES = ( ('Yes', 1), ('No', 0) )
class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['client','product','num_units']
        widgets = {
            'client': forms.RadioSelect

        }
        labels = {
            "num_units": "Quantity",
            "client":"Client Name"
        }

class InterestForm(forms.Form):
      your_name = forms.CharField(label='Your name', max_length=100)
      interested=forms.ChoiceField(widget=forms.RadioSelect,choices=VALUE_CHOICES)
      quantity=forms.IntegerField(initial=1)
      comment = forms.CharField(widget=forms.Textarea,required=False)

class NewUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    # def save(self, commit=True):
    #     user = super(NewUserForm, self).save(commit=False)
    #     user.email = self.cleaned_data["email"]
    #     if commit:
    #         user.save()
    #     return user