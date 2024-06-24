from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.core.exceptions import ValidationError
from .models import *

class DepositForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['amount']  # Specify which field(s) to include in the form


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    country = CountryField().formfield()
    telephone_number = forms.CharField(max_length=15)  # Example field for telephone number

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "password1", "password2", "email", "first_name", "last_name", "country", "telephone_number")

class DepositForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['proposed_amount']

    def clean_proposed_amount(self):
        proposed_amount = self.cleaned_data['proposed_amount']
        if proposed_amount <= 0:
            raise forms.ValidationError("Proposed amount must be greater than zero.")
        return proposed_amount


class InvestmentForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['amount']  # Add other fields as needed
    
    def __init__(self, *args, **kwargs):
        self.user_profile = kwargs.pop('user_profile', None)
        super().__init__(*args, **kwargs)
    
    def clean_amount(self):
        invested_amount = self.cleaned_data['amount']
        
        if invested_amount <= 0:
            raise ValidationError("Investment amount must be greater than zero.")
        
        if invested_amount > self.user_profile.amount:
            raise ValidationError("Insufficient funds.")
        
        return invested_amount
    
    def save(self, commit=True):
        instance = super().save(commit=False)  # Call the original save method without committing to the database

        # Assuming self.user_profile is a related model or attribute that provides additional data
        invested_amount = self.cleaned_data['amount']

        instance.user = self.user_profile.user  # Assigning user from user_profile

        # Calculate profit based on the adjusted amount
        instance.profit = instance.calculate_profit()

        if commit:
            instance.save()  # Save the instance with the calculated profit

        return instance
