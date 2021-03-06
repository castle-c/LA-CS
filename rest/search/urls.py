from rest_framework import routers
from django.conf.urls import url, include
from search import views



router = routers.DefaultRouter()
router.register(r'info', views.CompanyInfoList)
router.register(r'parishes', views.ParishList)
router.register(r'companies', views.CompaniesByParishList)
router.register(r'users', views.UserList)

urlpatterns = [
    url(r'^login$', views.login_user, name='login'),
      url(r'^register$', views.register_user, name='register'),
    url(r'^', include(router.urls)),
]
