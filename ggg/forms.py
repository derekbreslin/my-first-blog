from django import forms

from ggg.models import Entryggg

GAME_CHOICES = (
            ('', 'Pick a game'),
            (1, 'Cameroon v Serbia'),
            (2, 'Brazil v Switzerland'),
            (3, 'South Korea v Ghana'),
            (4, 'Portugal v Uruguay'),
            (5, 'Ecuador v Senegal'),
            (6, 'Netherlands v Qatar'),
            (7, 'Iran v USA'),
            (8, 'Wales v England')
)

class EntrygggForm(forms.ModelForm):

    gameone = forms.ChoiceField(
        widget=forms.Select,
        choices=GAME_CHOICES
    )    

    gametwo = forms.ChoiceField(
        widget=forms.Select,
        choices=GAME_CHOICES
    )    

    gamethree = forms.ChoiceField(
        widget=forms.Select,
        choices=GAME_CHOICES
    )    

    gamefour = forms.ChoiceField(
        widget=forms.Select,
        choices=GAME_CHOICES
    )    

    gamefive = forms.ChoiceField(
        widget=forms.Select,
        choices=GAME_CHOICES
    )    

    class Meta:
        model = Entryggg
        labels  = {
        'gameone': 'Game One', 
        'gametwo': 'Game Two'
        }
        fields = ('player', 'season', 'seasonround', 'tournamentweek', 'gameone', 'gametwo', 'gamethree', 'gamefour', 'gamefive',)
