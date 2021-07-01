from django.db.models import Model


class MyModel(Model):
    static_fields = ["id"]
    bool_fields = ["current_year", "agreed", "fully_executed", "particially_executed"]

    def update(self, data):
        for k, v in data.items():
            if self.static_fields.__contains__(k):
                continue
            if self.bool_fields.__contains__(k):
                try:
                    if v == 'null':
                        setattr(self, k, None)
                    elif v == 'false':
                        setattr(self, k, False)
                    else:
                        setattr(self, k, True)
                except:
                    pass
                continue
            try:
                setattr(self, k, v)
            except:
                pass
        self.save()

    class Meta:
        abstract = True
