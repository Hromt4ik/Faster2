# Generated by Django 4.1.4 on 2023-11-28 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navigate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='delivery_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Reservations_as_delivery_address', to='navigate.pointissue', verbose_name='Адрес доставки'),
        ),
        migrations.AddField(
            model_name='package',
            name='employee_id',
            field=models.ForeignKey(limit_choices_to={'user__employee': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Reservations_as_employee', to='navigate.user', verbose_name='Сотрудник'),
        ),
        migrations.AlterField(
            model_name='package',
            name='cargo_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='navigate.cargocategory', verbose_name='Категория груза'),
        ),
        migrations.AlterField(
            model_name='package',
            name='client_id',
            field=models.ForeignKey(limit_choices_to={'user__client': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Reservations_as_client', to='navigate.user', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='package',
            name='sending_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Reservations_as_sending_address', to='navigate.pointissue', verbose_name='Адрес отправки'),
        ),
        migrations.AlterField(
            model_name='pointissue',
            name='warehouse_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='navigate.warehouse', verbose_name='Id склада'),
        ),
    ]
