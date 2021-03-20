from Egida.settings import ENGINEERING_COMMUNICATION_URL


def inn_dir_path(instance, filename):
    return ENGINEERING_COMMUNICATION_URL + '/id_{}/{}'.format(instance.id, filename)


def inn_dir_path2(instance, filename):
    return ENGINEERING_COMMUNICATION_URL + '/id_{}/documentation/{}'.format(instance.id, filename)
