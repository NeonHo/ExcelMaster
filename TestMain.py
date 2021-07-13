import numpy as np
import xlrd

from ExcelSheetMaster import ExcelSheetMaster


def main():
    file_name = input("Enter the excel file Absolute Path:")  # E:\DraftBox\data2333.xlsx
    table = xlrd.open_workbook(file_name)
    sheet_index = eval(input("Enter the sheet you want to process:"))
    sheet = table.sheets()[sheet_index]
    excel_sheet_master = ExcelSheetMaster(sheet)
    column_info_list = [{'column_index': 2, 'min_border': 0.485, 'max_border': 100,
                         'include_min': False, 'include_max': True},
                        {'column_index': 1, 'min_border': 0, 'max_border': 5.185,
                         'include_min': True, 'include_max': True}]
    res_array = excel_sheet_master.is_all_columns_elements_in_range(column_info_list=column_info_list, begin_row_index=1)
    res_array1 = np.sum(res_array, axis=1)
    res_array2 = res_array1[res_array1 == 2]
    column_info_list = [{'column_index': 2, 'min_border': 0.485, 'max_border': 100,
                         'include_min': False, 'include_max': True},
                        {'column_index': 1, 'min_border': 0, 'max_border': 5.185,
                         'include_min': True, 'include_max': True},
                        {'column_index': 4, 'min_border': 1, 'max_border': 1,
                         'include_min': True, 'include_max': True},
                        ]
    res_array_3 = excel_sheet_master.is_all_columns_elements_in_range(column_info_list=column_info_list, begin_row_index=1)
    res_array_4 = np.sum(res_array_3, axis=1)
    res_array_5 = res_array_4[res_array_4 == 3]
    pass


if __name__ == '__main__':
    main()
