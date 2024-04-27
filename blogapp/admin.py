from django.contrib import admin
from .models import postdetails
from .models import signupdetails
from .models import contactdetails
# Register your models here.
admin.site.register(postdetails)
admin.site.register(signupdetails)
admin.site.register(contactdetails)
