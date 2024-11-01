from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator, RegexValidator
from decimal import Decimal
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    salary = models.IntegerField(validators=[
            MinValueValidator(1)
        ],verbose_name='Наименование')

class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    phone_number = models.CharField(max_length=11, verbose_name='Номер телефона')
    email = models.EmailField(max_length=150, verbose_name='Электронная почта', unique=True)
    passport = models.CharField(max_length=10, verbose_name='Паспорт', unique=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    login = models.CharField(max_length=20, verbose_name='Логин', unique=True)
    password = models.CharField(max_length=20,verbose_name='Пароль')
    role_id = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Id роли')


class CargoCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    coefficient = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Коэфициент перевозки')
    comments = models.CharField(max_length=500, verbose_name='Комментарии', null=True, blank=True)

class Warehouse(models.Model):
    address = models.CharField(max_length=200, verbose_name='Адрес')
    region = models.CharField(max_length=200, verbose_name='Регион')

class Car(models.Model):
    vin = models.CharField(max_length=17, verbose_name='VIN', unique=True)
    state_number = models.CharField(max_length=9, verbose_name='Гос.номер')
    stamp = models.CharField(max_length=200, verbose_name='Марка')
    model = models.CharField(max_length=200, verbose_name='Модель')
    status = models.CharField(max_length=200, verbose_name='Статус')
    driver_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Id водителя')

class PointIssue(models.Model):
    address = models.CharField(max_length=200, verbose_name='Адрес')
    warehouse_id = models.ForeignKey('Warehouse', on_delete=models.SET_NULL,null=True, verbose_name='Id склада')


class Package(models.Model):
    client_id = models.ForeignKey(
        'User',
        on_delete=models.SET_NULL,
        related_name='Reservations_as_client',
        verbose_name='Клиент',
        limit_choices_to={'post__name': "Клиент"},
        null=True,
    )
    comments = models.CharField(max_length=500, verbose_name='Комментарии', null=True, blank=True)
    sending_address = models.ForeignKey(
        'PointIssue',
        on_delete=models.SET_NULL,
        related_name='Reservations_as_sending_address',
        verbose_name='Адрес отправки',
        null=True,
    )
    delivery_address =models.ForeignKey(
        'PointIssue',
        on_delete=models.SET_NULL,
        related_name='Reservations_as_delivery_address',null=True,
        verbose_name='Адрес доставки',
    )
    weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Вес')
    date_of_receipt = models.DateField(verbose_name='Дата принятия')
    delivery_date = models.DateField(verbose_name='Дата доставки в пункт выдачи')
    date_of_issue = models.DateField(verbose_name='Дата выдачи')
    length = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='длина')
    height = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='высота')
    width = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='ширина')
    employee_id = models.ForeignKey(
        'User',
        on_delete=models.SET_NULL,
        related_name='Reservations_as_employee',
        verbose_name='Сотрудник',
        limit_choices_to={'post__name': "Сотрудник"},
        null=True
    )
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость доставки')
    cargo_category = models.ForeignKey('CargoCategory', on_delete=models.SET_NULL, null=True,
                                         verbose_name='Категория груза')
    status = models.CharField(max_length=200, verbose_name='Статус')
    car_id = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True, blank=True,
                                       verbose_name='Номер Машины')
