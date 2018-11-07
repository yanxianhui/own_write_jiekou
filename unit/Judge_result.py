#coding=utf-8

class Contain():
    def is_contain(self,str_one,str_two):
        res=None
        if str_one in str_two:
            res=True
        else:
            res=False
        return res
if __name__ == '__main__':
     Common=Contain()
     print(Common.is_contain('"Code": 200', '{"Code": 200, "Message": "质检成功", "Data": null}'))

