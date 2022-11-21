from django import forms

from ggg.models import Entryggg

class EntrygggForm(forms.ModelForm):

    class Meta:
        model = Entryggg
        fields = ('player', 'season', 'seasonround', 'tournamentweek', 'gameone', 'gametwo', 'gamethree', 'gamefour', 'gamefive',)
        GAME_CHOICES = (
            ('', 'Pick a game'),
            ('1', 'Argentina v Saudi Arabia'),
            ('2', 'Mexico v Poland'),
            ('3', 'Denmark v Tunisia'),
            ('4', 'France v Australia')
        )




