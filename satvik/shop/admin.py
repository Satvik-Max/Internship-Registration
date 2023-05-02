from django.contrib import admin
from .models import internship

@admin.register(internship)
class internshipAdmin(admin.ModelAdmin):
    list_display = ('name' , 'college' , 'Email' ,'Subject')
