from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("core/", include("core.urls")),
    path('hoodie1/', include("core.urls")),
    path('hoodie2/', include("core.urls")),
    path('hoodie3/', include("core.urls")),
    path('hoodie4/', include("core.urls"))

]