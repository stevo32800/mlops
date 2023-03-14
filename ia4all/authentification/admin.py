from django.contrib import admin
from authentification.models import Utilisateur
# Register your models here.

class colonnesTableUtilisateur(admin.ModelAdmin):
    list_display = [field.name for field in Utilisateur._meta.fields]


admin.site.register(Utilisateur,colonnesTableUtilisateur)