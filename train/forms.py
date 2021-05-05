from django import forms

from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('tracking_code',)

    tickets_number = forms.IntegerField()

    def clean_tickets_number(self):
        tickets_number = self.cleaned_data['tickets_number']
        if tickets_number <= 0:
            raise forms.ValidationError('Tickets number must be a positive number!')
        return tickets_number
