"""jewelshops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shopapp import views
from django.template.loader import get_template
from shopapp.views import home,signin,signup
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('signin/',views.signin),
    path('signup/',views.signup),
    path('<slug:owner>/owner/',views.owner),
    path('<slug:customer>/customer/',views.customer),
    path('logout/', views.signout),
    path('necklase/<str:jewelname>/', views.necklase),
    path('ring/<str:jewelname>/', views.ring),
    path('bracelet/<str:jewelname>/', views.bracelet),
    path('buy/<int:jewel_id>/', views.buy),
    
    path('addjewel/',views.addjewel),
    path('deletejewel/<int:jewel_id>/',views.deletejewel),
    path('checkout/<int:jewel_id>/',views.totalcheck),
    path('jewel_list/<str:owner>/',views.jewel_list),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
