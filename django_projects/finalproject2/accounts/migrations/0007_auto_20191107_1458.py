# Generated by Django 2.0 on 2019-11-07 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0006_auto_20191107_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='mysub',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.mysub'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='images',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
