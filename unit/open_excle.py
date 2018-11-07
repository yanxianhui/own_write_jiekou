#coding=utf-8
from xlrd import open_workbook
from xlutils.copy import copy

class Openexcle():
    def __init__(self,file_name=None,sheet_id=None):
        if file_name==None:
            self.file_name='C:\\Users\yanxianhuiclearbos\PycharmProjects\owns_write\data\case2.xls'
            self.sheet_id =0
        else:
            self.file_name=file_name
            self.sheet_id=sheet_id
        self.data=self.read_excle()
    #读取excle
    def read_excle(self):
        data=open_workbook(self.file_name)
        table=data.sheets()[self.sheet_id]
        return table
    #获取excle行数
    def get_line(self):
        table=self.data
        return table.nrows
    #根据行列获取值
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)
    #获取caseid列值
    def caseid_col_value(self):
        return self.data.col_values(0)
    # 根据caseid获取行数
    def get_id_row(self, caseid):
        col_vluse = self.caseid_col_value()
        num = 0
        for case in col_vluse:
            if case == caseid:
                return num
            num = num + 1
    # 根据行获取行数据
    def get_row_data(self, row):
        value = self.data.row_values(row)
        return value

    #写如excle测试结果
    def write_excle_value(self,row,col,value):
        read_data = open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)


if __name__ == '__main__':
    ope=Openexcle()
    #print(ope.caseid_col_value())
    print(ope.get_id_row('Imooc-16'))