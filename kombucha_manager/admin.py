from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *

class UserProfileInline(admin.StackedInline):
	model = UserProfile

class UserAdmin(UserAdmin):
	inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Source)
admin.site.register(TeaType)
admin.site.register(Tea)
admin.site.register(Batch)
admin.site.register(Flavor)
admin.site.register(Bottle)
admin.site.register(Vessel)
admin.site.register(Organization)
admin.site.register(UserProfile)