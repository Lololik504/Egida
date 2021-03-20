from Egida.settings import INDOOR_AREAS_URL

def inn_dir_path(instance, filename):
    return INDOOR_AREAS_URL + '/id_{}/{}'.format(instance.id, filename)