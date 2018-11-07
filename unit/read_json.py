#coding=utf-8
import json
class Readjson():
    def __init__(self,file_name=None):
        if file_name==None:
            self.file_name='../data/user.json'
        else:
            self.file_name=file_name
        self.data=self.read_json()
    def read_json(self):
        with open(self.file_name,encoding='utf-8') as fp:
            data=json.load(fp)
            return data
    def read_value(self,key=''):
        #res=None
        if key=='':
            res=None
        else:
            res=self.data[key]
        return res
    def write_json(self,data):
        with open('../data/cookid.json','wb+') as fp:
            fp.write(json.dumps(data).encode("utf-8"))

if __name__ == '__main__':
    ope=Readjson('../data/cookid.json')
    print(ope.read_value('coid'))