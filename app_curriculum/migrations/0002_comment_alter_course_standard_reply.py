# Generated by Django 4.0.6 on 2022-07-27 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_curriculum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_name', models.CharField(blank=True, max_length=100)),
                ('body', models.TextField(max_length=500)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('lesson_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app_curriculum.lesson')),
            ],
            options={
                'ordering': ['date_added'],
            },
        ),
        migrations.AlterField(
            model_name='course',
            name='standard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='app_curriculum.standard'),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_body', models.TextField(max_length=400)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comm_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='app_curriculum.comment')),
            ],
        ),
    ]
