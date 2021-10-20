# Generated by Django 3.1.3 on 2021-09-23 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0009_auto_20210922_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stage_Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('account_type', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('cin', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('sectors', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('stage', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('product_name', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('old_rating', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('new_rating', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('rating_3', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('rating_4', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('rating_5', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('rating_6', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('rating_7', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_1', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_2', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_3', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_4', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_5', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_6', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_7', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_8', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_9', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_10', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_11', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_12', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_13', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_14', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_15', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('criteria', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('cooling_period_1', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('cooling_period_2', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('cooling_period_3', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('cooling_period_4', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('cooling_period_5', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('rbi_window', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('mgmt_overlay_1', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('mgmt_overlay_2', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('file_identifier', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('edited_on', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('account_no', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.accountmaster')),
                ('edited_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stage_Initial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('account_no_temp', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('old_rating', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('new_rating', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('rating_3', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('rating_4', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('rating_5', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('rating_6', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('rating_7', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_1', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_2', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_3', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_4', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_5', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_6', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_7', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_8', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_9', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_10', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_11', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_12', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_13', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_14', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_15', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('criteria', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('cooling_period_1', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('cooling_period_2', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('cooling_period_3', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('cooling_period_4', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('cooling_period_5', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('rbi_window', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('mgmt_overlay_1', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('mgmt_overlay_2', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('file_identifier', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('edited_on', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('account_no', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.accountmaster')),
                ('edited_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stage_Final',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('old_rating', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('new_rating', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('rating_3', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('rating_4', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('rating_5', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('rating_6', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('rating_7', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_1', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_2', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_3', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_4', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_5', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_6', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_7', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_8', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_9', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_10', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_11', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_12', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_13', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_14', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('day_bucket_15', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('criteria', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('cooling_period_1', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('cooling_period_2', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('cooling_period_3', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('cooling_period_4', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('cooling_period_5', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('rbi_window', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('mgmt_overlay_1', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('mgmt_overlay_2', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('edited_on', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('account_no', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.accountmaster')),
                ('edited_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
