# Generated by Django 2.0.1 on 2018-01-28 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('email_sender', '0002_emailsender_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emails_receive', models.TextField()),
                ('text', models.TextField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('email_sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='email_sender.EmailSender')),
            ],
        ),
    ]