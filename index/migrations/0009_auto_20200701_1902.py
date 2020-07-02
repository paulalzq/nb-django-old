# Generated by Django 3.0.7 on 2020-07-02 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_servicio_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='portafolio',
            name='link',
            field=models.CharField(default='link_solucion', max_length=50),
        ),
        migrations.AlterField(
            model_name='portafolio',
            name='image',
            field=models.ImageField(default='none', upload_to='portafolio'),
        ),
    ]
