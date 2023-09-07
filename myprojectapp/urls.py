
from django.conf import settings
from django.contrib import admin
from django.urls import path
from myprojectapp import views
from django.conf.urls.static import static

app_name = "app"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tambahtugas/', views.tambahtugas, name="tambah_tugas"),
    path('makanan/', views.makanan, name="makanan"),
    path('task/', views.task, name='task'),
    path('task-update/<int:pk>/', views.task_update, name='task_update'),
    path('task-delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('peralatan/', views.tool, name='tool'),
    path('tambahtool/', views.tambah_tool, name='tambah_tool'),
    path('tool-update/<int:pk>/', views.tool_update, name='tool_update'),
    path('tool-delete/<int:pk>/', views.tool_delete, name='tool_delete'),
]
