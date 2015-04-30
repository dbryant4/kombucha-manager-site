from django.contrib import admin


from .models import *

admin.site.register(Source)
admin.site.register(TeaType)
admin.site.register(Tea)
admin.site.register(Batch)
admin.site.register(Flavor)
admin.site.register(Bottle)
admin.site.register(Vessel)
admin.site.register(Organization)
admin.site.register(UserProfile)