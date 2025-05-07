from django.urls import path
from portfolio import views
urlpatterns = [
    path('', views.customer_list),
    path('api/customers/', views.customer_list),
    path('api/mycustomers/', views.my_customer_list),
    path('api/customers/<int:pk>', views.getCustomer),
    path('api/investments/', views.investment_list),
    path('api/investments/<int:pk>', views.getInvestment),
    path('api/stocks/', views.stock_list),
    path('api/stocks/<int:pk>', views.getStock),
]
