# Generated by Django 2.2.17 on 2021-01-13 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'verbose_name': 'disque'},
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'verbose_name': 'artiste'},
        ),
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'reservation'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'prospect'},
        ),
        migrations.AlterField(
            model_name='album',
            name='available',
            field=models.BooleanField(default=True, verbose_name='disponible'),
        ),
        migrations.AlterField(
            model_name='album',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='album',
            name='picture',
            field=models.ImageField(null=True, upload_to='cover/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='album',
            name='reference',
            field=models.IntegerField(null=True, verbose_name='Réference'),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=200, verbose_name='titre'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='contacted',
            field=models.BooleanField(default=False, verbose_name='demande traitée ?'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Date d'envoi"),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nom'),
        ),
    ]