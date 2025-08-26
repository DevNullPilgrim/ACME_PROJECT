from django import forms

from birthday.models import Birthday

BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d',
            ),

        }

    def clean_first_name(self):
        # Получаем значение имени из словаря очищенных данных.
        first_name = self.cleaned_data['first_name']
        # Разбиваем полученную строку по пробелам
        # и возвращаем только первое имя.
        return first_name.split()[0]

    def clean(self):
        super().clean()
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']

        if f'{first_name} {last_name}' in BEATLES:
            raise forms.ValidationError(
                'Этого участника группы The Beatles уже нет в живых!')
