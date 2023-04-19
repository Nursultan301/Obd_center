from django.contrib import admin

from category.models import Category, Discount, CategoryInfo


class CategoryInfoInline(admin.TabularInline):
    model = CategoryInfo
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    inlines = [CategoryInfoInline]


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    pass


