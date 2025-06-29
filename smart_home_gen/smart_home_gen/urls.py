from django.urls import path, include

urlpatterns = [
    # Delegate all URLs to the generator app
    path('', include('generator.urls')),
]
