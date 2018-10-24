import django.db import models


class User(models.Model):
    """

    This class use a template as a user in this App
    we got a basic information about user.

    fisrt_name -- name user
    last_name -- last name user
    email_user -- email user
    phone_user -- phone user

    """
    fisrt_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    email_user = models.EmailField(blank=True, max_length=50)
    phone_user = models.IntegerField(blank=True,max_length=10)


    def __str__(self):
        return '%s, #%s' % (self.fisrt_name,self.phone_user)

    def __repr__(self):
        return '{} #{}'.format(self.fisrt_name,self.phone_user)
