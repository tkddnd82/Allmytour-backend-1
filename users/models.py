from django.db import models

class User(models.Model):
    name         = models.CharField(max_length=100)
    email        = models.EmailField()
    password     = models.CharField(max_length=300,null=True)
    phone_number = models.CharField(max_length=45)
    is_active    = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'users'

class UserTemp(models.Model):
    email      = models.EmailField()
    password   = models.CharField(max_length=300,null=True)
    code       = models.CharField(max_length=30)
    expired_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'user_temp'

class PhoneCheck(models.Model):
    phone_number = models.CharField(max_length=45)
    auth_number  = models.IntegerField()
    expired_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'phone_checks'
