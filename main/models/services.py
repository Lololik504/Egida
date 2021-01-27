def get_model_fields(model):
    return model._meta.fields


def get_model_name(model):
    return model._meta.model_name
