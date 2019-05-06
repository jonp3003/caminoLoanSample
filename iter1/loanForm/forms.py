from django import forms
from loanForm.models import Product
from loanForm.models import BTYPE

class ProductForm(forms.ModelForm):

    name   = forms.CharField(widget=forms.TextInput
             (attrs={"placeholder": "Your Name"}))

    amount   = forms.DecimalField(widget=forms.TextInput
            (attrs={"placeholder": "Loan Amount Requested"}))

    years    = forms.IntegerField(widget=forms.TextInput
             (attrs={"placeholder": "# of Years in Business"}))

    type      = forms.ChoiceField(label='Business Type',
                choices=BTYPE, required=True,)



    class Meta:
        model = Product
        fields = [
            'name',
            'amount',
            'type',
            'years'
        ]
