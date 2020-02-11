from django.contrib import admin
from blog.models import Posts,Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Posts, PostAdmin)
admin.site.register(Category, CategoryAdmin)
