from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
import re
from .models import Subjects

class RegisterFormAjaxKey(forms.Form):
    username = forms.CharField(required=False)
    password1 = forms.CharField(required=False)
    password2 = forms.CharField(required=False)
    
    method = forms.CharField(required=False)

    def clean(self):
        cred = super().clean()

        if cred.get("username"):
            if re.findall("[ -/-:-@-[-^-{-⁓]",cred.get("username")):
                self.add_error("username", "L'username può solo contenere lettere e numeri")
        elif cred.get("method") == "submit":
            self.add_error("username", "Compilare il campo")
        
        user_db = User.objects.filter(username = cred.get("username"))
        if user_db.exists():
            self.add_error("username", "Nome utente già esistente")

        if cred.get("password1"):
            if re.findall("[ -/-:-@-[-^-{-⁓]", cred.get("password1")):
                self.add_error("password1","La password può solo contenere lettere e numeri")
        elif cred.get("method") == "submit":
            self.add_error("password1", "Compilare il campo")  
        
        if cred.get("password2"):
            if re.findall("[ -/-:-@-[-^-{-⁓]",cred.get("password2")):
                self.add_error("password2","La password può solo contenere lettere e numeri")
            
            elif not cred.get("password1") == cred.get("password2") and cred.get("password1"):
                self.add_error("password2","Password non inserita correttamente")
        elif cred.get("method") == "submit":
            self.add_error("password2", "Compilare il campo") 

class LoginFormAjaxKey(forms.Form):
    username = forms.CharField(required=False)
    password = forms.CharField(required=False)
    
    method = forms.CharField(required=False)

    def clean(self):
        cred = super().clean()

        if cred.get("username"):
            if re.findall("[ -/-:-@-[-^-{-⁓]",cred.get("username")):
                self.add_error("username", "L'username può solo contenere lettere e numeri")
        elif cred.get("method") == "submit":
            self.add_error("username", "Compilare il campo")

        if cred.get("password"):
            if re.findall("[ -/-:-@-[-^-{-⁓]", cred.get("password")):
                self.add_error("password","La password può solo contenere lettere e numeri")
        elif cred.get("method") == "submit":
            self.add_error("password", "Compilare il campo") 
       
class AddSubject(ModelForm):
    subject_name = forms.CharField(required=False)
    class Meta:
        model = Subjects
        fields = ["subject_name"]
    def clean(self):
        cred = super().clean()
        subject = cred.get("subject_name")

        if not subject:
            self.add_error("subject_name", "Compilare il campo")
    