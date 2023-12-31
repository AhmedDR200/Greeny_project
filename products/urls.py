from django.urls import path
from .views import ProductList , ProductDetail , BrandList , BrandDetail

app_name = 'products'


urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('brands/', BrandList.as_view(), name='brand_list'),
    path('brands/<int:pk>', BrandDetail.as_view(), name='brand_detail'),
    

]
