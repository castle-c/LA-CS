from django.contrib import admin
from .models import Parish, CompanyInfo, CompaniesByParish

admin.site.register(Parish)
admin.site.register(CompanyInfo)
admin.site.register(CompaniesByParish)
