from django.db import models
from django.templatetags.static import static
from birthday.validators import real_age


class Birthday(models.Model):
    first_name = models.CharField(
        'Имя',
        max_length=20,
        help_text='Обязательное поле'
    )
    last_name = models.CharField(
        'Фамилия',
        blank=True,
        max_length=20,
        help_text='Необязательное поле'
    )
    birthday = models.DateField(
        'Дата рождения',
        validators=[real_age],
        help_text='Обязательное поле'
    )
    image = models.ImageField(
        'Фото',
        blank=True,
        upload_to='birthdays_images',
        default='birthdays_images/deffault_user.webp'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['first_name', 'last_name', 'birthday'],
                name='unique person constraint'
            )
        ]
