from django.contrib import admin

# Register your models here.
# registers models into Django admin it also implements default users

# import SignUp
from .models import SignUp

# this will add the Signups section on the admin page
class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model = SignUp

admin.site.register(SignUp, SignUpAdmin)
