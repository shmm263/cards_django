from datetime import datetime, timedelta

from django.conf import settings
from django.db import models
from django.core.validators import EmailValidator

# Create your models here.
from django.urls import reverse


class LookupRegion(models.Model):
    id = models.CharField(primary_key=True,max_length=5)
    regions = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'lookup_region'
        verbose_name = 'Регионы',
        verbose_name_plural = 'Регионы'

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.regions


class LookupRajon(models.Model):
    rajons = models.CharField(max_length=200)
    region = models.ForeignKey('LookupRegion', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lookup_rajon'
        verbose_name = 'Районы',
        verbose_name_plural = 'Районы'

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        # LookupRajon.objects.filter(region_id=5)
        return '{0} ({1})'.format(self.rajons, self.region)


class Patient(models.Model):
    first_name = models.CharField(verbose_name='Фамилия',db_column='first_name', max_length=100)  # Field name made lowercase.
    last_name = models.CharField(verbose_name='Имя',db_column='last_name', max_length=100)  # Field name made lowercase.
    patron_name = models.CharField(verbose_name='Отчество',max_length=150)  # Field name made lowercase.
    inn = models.CharField(verbose_name='ИНН',max_length=10 , unique=True,
        error_messages={'required': 'Please provide your inn.',
                        'unique': 'An account with this inn exist.'},)
    date_birthday = models.DateField(verbose_name='День рождения',blank=True, null=True)
    phone_home = models.CharField(verbose_name='Домашний телефон', max_length=10)
    phone_mobile = models.CharField(verbose_name='Мобильный телефон', max_length=13)
    email = models.CharField(verbose_name='Почта',max_length=250, unique=True,
        error_messages={'required': 'Please provide your email address.',
                        'unique': 'An account with this email exist.'},)
    place_of_work = models.TextField(verbose_name='Место работы',db_column='place_of_work',blank=True, null=True)
    reference_number = models.CharField(verbose_name='Номер л-го удостверения',max_length=30, null=True)
    region = models.ForeignKey('LookupRegion', models.DO_NOTHING, blank=True, null=True,verbose_name='Область',)
    rajon = models.ForeignKey('LookupRajon', models.DO_NOTHING, blank=True, null=True, verbose_name='Район',)
    locality = (
        ('м', 'місто'),
        ('с', 'село'),
        ('смт', 'селище міського типу'),
    )
    addr_locality = models.CharField(verbose_name= 'Тип населенного пункта', max_length=3,choices=locality, blank=True, default='с', help_text="Введите тип населенного пункта")
    addr_city = models.CharField(verbose_name= 'Город',max_length=100)
    abbreavation = (
        ('бульвар', 'бульвар'),
        ('вул', 'вулиця'),
        ('кв', 'квартал'),
        ('пр-к', 'провулок'),
        ('пр', 'проспект'),
        ('тупік', 'тупік'),
        ('узвіз', 'узвіз'),
        ('шосе', 'шосе'),
    )
    addr_abbreavation = models.CharField(verbose_name='Тип(улица, бульвар...)',max_length=10,choices=abbreavation, blank=True, default='вул', help_text="Введите абривиатуру улицы")
    addr_street = models.CharField(verbose_name='Улица',max_length=200)
    addr_house = models.CharField(verbose_name='Дом',max_length=5)
    addr_corpus = models.CharField(verbose_name='Корпус',max_length=5,default=0)
    addr_room = models.CharField(verbose_name='Квартира',max_length=5,default=0)
    addr_index = models.CharField(verbose_name='Индекс',max_length=5)
    date_update=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["first_name"]
        managed = True
        db_table = 'patient'
        verbose_name = 'Пациент',
        verbose_name_plural = 'Пациент'

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        # rajon_id = LookupRajon.objects.filter(region_id__regions__contains='Киевская')
        return '%s %s %s, %s, %s' % (self.first_name, self.last_name, self.patron_name, self.email, self.inn)

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('patient-detail', args=[str(self.id)])


class MedExamination(models.Model):
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)
    date_medical_examination = models.DateField(verbose_name='Дата медосмотра',default=datetime.now,blank=True)
    purpose = (
        ('Огляд водія', 'Огляд водія'),
        ('Дозвіл на зброю', 'Дозвіл на зброю'),
        ('Санітарна книжка', 'Санітарна книжка'),
        ('Сертифікат нарколога', 'Сертифікат нарколога'),
        ('Сертифікат психіатора', 'Сертифікат психіатора'),
        ('Довідка в бесейн', 'Довідка в бесейн'),
        ('Форма 086', 'Форма 086'),
        ('Інші', 'Інші'),

    )
    purpose_medical_examination = models.CharField(verbose_name='Цель', max_length=20, choices=purpose, blank=True,
                                                   default='Огляд водія', help_text="Введите цель медосмотра")
    status_id=(
        ('Да','Да'),
        ('Нет', 'Нет'),
    )
    patient_status= models.CharField(verbose_name='Статус', max_length=3, choices=status_id, blank=True,
                                                   default='Нет', help_text="Введите статус уведомления")
    dat_end = models.DateField(verbose_name='Дата действия справки',default=datetime.now()+timedelta(days=731))
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]
        managed = True
        db_table = 'medexamination'
        verbose_name = 'Медосмотры',
        verbose_name_plural = 'Медосмотры'

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        # rajon_id = LookupRajon.objects.filter(region_id__regions__contains='Киевская')
        return '%s, %s, %s' % (self.date_medical_examination, self.purpose_medical_examination, self.dat_end)

class PatientList(models.Model):
    pid = models.IntegerField(primary_key=True)
    patient = models.TextField(verbose_name='Пациент')
    inn = models.CharField(verbose_name='ИНН', max_length=10)
    date_birthday = models.DateField(verbose_name='День рождения')
    phone_home = models.CharField(verbose_name='Домашний телефон', max_length=10)
    phone_mobile= models.CharField(verbose_name='Мобильный телефон', max_length=13)
    email = models.CharField(verbose_name='Почта', max_length=255)
    place_of_work = models.TextField(verbose_name='Место работы' )
    reference_number = models.CharField(verbose_name='Номер л-го удостверения', max_length=30)
    addr_locality = models.CharField(verbose_name= 'Тип населенного пункта', max_length=3)
    addr_city = models.CharField(verbose_name= 'Город', max_length=100)
    addr_street = models.TextField(verbose_name= 'Улица')
    addr_house = models.CharField(verbose_name= 'Дом', max_length=5)
    addr_corpus = models.CharField(verbose_name= 'Корпус', max_length=5)
    addr_room = models.CharField(verbose_name= 'Квартира', max_length=5)
    addr_index = models.CharField(verbose_name= 'Индекс', max_length=5)
    rajons = models.CharField(verbose_name= 'Район', max_length=200)
    regions = models.CharField(verbose_name= 'Область', max_length=200)
    mm = models.TextField(verbose_name='Медосмотры')
    date_update = models.DateTimeField(verbose_name='Дата ввода')

    class Meta:
        managed = False
        ordering = ['patient']
        db_table = 'patient_list'


class MedExamtList(models.Model):
    mid = models.IntegerField(primary_key=True)
    patient = models.TextField(verbose_name='Пациент')
    email = models.CharField(verbose_name='Почта', max_length=20)
    phone_mobile = models.CharField(verbose_name='Мобильный телефон', max_length=13)
    purpose_medical_examination= models.CharField(verbose_name='Цель медосмотра', max_length=20)
    date_medical_examination = models.DateField(verbose_name='Дата медосмотра')
    dat_end = models.DateField(verbose_name='Дата окончанмя действия справки')
    patient_status = models.CharField( verbose_name='Статус уведомления', max_length=3)
    date_update = models.DateTimeField(verbose_name='Дата ввода')
    patient_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'medexam_list'
