from django import forms	
from boards.models import Question, Choice, Comentario

class PollForm(forms.ModelForm):

	#choice_list = forms.ModelChoiceField(Choice.objects.all())
	class Meta:
		model = Question

		fields = [
		 'question_text',
		 'image'

		]

		labels = { 'question_text': 'Pregunta', 'image':'Seleccione una imágen (No obligatorio)'}
		widgets = {
			'question_text': forms.TextInput(attrs={'class':'form-control'}),
		}




class ChoiceForm(forms.ModelForm):

	class Meta:
		model = Choice

		fields = [
		 'choice_text',

		]

		labels = { 'choice_text': 'Opción (No obligatorio)'}
		widgets = {
			'choice_text': forms.TextInput(attrs={'class':'form-control'}),
		}


class ComentarioForm(forms.ModelForm):
	class Meta:
		model = Comentario

		fields = [
		 'comentario',

		]
		labels = { 'comentario': 'Escribe tu comentario'}
		widgets = {
            'comentario': forms.Textarea(attrs={'cols': 80, 'rows': 4 ,'class':'form-control'}),
		}

