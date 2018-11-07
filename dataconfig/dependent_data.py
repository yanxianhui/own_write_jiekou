#coding=utf-8
from Method.run_method import RunMethod
from unit.open_excle import Openexcle
from dataconfig.get_data import Getdata
from jsonpath_rw import parse
from unit.read_json import Readjson
import json
class DependentData():
    def __init__(self,case_id):
        self.run_resquet=RunMethod()
        self.ope=Openexcle()
        self.data=Getdata()
        self.case_id=case_id
        self.opejson=Readjson('../data/cookid.json')
    def get_dependent(self):
        row_num=self.ope.get_id_row(self.case_id)
        url=self.data.case_url(row_num)
        method=self.data.case_method(row_num)
        resquest_data=self.data.case_requestdata(row_num)
        header=self.data.case_header(row_num)
        res=None
        if header=='yes':
            headers=self.opejson.read_value('coid')
            res=self.run_resquet.run_mian(url,method,resquest_data,headers)
        else:
            res = self.run_resquet.run_mian(url, method, resquest_data)
        return json.loads(res)

    def get_dependent_key(self,row):
        response_data=self.get_dependent()
        dependent_data=self.data.case_Relyreturn(row)
        json_exe=parse(dependent_data)
        madil=json_exe.find(response_data)
        return [math.value for math in madil][0]


if __name__ == '__main__':
    ope=DependentData('Imooc-22')
    print(ope.get_dependent())
    print(ope.get_dependent_key(25))
    #print(ope.get_dependent_key(15))
