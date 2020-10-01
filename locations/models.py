from django.db import models
from django.utils.translation import ugettext_lazy as _


# class BaseModel(models.Model):
#     """
#     model that will be inherited by all models to add common fields.
#     """
#     updated_on = models.DateTimeField(auto_now=True, null=True)
#     created_on = models.DateTimeField(auto_now_add=True, editable=False)
#
#     class Meta:
#         abstract = True
#
#
# class State(BaseModel):
#     name = models.CharField(max_length=50, unique=True)
#
#     class Meta:
#         db_table = 'STATE'
#         verbose_name = _('state')
#         verbose_name_plural = _('states')
#
#     def __str__(self):
#         return '{}'.format(self.name)
#
#
# class District(BaseModel):
#     name = models.CharField(max_length=50)
#     state = models.ForeignKey(State, related_name='districts', on_delete=models.CASCADE)
#     pincode = models.CharField(max_length=10, default='')
#
#     class Meta:
#         db_table = 'DISTRICT'
#         verbose_name = _('district')
#         verbose_name_plural = _('districts')
#
#     def __str__(self):
#         return '{}, {}'.format(self.name, self.state.name)


class Location(models.Model):
    name = models.CharField(max_length=50, unique=True)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10, default='')
    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        db_table = 'LOCATION'
        verbose_name = _('location')
        verbose_name_plural = _('locations')

    def __str__(self):
        return '{}, {}'.format(self.name, self.state)
