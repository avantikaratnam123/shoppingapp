from django.contrib import admin
from .models import(Customer,Product,Cart,Orderplaced)

# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discounted_price','description','brand','category']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display =['id','user','product']

@admin.register(Orderplaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_diaplay =['id','user','customer','product','quantity','ordered_date','status']

