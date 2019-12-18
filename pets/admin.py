from pets.models import Pet
from django.contrib import admin


class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'birthday', 'owner')
    list_filter = ('type', 'owner')
    search_fields = ('name',)
    empty_value_display = '-empty-'


admin.site.register(Pet, PetAdmin)
