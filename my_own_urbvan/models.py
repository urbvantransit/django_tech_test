from django.db import models

class Users(models.Model):
    """

    Template as a Users object in the app my_own_urbvan
    we got a basic information about user.


    id -- unique id to describe user_(number)
    fisrt_name -- name user
    last_name -- last name user
    email_user -- email user to connect data user
    phone_user -- phone user to send sms
    pass_user -- password user to use in app registration

    """
    fisrt_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    email_user = models.EmailField(blank=True, max_length=50)
    phone_user = models.IntegerField(blank=True)
    pass_user = models.CharField(blank=True, max_length=50)


    def __str__(self):
        return '%s, #-%s' % (self.fisrt_name,self.phone_user)

    def __repr__(self):
        return '{} #-{}'.format(self.fisrt_name,self.phone_user)


#---------------------Model Class separator ------------------------------

class Locations(models.Model):
    """
    Location object is the representation of physical station
    id -- This is the unique identifier for object instance.
    name -- This is the common identifier for a physical location.
    coordinates --  Latitude and Longuitude as string.
                    example. "19.4094937,-99.1634261"
    geometry -- Similar to coordinate but using with postgis

    """
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=19, decimal_places=16)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)

    def __str__(self):
        return '%s' % (self.name)

    def __repr__(self):
        return '{}'.format(self.name)

#---------------------Model Class separator ------------------------------

class Stations(models.Model):
    """
    Template as a Station object in the app my_own_urbvan
    we got a basic information about Stations

    id -- default provided by own django models, but,
    I notice it'll be the sta_(number) in the other model

    location -- this is a FK field to merge with the Locations model.

    order -- order number and default=0

    is_active -- a Boolean field to check is_active or inactive current station.

    """
    location = models.ForeignKey(Locations, on_delete=models.DO_NOTHING)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '%s' % (self.id)

    def __repr__(self):
        return '{}'.format(self.id)



#---------------------Model Class separator ------------------------------


class Lines(models.Model):
    """
    Template as a Lines object to save the lines in my_own_urbvan app

    id -- id unique example: line_(numbre)
    name --the line's name
    color -- the color's line to identify between them

    """
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=8)

    def __str__(self):
        return '%s' % (self.name)

    def __repr__(self):
        return '{}'.format(self.name)



#---------------------Model Class separator ------------------------------

class Routes(models.Model):
    """
    We'll create a Many2Many field with stations
    and a fk in lines
    direction -- as a route direction
    is_active -- a Boolean field to check is_active or inactive current route.
    """
    line = models.ForeignKey(Lines, on_delete=models.DO_NOTHING)
    stations = models.ManyToManyField(Stations)
    direction = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '%s' % (self.id)

    def __repr__(self):
        return '{}'.format(self.id)
