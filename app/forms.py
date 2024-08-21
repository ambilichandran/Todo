from django import forms
from  .models import Todo
from django .forms import TextInput
class Todolist(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['items']
        widgets={
            'items':TextInput(
                attrs={
                    "type":"text",
                    "class":"form-control",
                    "placeholder":"Enter your text here",
                    "aria-label":"Username",
                    "aria-describedby":"basic-addon1"
                }
            )
        }
