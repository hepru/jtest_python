from django.db import models

class TreeMenuCategory(models.Model):

    name = models.CharField( "name", max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name


class TreeMenu(models.Model):

    name = models.CharField("name", max_length=255, blank=True, null=False)

    category = models.ForeignKey(
        TreeMenuCategory,
        name='category',
        on_delete=models.CASCADE,
        blank=False,
        null=True
    )
    link = models.CharField("link", max_length=1000, blank=True, null=False)

    parent = models.ForeignKey(
        'self',
        name='parent',
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True,
        default=0
    )

    def __str__(self):
        return self.name
