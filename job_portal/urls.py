from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from teachers import views as teacher_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', teacher_views.home, name='home'),  # Home page view
    
    path('users/', include('users.urls')), # User authentication URLs

    path('teachers/', teacher_views.teacher_list, name='teacher_list'),  # List of teachers
    path('teachers/create/', teacher_views.create_teacher_profile, name='teacher_profile_create'),  # Create teacher profile
    #path('students/', include('students.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

