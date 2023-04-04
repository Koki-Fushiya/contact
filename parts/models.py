from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default='logo2.LPG', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Parts(models.Model):
    CATEGORY = (
        ('フリーザー', 'フリーザー'),
        ('ロボット', 'ロボット'),
        ('コンベア','コンベア')
    )
    name = models.CharField(max_length=200, null=True)
    quantity = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)

    class Meta:
        verbose_name_plural = "parts"

    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS = (
        ('-1個/セット', '-1個/セット'),
        ('在庫切れ', '在庫切れ'),
        ('在庫数正常','在庫数正常')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    parts = models.ForeignKey(Parts, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.parts.name



class Trouble(models.Model):
    MAIN_CATEGORY = (
    ('フリーザー', 'フリーザー'),
    ('ロボット', 'ロボット'),
    ('コンベア','コンベア'),
    ('その他','その他'),
    )
    SUB_CATEGORY = (
    ('インレット', 'インレット'),
    ('アウトレット', 'アウトレット'),
    ('ベルト', 'ベルト'),
    ('ロボット', 'ロボット'),
    ('コンベア','コンベア'),
    ('その他','その他'),
    )


    main_category = models.CharField(max_length=200, null=True, choices=MAIN_CATEGORY)
    sub_category = models.CharField(max_length=200, null=True, choices=SUB_CATEGORY)
    title = models.CharField(max_length=400, null=True)
    note = models.TextField(max_length=1500, null=True)
    trouble_pic = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "trouble"

    def __str__(self):
        return self.title



class Manual(models.Model):
    file = models.FileField(upload_to='')
    name = models.CharField(max_length=200, blank=True, null=True)
    upload_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name

    