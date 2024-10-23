#in admin site super user is allow to add property, tenant, unit and lease. and he or she can change credentails of any user.
from django.contrib import admin

from property_app.models import Property,Tenant,Unit,Lease

admin.site.register(Property)
admin.site.register(Tenant)
admin.site.register(Unit)
admin.site.register(Lease)
#
