from django.urls import path
from crud import views

urlpatterns = [
    path('',views.add_show,name='addshow'),
    path('delete/<int:id>/',views.del_data, name='deletedata'),
    path('<int:id>',views.update_data, name='updatedata'),
]
