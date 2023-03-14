from django import forms

class CSVForm(forms.Form):
    csv_file = forms.FileField()

class TargetColumnForm(forms.Form):
    target_column = forms.CharField(max_length=100)