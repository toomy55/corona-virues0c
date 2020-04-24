from django.contrib import admin

from mysite.core.models import Country ,City,daily,avrage,manths,week

# Register your models here.

admin.site.register(Country)
admin.site.register(City)
admin.site.register(daily)
admin.site.register(avrage)

admin.site.register(manths)

admin.site.register(week)




