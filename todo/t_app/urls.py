from django.urls import path
from t_app import views


#TODO делал дз с другом,точнне обратлся к нему за помошью он помог с машрутами и с HTML
urlpatterns = [
    path('', views.osnova, name='osnova'),
    path('store/<int:store_id>/', views.infoKategory, name='infoKategory'),
    path('store/<int:store_id>/add_category/', views.add_cat, name='add_cat'),
    path('store/<int:store_id>/category/<int:category_id>/edit/', views.change_cat_page, name='change_cat_page'),
    path('store/<int:store_id>/category/<int:category_id>/update/', views.change_cat, name='change_cat'),
    path('store/<int:store_id>/category/<int:category_id>/delete/', views.del_cat, name='del_cat'),
    path('store/<int:store_id>/category/<int:category_id>/products/', views.product_list, name='product_list'),
    path('store/<int:store_id>/category/<int:category_id>/add_product/', views.add_product, name='add_product'),
    path('product/<int:product_id>/edit/', views.product_update, name='product_update'),
    path('product/<int:product_id>/delete/', views.product_delete, name='product_delete'),
]