from re import T
from django.contrib import admin
from accounts.models import *
from safaris.models import *

# Register your models here.
admin.site.register(Tourist),
admin.site.register(Safaris),
admin.site.register(Tourguide),
admin.site.register(CustomUser)