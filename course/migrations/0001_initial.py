# Generated by Django 2.0.6 on 2020-11-10 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
                ('contents', models.TextField()),
                ('page_views', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('level', models.IntegerField()),
                ('parent_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='cate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Category'),
        ),
    ]
