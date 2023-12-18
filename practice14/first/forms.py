from django import forms

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
class Form(forms.Form):
	comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
	value = forms.DecimalField()
	agree = forms.BooleanField(initial=True)
	favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
	