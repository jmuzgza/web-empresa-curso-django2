from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')  #categories__name nos daría error tb... no es llamable
    ordering = ('author','published') # dejar con una coma si solo hay un criterio
    search_fields = ('title','author__username', 'categories__name') #si buscamos por author directamente habría problema... 
    date_hierarchy = 'published'   # para buscar por fechas de ese campo
    list_filter = ('author__username','categories__name')

    def post_categories(self, obj):   #truco para mostrar las categorías de otra clase
        return (", ").join([c.name for c in obj.categories.all().order_by("name")]) 
    
    post_categories.short_description= "Categorías" # para no mostrar post_categories

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

