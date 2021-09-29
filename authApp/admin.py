from django.contrib import admin

from .models.account import Account
from .models.user import User

admin.site.register(User)
admin.site.register(Account)
