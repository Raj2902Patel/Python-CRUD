
from django.urls import path
from myapp import views



urlpatterns = [
    path('',views.index,name='index'),
    path('add',views.insertdata,name='add'),
    path('show',views.show,name='show'),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.destroy),

]