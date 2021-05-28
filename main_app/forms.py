from django.forms import ModelForm
from .models import Craft

class CraftForm(ModelForm):
    class Meta:
        model = Craft
        exclude = ['url', 'user', 'badges', 'black', 'color']

