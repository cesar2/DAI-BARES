from django import forms
from django.contrib.auth.models import User
from rango.models import Bar, Tapa, UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website',)
		
class BarForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="Por favor introduce el nombre del bar.")
	address = forms.CharField(max_length=128, help_text="Escribe la direccion del bar")
	visits = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
	class Meta:
        # Provide an association between the ModelForm and a model
		model = Bar
		fields = ('name', 'address')

class TapaForm(forms.ModelForm):
	name2 = forms.CharField(max_length=128, help_text="Por favor, introduce el nombre de la tapa.")
	votos = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	url = forms.URLField(max_length=500, help_text="Introduce url de la imagen")

	class Meta:
        # Provide an association between the ModelForm and a model
		model = Tapa

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
		exclude = ('bar',)
        #or specify the fields to include (i.e. not include the category field)
		fields = ('name2','url','votos')
