"""envision URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from backend import views
from . import urls
from rest_framework.routers import DefaultRouter,url
from django.views.generic import TemplateView

router=DefaultRouter()
#-------------------------------文章----------------------------------
router.register(r'ArticleViewSet',views.ArticleViewSet)
router.register(r'ArticleCommentViewSe',views.ArticleCommentViewSet)
router.register(r'ArticleCommentReplyViewSet',views.ArticleCommentReplyViewSet)
#-------------------------------公告----------------------------------
router.register(r'AnnouncementViewSet',views.AnnouncementViewSet)
#-------------------------------帖子----------------------------------
router.register(r'SectionViewSet',views.SectionViewSet)
router.register(r'PostVieweSet',views.PostVieweSet)
router.register(r'PostCommentViewSet',views.PostCommentViewSet)
router.register(r'PostCommentReplyViewSet',views.PostCommentReplyViewSet)
#-------------------------------直答----------------------------------
router.register(r'DirectAnswerViewSet',views.DirectAnswerViewSet)
router.register(r'DirectAnswerAnswerViewSet',views.DirectAnswerAnswerViewSet)
#-------------------------------群组----------------------------------
router.register(r'GroupViewSet',views.GroupViewSet)
router.register(r'GroupActivityViewSet',views.GroupActivityViewSet)
router.register(r'GroupAnnouncementViewSet',views.GroupAnnouncementViewSet)
router.register(r'LearningTaskViewSet',views.LearningTaskViewSet)
#-------------------------------用户----------------------------------
router.register(r'UserViewSet',views.UserViewSet)
router.register(r'UserAccountViewSet',views.UserAccountViewSet)


urlpatterns = [
    url('^api/',include(router.urls)),
    path('admin/', admin.site.urls),
    path('register/',views.UserRegisterAPIView.as_view()),
    path('login/',views.UserLoginAPIView.as_view()),
    path('changepassword/',views.ChangePasswordAPIView.as_view()),

]
