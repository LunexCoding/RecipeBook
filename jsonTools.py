import json
from json import JSONEncoder


class JsonEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__


class JsonTools:
    @staticmethod
    def jsonWrite(obj, fileObj):
        json.dump(obj, fileObj, cls=JsonEncoder, ensure_ascii=False, indent=4)

    @staticmethod
    def jsonLoad(fileObj):
        return json.load(fileObj)
