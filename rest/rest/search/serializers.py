from rest_framework import serializers
from django.contrib.auth.models import User
from search.models import CompanyInfo, Parish, CompaniesByParish

# Using the HyperlinkedModelSerializer will examine the relationships
# between the models, and the data, and provide a hyperlink to the
# related resource instead of the primary key
#   http://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/#hyperlinking-our-api


class ParishSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Parish
    fields = ('id', 'url', 'parish_name', 'parish_id')


class CompanyInfoSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = CompanyInfo
    fields = ('id', 'url', 'company_name','owner','email','company_id', 'address', 'city', 'state', 'zipcode', 'phone')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'url', 'username')


class CompaniesByParishSerializer(serializers.HyperlinkedModelSerializer):



  class Meta:
    model = CompaniesByParish
    fields = ('id', 'url', 'city', 'company_name', 'state', 'parish_key', 'company_key')



