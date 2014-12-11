from django.contrib import admin
from site_2015.models import(
    HomeImg,
    PageImg,
    Home,
    Page)


class HomeImgInline(admin.TabularInline):
    model = HomeImg
    extra = 1


class PageImgInline(admin.TabularInline):
    model = PageImg
    extra = 1

# Register your models here.


class HomeAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['title']
    # fields to filter the change list with
    save_on_top = True
    inlines = [HomeImgInline]

class PageAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['title']
    # fields to filter the change list with
    save_on_top = True
    # fields to search in change list
    search_fields = ['title', 'text']
    # enable the date drill down on change list
    date_hierarchy = 'pub_date'
    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("title",)}
    # Add multiple images
    inlines = [PageImgInline]


admin.site.register(Home, HomeAdmin)
admin.site.register(Page, PageAdmin)
