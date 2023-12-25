from django import forms

from pages.models import ReservationModel


class ReservationForm(forms.ModelForm):
    class Meta:
        model = ReservationModel
        fields = ['name', 'email', 'phone', 'message', 'date', 'time']