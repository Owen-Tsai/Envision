from django.shortcuts              import       render
from django.http                   import       JsonResponse
from django.views.generic          import       View
from django_filters                import       rest_framework
from django.contrib.auth.hashers   import       hashlib
from django_filters.rest_framework import       DjangoFilterBackend
#----------------------------------------------------------------------------------------
from rest_framework                import       filters
from rest_framework.views          import       APIView
from rest_framework.response       import       Response
from rest_framework.decorators     import       api_view
from rest_framework                import       permissions,viewsets,renderers,generics,status,exceptions
#-----------------------------------------------------------------------------------------
import random
#导入序列化器
from .serializers import ArticleSerializer,ArticleCommentSerializer,ArticleCommentReplySerializer,AnnouncementSerializer
from .serializers import SectionSerializer,PostSerializer,PostCommentSerializer,PostCommentReplySerializer,UserSerializer
from .serializers import PostCommentReplySerializer,DirectAnswerSerializer,DirectAnswerAnswerSerializer,GroupSerializer
from .serializers import GroupActivitySerializer,GroupAnnouncementSerializer,LearningTaskSerializer,UserRegisterSerializer
from .serializers import UserLoginSerializer,ChangePasswordSerializer,ForgetPasswordSerializer,ResetPasswordSerializer,UserAccountSerializer

#导入模型
from .models import Article,ArticleComment,ArticleCommentReply,Announcement,Section,Post,PostComment,PostCommentReply
from .models import Group,GroupActivity,GroupAnnouncement,DirectAnswer,DirectAnswerAnswer,User,UserAccount,UserToken
from .models import LearningTask

#导入过滤器

class ArticleViewSet(viewsets.ModelViewSet):
    queryset          =   Article.objects.all()
    serializer_class  =   ArticleSerializer
    filter_backends   =   (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filter_fields     =   ('author_id',)
    ordering_fields   =   ('create_time',)
    search_fields     =   ('^tag',)



class ArticleCommentViewSet(viewsets.ModelViewSet):
    queryset          =   ArticleComment.objects.all()
    serializer_class  =   ArticleCommentSerializer
    filter_backends   =   (DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields     =   ('article_id','author_id',)
    ordering_fields   =   ('create_time',)


class ArticleCommentReplyViewSet(viewsets.ModelViewSet):
    queryset          =   ArticleCommentReply.objects.all()
    serializer_class  =   ArticleCommentReplySerializer
    filter_backends   =   (DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields     =   ('article_id','comment_id','author_id',)
    ordering_fields   =   ('create_time',)


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset          =   Announcement.objects.all()
    serializer_class  =   AnnouncementSerializer
    filter_backends   =   (filters.OrderingFilter,)
    ordering_fields   =   ('create_time',)


class SectionViewSet(viewsets.ModelViewSet):
    queryset          =   Section.objects.all()
    serializer_class  =   SectionSerializer


class PostVieweSet(viewsets.ModelViewSet):
    queryset          =   Post.objects.all()
    serializer_class  =   PostSerializer
    filter_backends   =   (DjangoFilterBackend,filters.OrderingFilter,)   
    filter_fields     =   ('author_id','section_id',)
    ordering_fields   =   ('create_time',)


class PostCommentViewSet(viewsets.ModelViewSet):
    queryset          =   PostComment.objects.all()
    serializer_class  =   PostCommentSerializer
    filter_backends   =   (DjangoFilterBackend,filters.OrderingFilter,)  
    filter_fields     =   ('author_id','post_id',)
    ordering_fields   =   ('create_time',)


class PostCommentReplyViewSet(viewsets.ModelViewSet):
    queryset          =   PostCommentReply.objects.all()
    serializer_class  =   PostCommentReplySerializer
    filter_backends   =   (DjangoFilterBackend,filters.OrderingFilter,)   
    filter_fields     =   ('comment_id','post_id','author_id',)
    ordering_fields   =   ('create_time',)


class DirectAnswerViewSet(viewsets.ModelViewSet):
    queryset          =   DirectAnswer.objects.all()
    serializer_class  =   DirectAnswerSerializer
    filter_backends   =   (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter,)   
    filter_fields     =   ('author_id',)
    ordering_fields   =   ('create_time',)
    search_fields     =   ('^tag',)


class DirectAnswerAnswerViewSet(viewsets.ModelViewSet):
    queryset          =   DirectAnswerAnswer.objects.all()
    serializer_class  =   DirectAnswerAnswerSerializer
    filter_backends   =   (DjangoFilterBackend,filters.OrderingFilter,)   
    filter_fields     =   ('direct_answer_id','author_id')
    ordering_fields   =   ('create_time',)


class GroupViewSet(viewsets.ModelViewSet):
    queryset          =   Group.objects.all()
    serializer_class  =   GroupSerializer
    filter_backends   =   (filters.SearchFilter,)
    search_fields     =   ('group_name',)   



class GroupActivityViewSet(viewsets.ModelViewSet):
    queryset          =   GroupActivity.objects.all()
    serializer_class  =   GroupActivitySerializer
    filter_backends   =   (DjangoFilterBackend,filters.OrderingFilter,)   
    filter_fields     =   ('group_id',)
    ordering_fields   =   ('start_time',)


class GroupAnnouncementViewSet(viewsets.ModelViewSet):
    queryset          =   GroupAnnouncement.objects.all()
    serializer_class  =   GroupAnnouncementSerializer
    filter_backends   =   (DjangoFilterBackend,filters.OrderingFilter,)   
    filter_fields     =   ('group_id',)
    ordering_fields   =   ('create_time',)


class LearningTaskViewSet(viewsets.ModelViewSet):
    queryset          =   LearningTask.objects.all()
    serializer_class  =   LearningTaskSerializer
    filter_backends   =   (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter,)   
    filter_fields     =   ('author_id',)
    ordering_fields   =   ('start_time',)
    search_fields     =   ('tag',)


class UserViewSet(viewsets.ModelViewSet):
    queryset          =   User.objects.all()
    serializer_class  =   UserSerializer


class UserAccountViewSet(viewsets.ModelViewSet):
    queryset          =   UserAccount.objects.all()
    serializer_class  =   UserAccountSerializer


class UserRegisterAPIView(APIView):
    queryset          =   User.objects.all()
    serializer_class  =   UserRegisterSerializer

    # 重载GET方法
    def get(self,request,format=None):
        serializer    =   UserRegisterSerializer()
        return Response(serializer.data)

    #重载POST方法
    def post(self,request,format=None):
        data          =   request.data
        if User.objects.filter(e_mail=data.get('e_mail')):
            return Response('该邮箱已被注册',status=status.HTTP_400_BAD_REQUEST)
        elif data.get('password') != data.get('confirm_password'):
            return Response('两次输入密码不一致',status=status.HTTP_400_BAD_REQUEST)
        serializer    =   UserRegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            context   =   {'msg':'Succeeded'}
            return JsonResponse(context)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    #---------------登录成功时为用户设置Token,返回并保存---------------
    queryset          =   User.objects.all()
    serializer_class  =   UserLoginSerializer

    #重载GET方法
    def get(self,request,format=None):
        serializer    =   UserLoginSerializer()
        return Response(serializer.data)

    #重载POST方法
    def post(self,request,format=None):
        data          =   request.data
        try:
            if User.objects.get(e_mail=data.get('email_or_username')):
                user = User.objects.get(e_mail=data.get('email_or_username'))
            else:
                user = User.objects.get(username=data.get('email_or_username'))
            for i in range(2):
                password = hashlib.md5(data.get('password').encode('utf-8') + user.salt.encode('utf-8')).hexdigest()
            if password  == user.password:
                random_list = 'abdjcniejknmdkjdj'
                for i in range(10):
                    ch += (list(random_list)[random.randint(0,16)])
                token = hashlib.md5(user.e_mail.encode('utf-8') + ch.encode('utf-8')).hexdigest()
                UserToken.objects.update_or_create(user=user,defaults={'token':token})
                context = {'msg':'Succeeded','Token':token}
                return JsonResponse(context)
            return Response({'msg':'ERROR Incorrect username or password'},status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'msg':'The user does not exist'},status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordAPIView(APIView):
    #---------------An endpoint for changing password.-------------
    queryset          =   User.objects.all()
    serializer_class  =   ChangePasswordSerializer

    #获取请求对象
    def get_object(self,queryset=None):
        return self.request.user

    #重载GET方法
    def get(self,request,format=None):
        serializer    =   ChangePasswordSerializer()
        return Response(serializer.data)

    #重载POST方法
    def post(self,request,*args,**kwargs):
        self.object   =   self.get_object()
        serializer    =   ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({'msg':'Old password error'},status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            return Response({'msg':'Successful password modification'},status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



        
