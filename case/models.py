from django.db import models
from db.base_model import BaseModel
# Create your models here.

class Case(BaseModel):
    level_choices = (
        (0,'高'),
        (1,'中'),
        (2,'低'),
    )

    case_types = (
        (0,'功能型'),
        (1,'页面校验'),
    )

    judge_results = (
        (0,'通过'),
        (1,'不通过'),
        (2,'未审核'),
        (3,'作废'),
    )

    case_status=(
        (0,'未执行'),
        (1,'已执行'),
        (2,'弃用'),
    )

    case_results = (
        (0,'通过'),
        (1,'未通过'),
        (2,'弃用'),
    )
    case_no =  models.CharField(max_length=50,verbose_name='用例编号')
    project_name = models.ForeignKey('Project',verbose_name='所属项目',on_delete=models.CASCADE)
    project_model = models.CharField(max_length=100,verbose_name='所属模块')
    project_desired = models.TextField(verbose_name='相关需求')
    case_title = models.CharField(max_length=200,verbose_name='用例标题')
    pre_condition = models.CharField(max_length=200,verbose_name='前置条件')
    run_step = models.CharField(max_length=300,verbose_name='执行步骤')
    expect_result = models.TextField(verbose_name='预期结果')
    expect_reality = models.TextField(verbose_name='实际结果')
    level = models.SmallIntegerField(default=1, choices=level_choices, verbose_name='优先级')
    case_type = models.SmallIntegerField(default=0, choices=case_types, verbose_name='用例类型')
    create_by = models.CharField(max_length=100,verbose_name='用例创建者')
    judge_by = models.CharField(max_length=100,verbose_name='用例评审者')
    judge_result = models.SmallIntegerField(default=2, choices=judge_results, verbose_name='评审结果')
    case_statu = models.SmallIntegerField(default=0, choices=case_status, verbose_name='用例状态')
    case_result = models.SmallIntegerField(default=1, choices=case_results, verbose_name='用例执行结果')
    remark = models.CharField(max_length=200,verbose_name='备注')



    class Meta:
        db_table = 'tms_case'
        verbose_name = '用例表'
        verbose_name_plural = verbose_name

    def __str__(self):
        try:
            return self.case_title
        except Case.DoesNotExist:
            return self.case_title

class Project(BaseModel):
    project_name = models.CharField(max_length=200,verbose_name='项目名称')
    manager = models.CharField(max_length=100,verbose_name='项目经理')

    class Meta:
        db_table = 'tms_project'
        verbose_name = '项目表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.project_name

