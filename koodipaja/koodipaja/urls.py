"""koodipaja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from projects.views import ProjectViewSet, ProjectPageTitleViewSet, ProjectArticleViewSet

# testing stuff
from testaus.views import QuestionAnswerPairViewSet

router = DefaultRouter()
router.register(r'project', ProjectViewSet, basename='project')
router.register(r'project_title', ProjectPageTitleViewSet, basename='project_title')
router.register(r'project_article', ProjectArticleViewSet, basename='project_article')
router.register(r'question_answer', QuestionAnswerPairViewSet, basename='question_answer')

urlpatterns = [
    path('api/', include(router.urls)),

    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('kotisivu.urls')),
    path('', include('testaus.urls')),
    path('', include('projects.urls')),

    # path('api/', include('projects.urls')),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"),
         name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"),
         name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"),
         name='password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
