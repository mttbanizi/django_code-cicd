from django.urls import path, include

urlpatterns = [
    path('blog/', include(('devops.blog.urls', 'blog'))),
    path('users/', include(('devops.users.urls', 'users'))),
    path('auth/', include(('devops.authentication.urls', 'auth'))),
]
