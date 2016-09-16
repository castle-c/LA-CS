from django.db import models



class Parish(models.Model):
  parish_name = models.CharField(max_length=55)
  parish_id = None


  # This representation is used any time a base string representation
  # is needed, such as the web browseable API interface provide by
  # the framework.
  def __str__(self):
    return "{}: {}".format(self.id, self.name)

class ComapnyInfo(models.Model):
  company_name = models.CharField(max_length=55)
  owner = models.CharField(max_length=55)
  company_id = models.CharField(max_length=55)
  email = models.CharField(max_length=55)
  address = models.CharField(max_length=55)
  city = models.CharField(max_length=55)
  zipcode = models.CharField(max_length=55)
  phone = models.CharField(max_length=55)

  def __str__(self):
    return "{}: {}".format(self.id, self.name)



class CompaniesByParish(models.Model):
  user = models.ForeignKey('auth.User', related_name='')
  city = models.CharField(max_length=55)
  company_name = models.CharField(max_length=55)
  state = models.CharField(max_length=55)
  company_key = models.ForeignKey(CompanyInfo, related_name='company')
  parish_key = models.ForeignKey(Parish, related_name='parish')

  def __str__(self):
    return "{}: {}".format(self.id, self.name)


