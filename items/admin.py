from django.contrib import admin
from .models import Product,Category, Comments, Rating, Basket, Order
from myauth.models import Foundation, Company, Section, Destitute, Users,Cards
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discountprice', 'discountPercent','quantity','is_active','link', 'image','onsale', 'category', 'author')
    list_filter = ("onsale",)
    search_fields = ['title']

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_on', 'product', 'author')
    list_filter = ("product",)
    search_fields = ['product']

class RatingAdmin(admin.ModelAdmin):
    list_display = ('rate','product', 'author')
    list_filter = ("product",)
    search_fields = ['product']

class BasketAdmin(admin.ModelAdmin):
    list_display = ('product', 'author','amount')
    list_filter = ("product",)
    search_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ('orderDate', 'author')
    list_filter = ("author",)
    search_fields = ['author']

class CardsAdmin(admin.ModelAdmin):
    list_display = ('cardNumber','cvv','balance', 'validDate','author')
    

class FoundationAdmin(admin.ModelAdmin):
    list_display = ('name','description','phone', 'cardBalance', 'author')
    list_filter = ("name",)
    search_fields = ['name']

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('username','email','description','phone', 'cardBalance', 'address','author')
    list_filter = ("username",)
    search_fields = ['username']

class UsersAdmin(admin.ModelAdmin):
    list_display = ('name','phone', 'cardBalance', 'address','users')
    list_filter = ("name",)
    search_fields = ['name']

class SectionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

class DestituteAdmin(admin.ModelAdmin):
    list_display = ('name','description','phone', 'cardNumber','iin', 'address','image', 'section')
    list_filter = ("name",)
    search_fields = ['name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cards, CardsAdmin)
admin.site.register(Foundation, FoundationAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Destitute, DestituteAdmin)
admin.site.register(Users, UsersAdmin)

