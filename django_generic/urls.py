from django.contrib import admin
from django.urls import path, include
from app import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', views.ModelNameListView.as_view(), name='model_name_list'),
    path('detail/<str:pk>', views.ModelNameDetailView.as_view(),
         name='model_name_detail'),
    path('create', views.ModelNameCreateView.as_view(), name='model_name_create'),
    path('update/<str:pk>', views.ModelNameUpdateView.as_view(),
         name='model_name_update'),
    path('delete/<str:pk>', views.ModelNameDeleteView.as_view(),
         name='model_name_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
