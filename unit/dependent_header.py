#coding=utf-8
import json
from Method.run_method import RunMethod
from unit.read_json import Readjson
class Header():
    def __init__(self,res):
        self.ope_header=json.loads(res)
    def get_cookid(self):
        cookid=self.ope_header['Data']['AccessToken']
        return cookid

    def write_header(self):
        data=self.get_cookid()
        coodid={
            'coid':{
                "Authorization": "Bearer %s" % (data)
        }
        }
        self.ope_json=Readjson()
        self.ope_json.write_json(coodid)


if __name__ == '__main__':
        ope = RunMethod()
        url = 'http://www.clearbos.cn:81/api/auth/login/signin'
        data = {
            "userAccount": "15890158362",
            "userPassword": "123456",
            "VerificationCode": "259199",
            "EncryptCode": ""
        }
        dae=ope.run_mian(url, 'Post', data)
        print(dae)
        hera=Header(dae).write_header()
        print(hera)