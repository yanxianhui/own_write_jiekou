#coding=utf-8
from dataconfig.get_data import Getdata
from unit.open_excle import Openexcle
from Method.run_method import RunMethod
from dataconfig.dependent_data import DependentData
from unit.read_json import Readjson
from unit.dependent_header import Header
from unit.Judge_result import Contain
import json
class Runcase():
    def __init__(self):
        self.data=Getdata()
        self.opeccle=Openexcle()
        self.Metmod=RunMethod()
        self.contain=Contain()
    def run_case_erp(self):
        pass_case = []
        file_case = []
        lines=self.opeccle.get_line()
        for i in range(1,lines):
            is_run=self.data.is_run(i)
            if is_run:
                url=self.data.case_url(i)
                method=self.data.case_method(i)
                header=self.data.case_header(i)
                data=self.data.case_requestdata(i)
                expect=self.data.case_expectedvalue(i)
                dependent_case=self.data.case_relyon(i)
                #print(url,method,header,data,expect,dependent_case)
                if dependent_case!=None:
                    self.dependata = DependentData(dependent_case)
                    dependword = self.data.case_relyword(i)
                    dependent_response=self.dependata.get_dependent_key(i)
                    data[dependword]=dependent_response
                if header=='write':
                    res = self.Metmod.run_mian(url,method,data)
                    self.header=Header(res)
                    self.header.write_header()
                    #print(json.loads(res))
                elif header=='yes':
                    self.opejson = Readjson('../data/cookid.json')
                    cookid=self.opejson.read_value('coid')
                    #print(cookid)
                    res = self.Metmod.run_mian(url,method,data,cookid)
                    #print(json.loads(res))
                else:
                    res=self.Metmod.run_mian(url,method,data,header)
                    #print(json.loads(res))
                if self.contain.is_contain(expect,res)==True:
                    self.data.write_case_result(i,'pass')
                    pass_case.append(i)
                else:
                    self.data.write_case_result(i,res)
                    file_case.append(i)
        print("通过接口",len(pass_case),'  ',"失败接口",len(file_case))







if __name__ == '__main__':
    ope=Runcase()
    ope.run_case_erp()



