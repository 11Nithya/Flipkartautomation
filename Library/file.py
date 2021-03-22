import xlrd

class Reader:
    def wbreader(self, obj_filename, obj_sheetname):
        with xlrd.open_workbook(obj_filename,obj_sheetname) as wb:
            ws=wb.sheet_by_name(obj_sheetname)
            rows=ws.get_rows()
            next(rows)
            read={row[0].value:(row[1].value,row[2].value) for row in rows}
            return read, read.keys()

    # def wbvalue(self, test_data_filename, test_data_sheetname, testcase):
    #     with xlrd.open_workbook(test_data_filename) as wb:
    #         ws = wb.sheet_by_name(test_data_sheetname)
    #         rows = ws.get_rows()
    #         next(rows)
    #         r2= {row[0].value:(row[1].value,row[2].value) for row in rows}
    #         return r2[testcase]