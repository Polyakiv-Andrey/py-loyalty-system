# Generated by Django 4.1 on 2022-12-12 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LoyaltyProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('bonus_percentage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LoyaltyProgramParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_activity', models.DateField(auto_now=True)),
                ('active_bonuses', models.IntegerField(blank=True, default=0, null=True)),
                ('sum_of_spent_money', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.customer')),
                ('loyalty_program', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='db.loyaltyprogram')),
            ],
        ),
    ]
