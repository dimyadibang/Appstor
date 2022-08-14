from django.urls import path, include

from . import views

from Setoran.viewset_api import *
from rest_framework import routers




router = routers.DefaultRouter()
router.register('ustadz', UstadzViewSet)
router.register('mahasantri', MahasantriViewSet)
router.register('kitab', KitabViewSet)
router.register('setoran', SetoranViewSet)

router.register('users', UserViewSet)
router.register('groups', GroupViewSet)

#router.register('ustadzphoto', UstadzPhotoViewSet)
#router.register('list-users', ListUsers)




urlpatterns = [
    # login dll


    path('api/', include(router.urls)),
  #  path('api/list-users/',ListUsers.as_view),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', CustomAuthToken.as_view()),

    path('', views.home, name='home'),
    path('ustadz/', views.ustad, name='ustad'),
    path('ustadz/<str:pk>', views.ustadz, name='ustadz'),
    path('update_ustadz/<str:pk>', views.updateUstad, name='update_ustadz'),
    path('delete_ustadz/<str:pk>', views.deleteUstad, name='delete_ustadz'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutPage, name='logout'),
    path('user/', views.userPage, name='user-page'),
    path('account/', views.accountSetting, name='account-page'),
    path('create_mahasntri/', views.createMahasantri, name='create_mahasntri'),
    path('mahasantri/', views.mahasantri, name='mahasantri'),
    path('update_mahasantri/<str:pk>', views.updateMahasantri, name='update_mahasantri'),
    path('delete_mahasantri/<str:pk>', views.deleteMahasantri, name='delete_mahasantri'),
    path('mahasantri/<str:pk>', views.mhsantri, name='mhsantri'),
    path('kitab/', views.add_kitab_to_setoran, name='add-kitab-to-setoran'),
    path('delete_setoran/<str:pk>', views.deleteSetoran, name='delete_setoran'),
    # path('kitab/<int:pk>', views.add_to_setoran,name='add-to-cart'),
    # path('kitab/setorkan', views.check_mychecklist, name='check_mychecklist'),

]