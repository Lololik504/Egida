

class MyModel:
    static_fields = ["id"]

    def update(self, data):
        for k, v in data.items():
            if self.static_fields.__contains__(k):
                continue
            try:
                setattr(self, k, v)
            except:
                pass
        self.save()
