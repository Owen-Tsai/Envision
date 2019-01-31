from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User,UserAccount,UserToken,Article,ArticleComment,ArticleCommentReply,Announcement,Group,GroupActivity
from .models import GroupAnnouncement,LearningTask,Section,Post,PostComment,PostCommentReply,DirectAnswer,DirectAnswerAnswer


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model   =  Article
        fields  =  ('article_id','author_id','create_time','tag','topic','content')


class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model   =  ArticleComment
        fields  =  ('comment_id','article_id','author_id','create_time','content')


class ArticleCommentReplySerializer(serializers.ModelSerializer):
    class Meta:
        model   =  ArticleCommentReply
        fields  =  ('comment_reply_id','article_id','comment_id','author_id','create_time','content')


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model   =  Announcement
        fields  =  ('announcement_id','author_id','create_time','topic','content')


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model   =  Section
        fields  =  ('section_id','create_time','theme','description')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model   =  Post
        fields  =  ('post_id','author_id','section_id','create_time','topic','content')


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model   =  PostComment
        fields  =  ('comment_id','author_id','post_id','create_time','content')


class PostCommentReplySerializer(serializers.ModelSerializer):
    class Meta:
        model   =  PostCommentReply
        fields  =  ('comment_reply_id','comment_id','post_id','author_id','create_time','content')


class DirectAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model   =  DirectAnswer
        fields  =  ('direct_answer_id','author_id','create_time','tag','question','description','invited_person_id')


class DirectAnswerAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model   =  DirectAnswerAnswer
        fields  =  ('answer_id','direct_answer_id','author_id','create_time','content')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model   =  Group
        fields  =  ('group_id','group_name','group_admin_id','description','create_time','group_member_id')


class GroupAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model   =  GroupActivity
        fields  =  ('announcement_id','group_id','create_time','topic','content')


class GroupActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model   =  GroupAnnouncement
        fields  =  ('group_activity_id','group_id','start_time','end_time','topic','content','activity_admin_id')


class LearningTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model   =  LearningTask
        fields  =  ('task_id','author_id','start_time','end_time','tag','topic','content','is_supervise','is_end')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model   =  User
        fields  =  ('uid','username','e_mail','real_name','user_logo','user_description','major','e_class','dept','identity')


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model   =  UserAccount
        fields  =  ('uid','user_rank','user_score')


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model   =  User
        fields  =  ('username','e_mail','password','confirm_password')


class UserLoginSerializer(serializers.ModelSerializer):
    email_or_username = serializers.CharField(max_length=90,allow_blank=False)
    class Meta:
        model   =  User
        fields  =  ('email_or_username','password')


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    def validata_new_password(self,value):
        validate_password(value)
        return value


class ForgetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model   =  User
        fields  =  ('e_mail')


class ResetPasswordSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model   =  User
        fields  =  ('e_mail','password','confirm_password')
