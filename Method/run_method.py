#coding=utf-8
import requests
import json
class RunMethod():
    def get_send(self,url,data=None,header=None):
        res=requests.get(url=url,params=data,headers=header,verify=False)
        return res.json()
    def post_send(self,url,data=None,header=None):
        if header!=None:
            res=requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res.json()
    def run_mian(self,url,method,data,header=None):
        if method=='Post':
            res=self.post_send(url,data,header)
        else:
            res=self.get_send(url,data,header)
        return json.dumps(res,ensure_ascii=False)
if __name__ == '__main__':
    ope=RunMethod()
    url='http://www.clearbos.cn:81/api/flow/area/getchildrenarealist'
    data= {
    "ParentAreaCode":"110000"
  }
    heade={"Authorization": "Bearer 4hjWYFzu4g0oAaGAoUCER51n3Uerp0Fw9RqSnTXZIkV9Ftt65yl2qBZcsxeh13Dm-zp9W3Qu-cLPtnzsNx8SWhB_fvVJ9kPytyo4AE83gk347EMA6cOdgayPaD7rmTSX_eLvCIVsYtNbYMhq0vuoAR4jXVABRh9gCfc2238QYe_Cue2kB_3vAi6GBNTAwApJ4lb5BkkIo_hd4H9pBT9l4BW21LcIysH7KxHBAvg-XkTMJHbRu1_fobhKv6Xiljr1_rCVeaiVFcah96fFJj07pfeQ5nqn5KCNCQu4zkNOSp3yVgAZcE9hvlSnMZFleVru"}
    print(ope.run_mian(url,'Post',data,heade))
