from django.contrib.auth.forms import UserCreationForm
from django import forms
from .constants import  role_choices,GENDER_TYPE
from django.contrib.auth.models import User
from .models import UserAccount

class UserRegistrationForm(UserCreationForm):
    nid_no = forms.IntegerField(label='NID No')
    birth_date = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}))
    userRole = forms.ChoiceField(choices=role_choices)
    gender= forms.ChoiceField(choices=GENDER_TYPE)
    
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email','birth_date','userRole','gender','nid_no','password1', 'password2',]
        
        
    def save(self, commit=True):
        our_user = super().save(commit=False) 
        if commit == True:
            our_user.save() 
            UserAccount.objects.create(
                user = our_user,
                userRole=self.cleaned_data['userRole'],
                nid_no = self.cleaned_data['nid_no'],
                birth_date = self.cleaned_data['birth_date'],
                
            )
        return our_user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                
                'class' : (
                    'form-control bg-gray-200 text-gray-700' 
                    'border rounded py-3 px-4 mb-3' 
                    'leading-tight focus:outline-none focus:bg-white'
                ) 
            })

class UserUpdateForm(forms.ModelForm):
    nid_no = forms.IntegerField(label='NID No')
    birth_date = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.CharField(label='Gender', widget=forms.Select(choices=GENDER_TYPE))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'form-control bg-gray-200 text-gray-700'
                    'border rounded py-3 px-4 mb-3'
                    'leading-tight focus:outline-none focus:bg-white'
                )
            })

            if self.instance:
                try:
                    user_account = self.instance.account
                except UserAccount.DoesNotExist:
                    user_account = None

                if user_account:
                    self.fields['nid_no'].initial = user_account.nid_no
                    self.fields['gender'].initial = user_account.gender
                    self.fields['birth_date'].initial = user_account.birth_date

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_account, created = UserAccount.objects.get_or_create(user=user)
            user_account.nid_no = self.cleaned_data['nid_no']
            user_account.gender = self.cleaned_data['gender']
            user_account.birth_date = self.cleaned_data['birth_date']
            user_account.save()
        return user