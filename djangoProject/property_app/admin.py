from django.contrib import admin

from property_app.models import Property,Tenant,Unit,Lease

admin.site.register(Property)
admin.site.register(Tenant)
admin.site.register(Unit)
admin.site.register(Lease)
#
