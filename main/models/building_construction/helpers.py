from Egida.settings import BUILDING_MEDIA_URL

def inn_dir_path(instance, filename):
    return BUILDING_MEDIA_URL + '/id_{}/{}'.format(instance.id, filename)