from django.contrib import admin
from .models import Flat, Complaint, Owner


class UtensilsInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner', 'flat']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['owner', 'address', 'town']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'floor']
    raw_id_fields = ['liked_by']
    inlines = [
        UtensilsInline,
    ]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']
    inlines = [
        UtensilsInline,
    ]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
