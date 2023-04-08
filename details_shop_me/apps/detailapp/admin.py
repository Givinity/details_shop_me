from django.contrib import admin

from .models import Details, Category


class DetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create', 'published_or_not')  # для отображения по нажатию
    list_display_links = ('id', 'name') # кликабельные ид и имя
    # list_filter = ('cat')  # фильтр
    search_fields = ('name',)  # поиск по имени
    list_editable = ('published_or_not',) # снять/повесить публикацию
    prepopulated_fields = {'slug': ('name',)} # автозаполнение slug'a


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') # для отображения по нажатию
    list_display_links = ('id', 'name') # кликабельные ид и имя
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Details, DetailsAdmin)
admin.site.register(Category, CategoryAdmin)
