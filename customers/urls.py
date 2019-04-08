from django.urls import path,include
from customers import views


urlpatterns = [
    path('customers/',views.customer_list,name='customer_list'),
    path('customers/<int:pk>/',views.customer_detail,name='customer_detail'),
    path('customers/age/<int:age>/',views.customer_list_age,name='customer_list_age'),
]
