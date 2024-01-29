from django.contrib import admin
from . models import District,Branches,City,Country,Account_type,Materials,Gender,Form_data

# Register your models here.
admin.site.register(District)
admin.site.register(Branches)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Account_type)
admin.site.register(Materials)
admin.site.register(Gender)

class FormAdmin(admin.ModelAdmin):
    list_display = ['firstname','birthday','age','account_type','district','gender','materials']
admin.site.register(Form_data,FormAdmin)
