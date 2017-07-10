# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# # Author：Xuhong Wen
from django.db import models
# from django.contrib.auth.models import User
#
#
# #Create your models here.
# class Customer(models.Model):
#     '''客户信息表 -- qq、qq名、电话、渠道来源、转介绍人、咨询课程、咨询详情、标签、备注'''
#     #32个字节，10个汉字（3个字节一个汉字）;考虑是否唯一；可否为空；一般blank（Django专属）和null成对出现
#     name = models.CharField(max_length=32,blank=True,null=True)
#     #qq号字段作为唯一值
#     qq = models.CharField(max_length=64,unique=True)
#     qq_name = models.CharField(max_length=64,blank=True,null=True)
#     phone = models.CharField(max_length=64,blank=True,null=True)
#     source_choices=(('0','转介绍'),
#                     ('1','QQ群'),
#                     ('2','官网'),
#                     ('3','百度推广'),
#                     ('4','51CTO'),
#                     ('5','知乎'),
#                     ('6','市场推广')
#                     )
#     soure = models.SmallIntegerField(choices=source_choices)
#     referral_from = models.CharField(verbose_name="转介绍人qq",max_length=64,blank=True)
#     consult_course= models.ForeignKey("Course",verbose_name="咨询课程")
#     content = models.TextField(verbose_name="咨询详情")
#     #添加标签
#     tags = models.ManyToManyField("Tag",blank=True,null=True)
#     #课程顾问，作为外键连接User表
#     consultant =models.ForeignKey("UserProfile")
#     memo = models.TextField(blank=True,null=True)
#     #设置自动增长
#     date =models.DateTimeField(auto_now_add=True)
#
#     def __srt__(self):
#         return self.qq
#
#     class Meta:
#             verbos_name="客户表"
#             verbos_name_plural = "客户表"
#
# class Tag(models.Model):
#     name =models.CharField(unique=True,max_length=32)
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbos_name="标签"
#         verbos_name_plural = "标签"
#
# class CustomerFollowUp(models.Model):
#     '''客户跟进表--客户、跟进人、跟进内容、客户意向选择、日期、'''
#     customer =models.ForeignKey("Customer")
#     content =models.TextField(verbose_name="跟进内容")
#     consultant = models.ForeignKey("UserProfile")
#     #意向
#     intention_choices = ((0,'2周内报名'),
#                          (1,'1个月内报名'),
#                          (2,'近期无报名计划'),
#                          (3,'已在其它机构报名'),
#                          (4,'已报名'),
#                          (5,'已拉黑')
#                          )
#
#     intention =models.SmallIntegerField(choices=intention_choices)
#     date = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return "<%s : %s>"%(self.customer.qq,self.intention)
#
#     class Meta:
#         verbos_name="客户跟进记录"
#         verbos_name_plural = "客户跟进记录"
#
# class Course(models.Model):
#     '''课程表 -- 课程名字、课程价格、学期、课程大纲 '''
#     name = models.CharField(max_length=64,unique=True)
#     price = models.PositiveSmallIntegerField()
#     period = models.PositiveSmallIntegerField(verbose_name="周期（月）")
#     outline = models.TextField()
#     def __str__(self):
#         return self.name
#
#         # class Meta:
#         #     verbos_name="课程表"
#         #     verbos_name_plural = "课程表"
#
#
# class Branch(models.Model):
#     '''校区'''
#     name = models.CharField(max_length=128,unique=True)
#     addr = models.CharField(max_length=128)
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbos_name="客户跟进记录"
#         verbos_name_plural = "客户跟进记录"
#
# class ClassList(models.Model):
#     '''班级表'''
#     branch = models.ForeignKey("Branch",verbose_name="分校")
#     course = models.ForeignKey("Course")
#     class_type_choices=((0,"面授"),
#                         (1,"面授（周末）"),
#                         (2,"网络班"),
#                         )
#     class_type =models.SmallIntegerField(choices=class_type_choices,verbose_name="班级类型")
#     semester = models.PositiveSmallIntegerField(verbose_name="学期")
#     teachers = models.ManyToManyField("UserProfile")
#     start_date = models.DateField(verbose_name="开班日期",blank=True,null=True)
#     end_date = models.DateField(verbose_name="结业日期",blank=True,null=True)
#
#     def __str__(self):
#         return "%s %s %s" %(self.branch,self.course,self.semester)
#
#     #联合唯一
#     class Meta:
#         unique_together = ('branch','course','semester')
#         verbos_name_plural = "班级表"
#         verbos_name="班级表"
#
#
# class CourseRecord(models.Model):
#     '''上课记录-- 班级、第几节（第几天课）、老师、是否有作业、作业标题、摘要、大纲'''
#     from_class = models.ForeignKey("ClassList",verbose_name="班级")
#     day_num = models.PositiveSmallIntegerField(verbose_name="第几节（天）")
#     teacher = models.ForeignKey("UserProfile")
#     has_homework = models.BooleanField(default=True)
#     homework_tile = models.CharField(max_length=128,blank=True,null=True)
#     outline = models.TextField()
#     def __str__(self):
#         return "%s %s" %(self.from_class,self.day_num)
#     class Meta:
#         #联合唯一
#         uninque_together = ("from_class","day_num")
#         verbos_name_plural = "上课记录"
#         verbos_name="上课记录"
#
# class StudyRecord(models.Model):
#     '''学习记录表（成绩表）-- 学生、课程记录、（出勤记录）是否出席选择'''
#     student =models.ForeignKey("Enrollment")
#     course_record = models.ForeignKey("CourseRecord")
#     attendency_choices =((0,"已签到"),
#                          (1,"迟到"),
#                          (2,"缺勤"),
#                          (3,"早退"),
#                          )
#     attendency = models.SmallIntegerField(choices=attendency_choices,default=0)
#     score_choices = ((100,"A+"),
#                      (90,"A"),
#                      (85,"B+"),
#                      (80,"B"),
#                      (75,"B-"),
#                      (70,"C+"),
#                      (60,"C"),
#                      (40,"C-"),
#                      (-50,"D"),
#                      (-100,"COPY"),
#                      (0,"N/A")#Not Avaiable
#                      )
#     score = models.SmallIntegerField(choices=score_choices,default=0)
#     memo = models.TextField(blank=True,null=True)
#     date = models.DateField(auto_now_add=True)
#
#     def __str__(self):
#         return "%s %s %s" %(self.student,self.course_record,self.score)
#
#     class Meta:
#         unique_together=('student','course_record')
#         verbos_name_plural = "学习记录"
#
#
#
# class  Enrollment(models.Model):
#     '''报名表--客户、报名哪个班级的课程、合同'''
#     customer = models.ForeignKey("Customer")
#     enrolled_class = models.ForeignKey("ClassList",verbose_name="所报班级")
#     consultant = models.ForeignKey("UserProfile",verbose_name="课程顾问")
#     contract_agree = models.BooleanField(default=False,verbose_name="学员已同意合同")
#     contract_approved = models.BooleanField(default=False,verbose_name="合同已审核")
#     date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return "%s %s"%(self.customer,self.enrolled_class)
#
#     class Meta:
#         unique_together =("customer","enrolled_class")
#         verbos_name_plural = "报名表"
#
#
# class Payment(models.Model):
#     '''缴费记录'''
#     customer = models.ForeignKey("Customer")
#     course = models.ForeignKey("Course",verbose_name="所报课程")
#     amount = models.PositiveIntegerField(verbose_name="数额",default=500)
#     consultant = models.DateTimeField(auto_now_add=True)
#     date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return  "%s %s" %(self.customer,self.amount)
#     class Meta:
#         verbos_name_plural = "缴费表"
#
#
# class UserProfile(models.Model):
#     '''账号表'''
#     #外键关联的方式有两种models.ForeignKey
#     user = models.OneToOneField(User)
#     name = models.CharField(max_length=32)
#     roles = models.ManyToManyField("Role",blank=True,null=True)
#     def __str__(self):
#         return  self.name
# class Role(models.Model):
#     '''角色表'''
#     name = models.CharField(max_length=32,unique=True)
#     def __str__(self):
#         return self.name
#         #
#     class Meta:
#         verbos_name_plural = "角色表"