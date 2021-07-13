import xlrd

from ExcelSheetMaster import ExcelSheetMaster


def main():
    file_name = input("Enter the excel file Absolute Path:")
    table = xlrd.open_workbook(file_name)
    sheet_index = eval(input("Enter the sheet you want to process:"))
    sheet = table.sheets()[sheet_index]
    excel_sheet_master = ExcelSheetMaster(sheet)
    excel_sheet_master.is_all_columns_elements_in_range()


if __name__ == '__main__':
    main()
