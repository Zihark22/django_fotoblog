from django import forms

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=63, label='Nom d’utilisateur')
#     password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')


from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    username = forms.CharField(label='Utilisateur', min_length=5, max_length=150, error_messages={'required': 'Entrez votre nom d\'utilisateur (entre 5 et 150 charactères)'})  
    password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput, min_length=5, max_length=150)
    password2 = forms.CharField(label="Confirmation du mot de passe", widget=forms.PasswordInput, min_length=5, max_length=150)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'role')
    
    def clean(self):
        cleaned_data = super().clean()
        username = self.cleaned_data['username'].lower()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Les mots de passe ne correspondent pas.")
        for char in username:
            if char in "@é'\"&(-è\\çà[\{\}])+*/.!:;,§/.?µ£#{[|^@]}ễ³²¡÷×¿¬ß®©»«âÂåø€Êç±þæýðûÛîÎôÔ¶¹<>" :
                self.add_error('username', "Caractère(s) indésiré(s).")
                self.add_error('username', "Seul les lettres de l'alphabet sans accents et le _ sont autorisés ainsi que des chiffres !")
                break
        return cleaned_data


from . import validators

class PostCodeForm(forms.Form):
    post_code = forms.CharField(max_length=10, validators=[validators.PostCodeValidator])


from django import forms
from . import models

class UploadProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('profile_photo', )