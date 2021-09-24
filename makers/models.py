from django.db import models

class Maker(models.Model):
    user           = models.ForeignKey('users.User', on_delete = models.CASCADE)
    name           = models.CharField(max_length = 50)
    nickname       = models.CharField(max_length = 100)
    description    = models.TextField()
    create_at      = models.DateTimeField(auto_now_add=True)
    update_at      = models.DateTimeField(auto_now=True)
    instagram      = models.CharField(max_length=200,null=True)
    facebook       = models.CharField(max_length=200,null=True)
    youtube        = models.CharField(max_length=200,null=True)
    another_sns1   = models.CharField(max_length=200,null=True)
    another_sns2   = models.CharField(max_length=200,null=True)
    another_sns3   = models.CharField(max_length=200,null=True)
    option         = models.ManyToManyField('Option', through='MakerOption', related_name='makers')
    
    class Meta:
        db_table = 'makers'

class MakerOption(models.Model):
    maker  = models.ForeignKey('Maker', on_delete=models.CASCADE)
    option = models.ForeignKey('Option', on_delete=models.CASCADE)
    etc    = models.CharField(max_length=100, null=True)
     
    class Meta:
        db_table = 'maker_options'

class Option(models.Model):
    upper_code  = models.CharField(max_length=50)
    option_name = models.CharField(max_length=100)
    used        = models.CharField(max_length=10)

    class Meta:
        db_table = 'options'

class ImageFile(models.Model):
    maker          = models.ForeignKey('Maker', on_delete=models.CASCADE)
    profile_image  = models.ImageField(upload_to = 'profile_images/')
    id_card_image  = models.ImageField(upload_to = 'id_card_images/')
    license_image  = models.ImageField(upload_to = 'license_images/')

    class Meta:
        db_table = 'image_files'
