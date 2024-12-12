from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('page1',views.nike1),
    path('page2',views.register,name='signin'),
    path('page3',views.loginpage,name='login'),
    path('page4',views.logoutpage,name='logout'),
    path('page5/<int:id>',views.detail,name='detail'),
    path('page6/<int:id>',views.detail2,name='detail2'),
    path('page7/<int:id>',views.detail3,name='detail3'),
    path('page8',views.staff),
    path('page9',views.addproduct,name='addproduct'),
    path('page10',views.addproduct2,name='addproduct1'),
    path('page11',views.addproduct3,name='addproduct2'),
    
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)