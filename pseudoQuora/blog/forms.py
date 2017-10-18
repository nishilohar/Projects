from django import forms


class QuestionForm(forms.Form):
	question = forms.CharField(required = True, max_length = 100, help_text = "100 Characters Max")
	name = forms.CharField(required = False, max_length = 50)

class LoginForm(forms.Form):
	username = forms.CharField(max_length = 15, required = True)
	password = forms.CharField(required = True)

class ContactForm(forms.Form):
	name = forms.CharField(max_length = 30, required = True)
	email = forms.EmailField()
	subject = forms.CharField(max_length = 30, required = True)
	message = forms.CharField(required = True, widget=forms.Textarea)
