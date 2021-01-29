from django.db import models

from main.MyModelFile import MyModel


class InterFloorOverlapping(MyModel):
    inter_floor_overlapping_material = models.CharField(verbose_name="Материал перекрытия", max_length=50, null=True,
                                                        blank=True)
    inter_floor_overlapping_status = models.CharField(verbose_name="Состояние перекрытия", max_length=50, null=True,
                                                      blank=True)

    class Meta:
        abstract = True


class AtticOverlapping(MyModel):
    attic_overlapping_material = models.CharField(verbose_name="Материал перекрытия", max_length=50, null=True,
                                                  blank=True)
    attic_overlapping_status = models.CharField(verbose_name="Состояние перекрытия", max_length=50, null=True,
                                                blank=True)

    attic_overlapping_warming = models.CharField(verbose_name="Утепление", max_length=50, null=True, blank=True)

    class Meta:
        abstract = True


class BasementOverlapping(MyModel):
    basement_overlapping_material = models.CharField(verbose_name="Материал перекрытия", max_length=50, null=True,
                                                     blank=True)
    basement_overlapping_status = models.CharField(verbose_name="Состояние перекрытия", max_length=50, null=True,
                                                   blank=True)

    class Meta:
        abstract = True


class Overlapping(InterFloorOverlapping, AtticOverlapping, BasementOverlapping):
    class Meta:
        abstract = True
