import json
import os
dir_name = os.path.dirname(__file__)
# print(dir_name)
class check__:
    def __init__(self,args,id):
       for x in args:
        print(x.get("aaa"))


class token:
    def __init__(self):
        # print()
        with open(dir_name+"/token.json", "r") as f:
            file__ = json.load(f)
            # return file__["token"]
            self.token = file__["token"]
            # print()
