from django.db import models
from main.MyModelFile import MyModel
from Egida.settings import DOCUMENT_URL


def inn_dir_path(instance, filename):
    # print(DOCUMENT_ROOT)
    return DOCUMENT_URL + '/inn_{}/{}'.format(instance.school.INN, filename)


class Document(MyModel):
    school = models.ForeignKey(to="main.School", verbose_name="Школа", on_delete=models.CASCADE, default=None)
    passport_BTI = models.FileField(verbose_name='Паспорт БТИ', upload_to=inn_dir_path)
    topographic_plan = models.FileField(verbose_name='Топографический план', upload_to=inn_dir_path)
    teplosnabj_MK = models.FileField(verbose_name='МК на теплоснабжение', upload_to=inn_dir_path)
    vodosnabj_MK = models.FileField(verbose_name='МК на водоснабжение', upload_to=inn_dir_path)
    electrosnabj_MK = models.FileField(verbose_name='МК на электроснабжение', upload_to=inn_dir_path)

    class Meta:
        verbose_name = 'Документы'
        verbose_name_plural = 'Документы'
        app_label = 'main'
