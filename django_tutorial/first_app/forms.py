from django import forms
from datetime import datetime


YEARS = [x for x in range(1940, 3000)]


class EmployeeForm(forms.Form):
    name = forms.CharField(label="Employee Name",
                           max_length=30,
                           widget=forms.TextInput(attrs={'style': 'color:red',
                                                         'placeholder': "Enter a name"
                                                         })
                           )
    birth_date = forms.DateField(label="Date Of Birth", widget=forms.SelectDateWidget(years=YEARS))
    salary = forms.IntegerField(label="Salary")
    address = forms.CharField(label="Address", max_length=500, widget=forms.Textarea(attrs={
        'style': 'color: red;',
        'placeholder': 'Enter Address with landmark'
    }
                                                                                     ))

    # date of birth should not be greater than today

    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']
        # step #1
        if birth_date is None:
            raise forms.ValidationError("birth date is mandatory", code="birth_date")

        # step #2 should be less than today date
        today = datetime.now().date()
        if birth_date > today:
            raise forms.ValidationError("Date of birth should less than or equal to today", code="birth_date")

        return birth_date



# Model form
from .models import Inventory


class InventoryModelForm(forms.ModelForm):
    # Fields
    class Meta:
        model = Inventory
        fields = ('item', 'item_code', 'item_condition', 'quantity')
        #exclude = ('quantity',)

    def clean_item_code(self):
        item_code = self.cleaned_data['item_code']
        if item_code <= 0:
            raise forms.ValidationError("Item code should be greater than zero.")

        return item_code

from .models import Contact


class ContactModelForm(forms.ModelForm):
    # fields
    class Meta:
        model = Contact
        fields = "__all__"


