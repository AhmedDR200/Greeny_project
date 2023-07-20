from django.contrib import admin
from .models import Product , ProducstImages , Brand , Category , ProductReview
# Register your models here.



class ProductImageTabular(admin.TabularInline):
    model = ProducstImages




class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageTabular]
    list_display = ['name','flag','quantity','price']
    list_filter = ['flag','brand','category']
    search_fields = ['name','desc','subtitle']




admin.site.register(Product ,ProductAdmin)
admin.site.register(ProducstImages)
admin.site.register(ProductReview)
admin.site.register(Brand)
admin.site.register(Category)