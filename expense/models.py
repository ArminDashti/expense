from django.db import models

class expense(models.Model):
    shop_name = models.CharField(max_length=50,verbose_name='Shop Name')
    expense = models.IntegerField(verbose_name='Expense')
    sh_date = models.IntegerField(verbose_name='Date')
    ins_date = models.DateTimeField(auto_now_add=True)
    owner_id = models.IntegerField()
