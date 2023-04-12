from django.urls import path, include

urlpatterns = [
    path('blog/', include(('devops.blog.urls', 'blog')))
]
