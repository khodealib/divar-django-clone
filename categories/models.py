from django.db import models
from django.utils.translation import gettext_lazy as _
from treebeard.mp_tree import MP_Node

from utilities.base_model import BaseModel


class Category(BaseModel, MP_Node):
    name = models.CharField(max_length=50, verbose_name=_("name"))
    slug = models.SlugField(max_length=200, null=True, blank=True, allow_unicode=True, verbose_name=_("slug"))

    node_order_by = ["name"]

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")
