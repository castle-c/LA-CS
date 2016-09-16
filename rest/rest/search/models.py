from django.db import models




class Parish(models.Model):
  parish_name = models.CharField(max_length=55)


  # This representation is used any time a base string representation
  # is needed, such as the web browseable API interface provide by
  # the framework.
  def __str__(self):
    return "{}: {}".format(self.id, self.name)

class ComapnyInfo(models.Model):
  company_name = models.CharField(max_length=55)
  owner = models.CharField(max_length=55)
  email = models.CharField(max_length=55)
  address = models.CharField(max_length=55)
  city = models.CharField(max_length=55)
  zipcode = models.CharField(max_length=55)
  phone

  def __str__(self):
    return "{}: {}".format(self.id, self.name)



class CompaniesByParish(models.Model):
  # owner = models.ForeignKey('auth.User', related_name='tickets')
  city = models.CharField(max_length=55)
  company_name = models.CharField(max_length=55)
  company_id = models.ForeignKey(CompanyInfo, related_name='company')
  state = models.CharField(max_length=55)
  parish_id = models.ForeignKey(Parish, related_name='parish')

  def __str__(self):
    return "{}: {}".format(self.id, self.habitat.name)


