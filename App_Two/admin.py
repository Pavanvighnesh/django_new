from django.contrib import admin
from .models import Topic,Webpage,AccessRecord,user
from App_Two.models import user
# Register your models here.

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(user)
