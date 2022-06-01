from django import forms
from .models import Item


class ItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('user', 'name', 'scheduled_at', 'status')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['readonly'] = True


class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('user', 'name', 'scheduled_at', 'status')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['readonly'] = True
