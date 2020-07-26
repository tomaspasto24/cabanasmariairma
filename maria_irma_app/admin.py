from django.contrib import admin
from maria_irma_app.models import cabana, plano

# Register your models here.

class cabana_ADMIN(admin.ModelAdmin):
    fields = ("ubicacion", "texto", "fecha", "image_main", "image_1", "image_2", "image_3", "image_4", "image_5")
    list_display=("ubicacion", "fecha", "slug")
    date_hierarchy="fecha"

class plano_ADMIN(admin.ModelAdmin):
    fields = ("ubicacion", "texto", "image_main", "image_1", "image_2", "image_3", "image_4", "image_5")
    list_display=("ubicacion", "slug")

admin.site.register(cabana, cabana_ADMIN),
admin.site.register(plano, plano_ADMIN)
