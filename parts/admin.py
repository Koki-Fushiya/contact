from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Parts)
admin.site.register(Tag)
admin.site.register(Order)
admin.site.register(Trouble)
admin.site.register(Manual)
