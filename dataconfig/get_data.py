#coding=utf-8
from unit.open_excle import Openexcle
from unit.read_json import Readjson
class Getdata():
    def __init__(self):
        self.ope=Openexcle()

    #获取用例id
    def case_id(self,row):
        value=self.ope.get_cell_value(row,0)
        return value
    #获取用例名称
    def case_name(self,row):
        value=self.ope.get_cell_value(row,1)
        return value
    #获取url
    def case_url(self,row):
        value=self.ope.get_cell_value(row,2)
        return value
    #获取是否运行
    def is_run(self,row):
        value=self.ope.get_cell_value(row,3)
        if value=='yes':
            return True
        else:
            return False
    #获取请求方式
    def case_method(self,row):
        value = self.ope.get_cell_value(row,4)
        return value
    #获取是否需要header
    def case_header(self,row):
        value = self.ope.get_cell_value(row, 5)
        if value=='':
            return None
        else:
            return value
    #获取是否依赖值
    def case_relyon(self,row):
        value = self.ope.get_cell_value(row, 6)
        if value=='':
            return None
        else:
            return value
    #获取依赖返回数据
    def case_Relyreturn(self,row):
        value=self.ope.get_cell_value(row,7)
        if value=='':
            return None
        else:
            return value
    # 获取依赖数据字段
    def case_relyword(self,row):
        value = self.ope.get_cell_value(row, 8)
        if value=='':
            return None
        else:
            return value
    #获取请求数据
    def case_requestdata(self,row):
        readjson=Readjson()
        key=self.ope.get_cell_value(row,9)
        value=readjson.read_value(key)
        return value
    #获取期望值
    def case_expectedvalue(self,row):
        value = self.ope.get_cell_value(row, 10)
        return value
    def write_case_result(self,row,value):
        self.ope.write_excle_value(row,11,value)


if __name__ == '__main__':
    to=Getdata()
    print(to.case_header(3))