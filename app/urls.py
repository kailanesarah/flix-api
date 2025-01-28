from django.contrib import admin
from django.urls import path
from genres.views import genre_list_creat, genre_update_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', genre_list_creat, name="genre_list_creat"),
    path('genres/<int:pk>/', genre_update_delete, name ="genre_update_delete")
]
