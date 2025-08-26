from django.shortcuts import get_object_or_404, render, redirect
from birthday.forms import BirthdayForm
from birthday.utils import calculate_birthday_countdown
from birthday.models import Birthday
from django.core.paginator import Paginator


def birthday(request, pk=None):
    instance = get_object_or_404(Birthday, pk=pk) if pk is not None else None
    form = BirthdayForm(
        request.POST or None,
        files=request.FILES or None,
        instance=instance,
    )

    context = {
        'form': form,
        'mode': 'edit' if pk else 'create',
    }

    if request.method == 'POST' and form.is_valid():
        obj = form.save()
        context['birthday_countdown'] = calculate_birthday_countdown(
            obj.birthday)

    return render(request, 'birthday/birthday.html', context)


def birthday_list(request):
    birthdays = Birthday.objects.order_by('id')
    paginator = Paginator(birthdays, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'birthday/birthday_list.html', context)


def delete_birthday(request, pk):
    instance = get_object_or_404(Birthday, pk=pk)
    if request.method == 'POST':
        instance.delete()
        return redirect('birthday:list')

    form = BirthdayForm(instance=instance)
    return render(request, 'birthday/birthday.html', {
        'form': form,
        'mode': 'delete'})
