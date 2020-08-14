from django.contrib import admin
from .models import whitelist
from .models import blacklist
from .models import whitelist_stat

# Register your models here.
admin.site.register(whitelist)
admin.site.register(blacklist)
admin.site.register(whitelist_stat)
