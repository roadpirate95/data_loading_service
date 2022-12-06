from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView
from django.views.generic.list import ListView
from app.models import Employee
from app.forms import PersonForm
from django.views.generic.base import View


class CreateEmployeeView(View):
    """Класс для создания объекта Employee"""

    def get(self, request, *args, **kwargs):
        form = PersonForm()
        return render(request, 'app/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app:create_employee')


class EmployeeListView(ListView):
    """Класс для просмотров всех объектов Employee"""
    model = Employee
    template_name = 'app/list.html'
    context_object_name = 'employees'
    paginate_by = 5


class EmployeeUpdateView(UpdateView):
    """Класс для обновления данных объекта Employee"""
    model = Employee
    template_name = 'app/edit.html'
    fields = ['first_name', 'last_name', 'address', 'department']
    success_url = reverse_lazy('app:list_employee')


class EmployeeDeleteView(DeleteView):
    """Класс для удаления объекта Employee"""
    model = Employee
    template_name = 'app/delete.html'
    success_url = reverse_lazy('app:list_employee')
    context_object_name = 'employee'


def home(request):
    """Главная страница"""
    return render(request, 'app/home.html', {})
