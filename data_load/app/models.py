from django.db import models


class Department(models.Model):
    """Таблица Структурное подразделение"""
    name = models.CharField(verbose_name='Домашний адрес', max_length=400)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """Таблица Сотрудники"""
    first_name = models.CharField(verbose_name='Имя', max_length=250)
    last_name = models.CharField(verbose_name='Фамилия', max_length=250)
    middle_name = models.CharField(verbose_name='Отчество', max_length=250)
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    photo = models.ImageField(verbose_name='Фотография', upload_to='employee/')
    address = models.CharField(verbose_name='Домашний адрес', max_length=400)
    department = models.ForeignKey(
        Department,
        verbose_name='Отдел',
        on_delete=models.SET_NULL,
        null=True,
        related_name='employees'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
