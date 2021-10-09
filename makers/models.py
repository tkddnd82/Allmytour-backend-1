from django.db import models

class Maker(models.Model):
    user           = models.ForeignKey('users.User', on_delete = models.CASCADE)
    name           = models.CharField(max_length = 50)
    nickname       = models.CharField(max_length = 100)
    description    = models.TextField()
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    instagram      = models.CharField(max_length=200,null=True)
    facebook       = models.CharField(max_length=200,null=True)
    youtube        = models.CharField(max_length=200,null=True)
    option         = models.ManyToManyField('Option', through='MakerOption', related_name='makers')
    
    class Meta:
        db_table = 'makers'

class MakerOption(models.Model):
    maker       = models.ForeignKey('Maker', on_delete=models.CASCADE)
    option      = models.ForeignKey('Option', on_delete=models.CASCADE, null= True)
     
    class Meta:
        db_table = 'maker_options'

class Option(models.Model):
    upper_code  = models.CharField(max_length=50)
    option_name = models.CharField(max_length=100)
    used        = models.CharField(max_length=10)

    class Meta:
        db_table = 'options'

class ImageFile(models.Model):
    maker = models.ForeignKey('Maker', on_delete=models.CASCADE)
<<<<<<< HEAD
<<<<<<< HEAD
    image = models.ImageField(upload_to='image', blank=True, null=True, default='camera.png')
=======
    image = models.ImageField(upload_to='image', blank=True, null=True)
>>>>>>> 4b0e389 (Add: 모델링)
=======
    image = models.ImageField(upload_to='image', blank=True, null=True, default='camera.png')
>>>>>>> df7a403 (Add:makers5)

    class Meta:
        db_table = 'image_files'

