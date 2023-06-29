from url_filter.filtersets import ModelFilterSet
from . import models

class KatFilterSet(ModelFilterSet):
    class Meta(object):
        model = models.Kat