
from django.db import models



class Parish(models.Model):
  parish_name = models.CharField(max_length=55)
  parish_id = None


  # This representation is used any time a base string representation
  # is needed, such as the web browseable API interface provide by
  # the framework.
  def __str__(self):
    return "{}: {}".format(self.id, self.parish_name)


  class Meta:
        managed = False
        db_table = 'Parish'


class CompanyInfo(models.Model):
  company_name = models.CharField(max_length=55)
  owner = models.CharField(max_length=55)
  company_id = models.CharField(max_length=55)
  email = models.CharField(max_length=55)
  address = models.CharField(max_length=55)
  city = models.CharField(max_length=55)
  state = models.CharField(max_length=55)
  zipcode = models.CharField(max_length=55)
  phone = models.CharField(max_length=55)

  class Meta:
        managed = False
        db_table = 'CompanyInfo'

  def __str__(self):
    return "{}: {}".format(self.id, self.company_name)



class CompaniesByParish(models.Model):
  city = models.CharField(max_length=55)
  company_name = models.CharField(max_length=55)
  state = models.CharField(max_length=55)
  parish_key = models.ForeignKey('Parish', models.DO_NOTHING, db_column='parish_key', blank=True, null=True)
  company_key = models.ForeignKey('Companyinfo', models.DO_NOTHING, db_column='company_key', blank=True, null=True)


  class Meta:
    managed = False
    db_table = 'CompaniesByParish'

  def __str__(self):
    return "{}: {}".format(self.id, self.company_name)


