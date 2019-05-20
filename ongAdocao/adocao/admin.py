from django.contrib import admin
from .models import Pessoa, Animal, Adocao

admin.site.register(Pessoa)
admin.site.register(Animal)
admin.site.register(Adocao)
