import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 'hello world!'
sheet.cell(row=3, column=3).value = "Good Bye"
sheet.append(["Python","Java","HTML","JAVASRIPT"])
sheet.append(["Coala","Study","Crawling"])
wb.save("test.xlsx")