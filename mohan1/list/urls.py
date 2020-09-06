from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.home),
    path('show',views.show),
    path('register',views.register1),
    path('order/<int:id>',views.order),
    path('product_add',views.product_add),
    path('login',views.login),
    path('logout', views.logout_page),
    path('save_order',views.save_details),
    path('show_categery/<int:id>',views.show_categery),
    path('categeries',views.categeries),

    #path('search_item',views.search_details),
    path('delete/<int:id>',views.delete),
    path('Pending/<int:id>',views.pending),
    path('show_orders',views.show_orders),
    path('Delivered/<int:id>', views.deliver),
    path('count_all',views.count_all),
]