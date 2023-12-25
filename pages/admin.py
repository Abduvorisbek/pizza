from django.contrib import admin
from pages.models import ScrollModel, CategoryModel, ProductModel, ReservationModel, GalleryModel


@admin.register(ScrollModel)
class ScrollModelAdmin(admin.ModelAdmin):
        list_display = ['id', 'title', 'description', 'created_at']
        search_fields = ['title', 'C']
        list_filter = ['created_at']

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
        list_filter = ['created_at', 'updated_at']
        search_fields = ['title']
        list_display = ['title', 'created_at', 'updated_at']

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
        list_filter = ['created_at', 'updated_at']
        search_fields = ['title', 'description']
        list_display = ['id', 'title', 'price', 'created_at', 'updated_at']

@admin.register(ReservationModel)
class ReservationModelAdmin(admin.ModelAdmin):
        list_filter = ['created_at', 'updated_at']
        search_fields = ['name', 'email']
        list_display = ['id', 'name', 'email', 'date', 'time', 'created_at']

@admin.register(GalleryModel)
class GalleryModelAdmin(admin.ModelAdmin):
        list_display = ['image']