from django.urls import path
from . import views


urlpatterns = [
    # URLs for RETRIEVE data.
    path('productDetails/<str:subCategory>/', views.productDetails),
    path('categories/', views.categories),
    # path('category/<str:>', views.category),
    path('cart/', views.cart),
    path('addtoCart/', views.addtoCart),
    path('updateCartQty/<str:id>/<str:scope>/', views.updateCartQty),
    path('deleteCartItem/<str:id>/', views.deleteCartItem),   
    path('orderSummary/', views.cart),
    path('subCategory/<str:category>/', views.subCategory),   
     

]