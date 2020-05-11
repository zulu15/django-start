from django import forms	
from boards.models import Question, Choice

class PollForm(forms.ModelForm):

	#choice_list = forms.ModelChoiceField(Choice.objects.all())
	class Meta:
		model = Question

		fields = [
		 'question_text',
		 #'choice_list'

		]

		labels = { 'question_text': 'Pregunta'}
		widgets = {
			'question_text': forms.TextInput(attrs={'class':'form-control'}),
		}




class ChoiceForm(forms.ModelForm):

	class Meta:
		model = Choice

		fields = [
		 'choice_text',

		]

		labels = { 'choice_text': 'Opción'}
		widgets = {
			'choice_text': forms.TextInput(attrs={'class':'form-control'}),
		}

