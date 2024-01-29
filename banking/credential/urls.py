from django.urls import path
from  . import views


urlpatterns = [
        path('register',views.register,name='register'),
        path('login',views.login,name='login'),
        path('logout',views.logout,name='logout'),
        path('formPage', views.formPage, name='formPage'),
        path('ajax_handler/<int:id>',views.ajax_handler,name="ajax_handler")
        # path('get-branches/',views.get_branches,name='get_branches'),
]
