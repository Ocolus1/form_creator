from django import forms
from .models import Field, FormItem


class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ('name', 'types', 'ids', 'required')

        def __str__(self):
            return self._name


class FormItemForm(forms.ModelForm):
    field = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Field.objects.none(),
        label='Fields',
    )

    class Meta:
        model = FormItem
        fields = ('field', )

        def __str__(self):
            return self.form
        
    def __init__(self, *args, **kwargs):
        us = args[1] or None
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['field'].queryset = Field.objects.filter(user=us)
        self.fields['field'].error_messages = {'required': ''}
