from django.urls import path, include

from . import views

from Setoran.viewset_api import *
from rest_framework import routers




router = routers.DefaultRouter()
router.register('ustadz', UstadzViewSet)
router.register('mahasantri', MahasantriViewSet)
router.register('kitab', KitabViewSet)
#router.register('setoran', SetoranViewSet)

router.register('users', UserViewSet)
router.register('groups', GroupViewSet)

#router.register('postsetoran', PostSetoranViewSet)
#router.register('list-users', ListUsers)





urlpatterns = [
    # login dll


    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', CustomAuthToken.as_view()),

    path('api/setoran_create/',setoran_create_view),
    path('api/setoran_list/',setoran_list_view),
    path('api/setoran_list/<int:pk>/',setoran_list_detail_view),
    path('api/setoran_list/<int:pk>/update/',setoran_detail_update),
    path('api/setoran_list/<int:pk>/delete/',setoran_detail_delete),

    path('api/setoran_date/', ListSetoran.as_view()),
    path('api/setoran_date/<int:filter>/', ListSetoranMSantri),

    path('api/setoran_lima/', ListLimaSetoran.as_view()),

    path('api/setoran_day/',SetoranNowDay),

    path('api/kitab_add/<int:pk>/',KitabAddListAPIView),

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