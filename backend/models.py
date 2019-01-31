from django.db import models
from django.contrib.auth.hashers import hashlib
import random
# Create your models here.


class User(models.Model):
    uid                =   models.AutoField(primary_key=True)
    username           =   models.CharField(max_length=45)
    e_mail             =   models.CharField(max_length=45)
    password           =   models.CharField(max_length=200)
    salt               =   models.CharField(max_length=45,blank=True, null=True)
    real_name          =   models.CharField(max_length=45,blank=True,null=True)
    user_logo          =   models.CharField(max_length=45,blank=True, null=True)
    user_description   =   models.CharField(max_length=200,blank=True, null=True)
    major              =   models.CharField(max_length=45,blank=True,null=True)     #专业
    e_class            =   models.CharField(max_length=45,blank=True,null=True)     #行政班级
    dept               =   models.CharField(max_length=45,blank=True,null=True)     #协会部门
    identity           =   models.CharField(max_length=45,blank=True,null=True)     #身份
    #加盐腌制密码并保存
    def save(self,*args,**kwargs):
        ch = 'fhuendhsgjlsmlmnvjjsljlsmn'
        for i in range(10):
            self.salt += (list(ch)[random.randint(0,25)])
        for i in range(2):
            self.password = hashlib.md5(self.password.encode('utf-8')+self.salt.encode('utf-8')).hexdigest()
        super(User,self).save(*args,**kwargs)
    class Meta:
        db_table = 'user'  


class UserAccount(models.Model):
    uid                =   models.IntegerField(primary_key=True)
    user_rank          =   models.IntegerField(blank=True,null=True)
    user_score         =   models.IntegerField(blank=True,null=True)
    class Meta:
        db_table = 'useraccount'


class UserToken(models.Model):
    owner              =   models.OneToOneField(User,on_delete=models.CASCADE)
    token              =   models.CharField(max_length=64)
    class Meta:
        db_table = 'user_token'


class Announcement(models.Model):
    announcement_id    =   models.AutoField(primary_key=True)
    author_id          =   models.IntegerField(blank=True,null=True)
    create_time        =   models.DateTimeField(blank=True,null=True)
    topic              =   models.CharField(max_length=45)
    content            =   models.TextField(blank=True,null=True)
    class Meta:
        db_table = 'announcement'


class Article(models.Model):
    article_id         =   models.AutoField(primary_key=True)
    author_id          =   models.IntegerField()
    create_time        =   models.DateTimeField(blank=True,null=True)
    tag                =   models.CharField(max_length=90,blank=True,null=True)
    topic              =   models.CharField(max_length=200)
    content            =   models.TextField(blank=True,null=True)
    class Meta:
        db_table = 'article'


class ArticleComment(models.Model):
    comment_id         =   models.AutoField(primary_key=True)
    article_id         =   models.IntegerField()
    author_id          =   models.IntegerField()
    create_time        =   models.DateTimeField()
    content            =   models.TextField()
    class Meta:
        db_table = 'article_comment'


class ArticleCommentReply(models.Model):
    comment_reply_id   =   models.AutoField(primary_key=True)
    article_id         =   models.IntegerField()
    comment_id         =   models.IntegerField()
    author_id          =   models.IntegerField()
    create_time        =   models.DateTimeField()
    content            =   models.TextField()
    class Meta:
        db_table = 'article_comment_reply'


class Section(models.Model):
    section_id         =   models.AutoField(primary_key=True)
    create_time        =   models.DateTimeField()
    theme              =   models.CharField(max_length=45,blank=True,null=True)
    description        =   models.TextField(blank=True,null=True)
    class Meta:
        db_table = 'section'


class Post(models.Model):
    post_id            =   models.AutoField(primary_key=True)
    author_id          =   models.IntegerField(blank=True,null=True)
    section_id         =   models.IntegerField(blank=True,null=True)
    create_time        =   models.DateTimeField()
    topic              =   models.CharField(max_length=200)
    content            =   models.TextField(blank=True,null=True)
    class Meta:
        db_table = 'post'

    
class PostComment(models.Model):
    comment_id         =   models.AutoField(primary_key=True)
    author_id          =   models.IntegerField()
    post_id            =   models.IntegerField()
    create_time        =   models.DateTimeField()
    content            =   models.TextField()
    class Meta:
        db_table = 'post_comment'


class PostCommentReply(models.Model):
    comment_reply_id   =   models.AutoField(primary_key=True)
    comment_id         =   models.IntegerField()
    post_id            =   models.IntegerField()
    author_id          =   models.IntegerField()
    create_time        =   models.DateTimeField()
    content            =   models.TextField()
    class Meta:
        db_table = 'post_comment_reply'


class DirectAnswer(models.Model):
    direct_answer_id   =   models.AutoField(primary_key=True)
    author_id          =   models.IntegerField()
    create_time        =   models.DateTimeField()
    tag                =   models.CharField(max_length=90,blank=True,null=True)
    question           =   models.CharField(max_length=200,blank=True,null=True)
    description        =   models.TextField(blank=True,null=True)
    invited_person_id  =   models.CharField(max_length=90,blank=True,null=True)
    class Meta:
        db_table = 'direct_answer'


class DirectAnswerAnswer(models.Model):
    answer_id          =   models.AutoField(primary_key=True)
    direct_answer_id   =   models.IntegerField()
    author_id          =   models.IntegerField()
    create_time        =   models.DateTimeField()
    content            =   models.TextField()
    class Meta:
        db_table = 'direct_answer_answer'


class Group(models.Model):
    group_id           =   models.AutoField(primary_key=True)
    group_name         =   models.CharField(max_length=45)
    group_admin_id     =   models.CharField(max_length=200)
    description        =   models.TextField(blank=True,null=True)
    create_time        =   models.DateTimeField()
    group_member_id    =   models.CharField(max_length=200,blank=True,null=True)
    class Meta:
        db_table = 'group'


class GroupAnnouncement(models.Model):
    announcement_id    =   models.AutoField(primary_key=True)
    group_id           =   models.IntegerField()
    create_time        =   models.DateTimeField()
    topic              =   models.CharField(max_length=90,blank=True,null=True)
    content            =   models.TextField(blank=True,null=True)
    class Meta:
        db_table = 'group_bulletin'


class GroupActivity(models.Model):
    group_activity_id  =   models.AutoField(primary_key=True)
    group_id           =   models.IntegerField()
    start_time         =   models.DateTimeField(blank=True,null=True)
    end_time           =   models.DateTimeField(blank=True,null=True)
    topic              =   models.CharField(max_length=90)
    content            =   models.TextField(blank=True,null=True)
    activity_admin_id  =   models.CharField(max_length=45,blank=True,null=True)
    class Meta:
        db_table = 'group_activity'


#----------------------群组学习任务、学习资料等-----------
#-------------------------------------------------------

class LearningTask(models.Model):
    task_id            =   models.AutoField(primary_key=True)
    author_id          =   models.IntegerField()
    start_time         =   models.DateField()
    end_time           =   models.DateTimeField(blank=True,null=True)
    tag                =   models.CharField(max_length=45,blank=True,null=True)
    topic              =   models.CharField(max_length=45,blank=True,null=True)
    content            =   models.TextField(blank=True,null=True)
    is_supervise       =   models.IntegerField(blank=True,null=True)
    is_end             =   models.IntegerField(blank=True,null=True)
    class Meta:
        db_table = 'learning_task'




