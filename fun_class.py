import json
import os
dir_name = os.path.dirname(__file__)
# print(dir_name)
class check__:
    def __init__(self,args,id):
       self.value = False
       for x in args:
        # print()
        if x.get(id):
            # print("111")
            self.value = True
        else:
            self.value = False


            # print("222")
class rm_perm:
    def __init__(self,args,id):
        for x in args:
            if x.get(id):
                args.remove(x)
                # print(args)
                self.args = args

class token:
    def __init__(self):
        # print()
        with open(dir_name+"/token.json", "r") as f:
            file__ = json.load(f)
            # return file__["token"]
            self.token = file__["token"]
            # print()
