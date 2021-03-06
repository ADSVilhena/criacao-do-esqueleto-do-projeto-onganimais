from django.contrib import admin
from .models import Pessoa, Animal, Adocao



class AnimalAdmin(admin.ModelAdmin):
    list_display = ['nomeAnimal','sexo', 'especie', 'porte']
    #list_display = ['nomeAnimal','get_sexo_display', 'get_especie_display', 'get_porte_display','map_sexo', 'map_porte']
    search_fields = ['nomeAnimal']
   

class AdocaoAdmin(admin.ModelAdmin):
    list_display = ['animal','pessoa','funcionario','data_adocao']


admin.site.register(Animal, AnimalAdmin)
admin.site.register(Pessoa)
admin.site.register(Adocao, AdocaoAdmin)


admin.site.site_header = "Administração da OngAdoção"
