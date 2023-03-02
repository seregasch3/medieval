# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Citizens(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    income = models.IntegerField(blank=True, null=True)
    senior_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citizens'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Feodals(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    income = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feodals'


class MedievalCitizens(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    status = models.ForeignKey('MedievalStatus', models.DO_NOTHING)
    income = models.CharField(max_length=30)
    senior_id = models.ForeignKey('MedievalSeniors', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'medieval_citizens'


class MedievalEntry(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.TextField()
    date_added = models.DateTimeField()
    topic = models.ForeignKey('MedievalTopic', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'medieval_entry'


class MedievalFeodals(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    status = models.ForeignKey('MedievalStatus', models.DO_NOTHING)
    income = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'medieval_feodals'


class MedievalSeniors(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    status = models.ForeignKey('MedievalStatus', models.DO_NOTHING)
    income = models.CharField(max_length=30)
    feodal_id = models.ForeignKey(MedievalFeodals, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'medieval_seniors'


class MedievalStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'medieval_status'


class MedievalTopic(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'medieval_topic'


class Seniors(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    income = models.IntegerField(blank=True, null=True)
    feodal_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seniors'


class Status(models.Model):
    status_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'status'
