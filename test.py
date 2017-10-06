import xlwt

wb = xlwt.Workbook()

ws = wb.add_sheet("Test_sheet")

ws.write(0,0,"Testiusdh")

wb.save("ex.xls")
