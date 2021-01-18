from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from . models import Updext,Creatnote

class Usreg(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control",
		"placeholder":"Enter Password",
		}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control",
		"placeholder":"Enter Confirm Password",
		}))
	class Meta:
		model = User
		fields = ["username"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Username",
			}),
		}

class Uppfle(ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class": "form-control",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update Firstname",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update Lastname",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Update Emailid",
			}),
		}

class NeFld(ModelForm):
	class Meta:
		model = Updext
		fields = ["age","gender","im"]
		widgets ={
		"age":forms.NumberInput(attrs={
			"class":"form-control",
			}),
		"gender":forms.Select(attrs={
			"class":"form-control",
			}),
		}



class Cn(ModelForm):
	class Meta:
		model= Creatnote
		fields=["title","date","description","fl"]
		widgets={
		"title":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"title"
			}),
		"date":forms.DateInput(attrs={
			"class":"form-control",
			"type":"date",
			}),
		"description":forms.Textarea(attrs={
			"class":"form-control",
			"placeholder":"enter description",
			"rows":5,"col":10,
			}),
		}

class Un(ModelForm):
	class Meta:
		model= Creatnote
		fields=["title","date","description","fl"]
		widgets={
		"title":forms.TextInput(attrs={
			"class":"form-control",
			"readonly":True,
			}),
		"date":forms.DateInput(attrs={
			"class":"form-control",
			"type":"date",
			}),
		"description":forms.Textarea(attrs={
			"class":"form-control",
			"rows":5,"col":10,
			}),
		}