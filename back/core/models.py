class Document():
    fields = []
    export_fields = []
    editable_fields = []

    def to_dict(self):
        return {key: getattr(self, key) for key in self.export_fields}
    
    def to_insert_dict(self):
        return {key: getattr(self, key) for key in self.fields}

    def to_update_dict(self):
        return {key: getattr(self, key) for key in self.editable_fields}
        
    @staticmethod
    def from_dict(dict_object: dict):
        raise NotImplementedError

def from_dict_class(dict_object: dict, Class):
    kwargs = {
        key: value for (key, value) in dict_object.items()
        if key in Class.fields
    }
    return Class(**kwargs)