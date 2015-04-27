from django.contrib import admin


from .models import Source, TeaType, Tea, Batch, Flavor, Bottle

admin.site.register(Source)
admin.site.register(TeaType)
admin.site.register(Tea)
admin.site.register(Batch)
admin.site.register(Flavor)
admin.site.register(Bottle)
