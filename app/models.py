from datetime import date

from django.db import models


class Task(models.Model):
    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'

    start_date = models.DateField('Data inicial', auto_now_add=True)
    task_number = models.DecimalField('Número tarefa', max_digits=7, decimal_places=4, blank=False, null=False)
    ssi = models.DecimalField('Número SSI', max_digits=7, decimal_places=4, blank=True, null=True)
    description = models.TextField('Descrição', blank=False, null=False)
    font_name = models.CharField('Nome fonte', max_length=50, blank=False, null=False)
    final_opnion = models.TextField('Parecer Final', blank=True, null=True)
    started = models.BooleanField('Iniciada', default=False)
    finished = models.BooleanField('Finalizada', default=False)
    submeted = models.BooleanField('Submetido', default=False)
    end_date = models.DateField('Data final', null=True)

    @property
    def calc_date(self):
        if self.finished:
            self.end_date = date.today()

    def __str__(self):
        return self.font_name
