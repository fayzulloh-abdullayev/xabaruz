from django.contrib import admin
from .models import News,Category,Contact
# Register your models here.
admin.site.register(Category)
# admin.site.register(News)


@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display=('title','slug','state','created_date','update',)
    search_fields=('title',)
    list_display_links=('slug','title','update',)
    list_filter=('title','state',)
    prepopulated_fields = {'slug': ('title',),}
    short_description = 'title'


class AdminContact(admin.ModelAdmin):
    pass
admin.site.register(Contact,AdminContact)