import numpy as np


# pip3 install xlrd==1.2.0

class ExcelSheetMaster:
    def __init__(self, sheet):
        self.sheet = sheet

    def is_in_range(self, row_index, column_index, min_border, max_border, include_min: bool, include_max: bool):
        """
        if element in sheet at position [row_index, column_index] in the range.
        :param row_index:
        :param column_index:
        :param min_border:
        :param max_border:
        :param include_min:
        :param include_max:
        :return: bool
        """
        value = float(self.sheet.cell_value(row_index, column_index))
        if include_min:
            if include_max:
                if min_border <= value <= max_border:
                    return True
                else:
                    return False
            else:
                if min_border <= value < max_border:
                    return True
                else:
                    return False
        else:
            if include_max:
                if min_border < value <= max_border:
                    return True
                else:
                    return False
            else:
                if min_border < value < max_border:
                    return True
                else:
                    return False

    def is_all_columns_elements_in_range(self, column_info_list: list, begin_row_index: int):
        """
        If all column is in their own range? Give an array with value:(0, 1)
        :param begin_row_index: the first row we count.
        :param column_info_list: [column_index, min_border, max_border, include_min: bool, include_max: bool]
        :return: an array with value:(0, 1) 1=in range, 0=not in range.
        """
        res_array = np.zeros(shape=(self.sheet.nrows, self.sheet.ncols), dtype=int)
        for column_info in column_info_list:
            for row_index in range(self.sheet.nrows - 1):
                if row_index >= begin_row_index:
                    res = self.is_in_range(row_index=row_index,
                                           column_index=column_info['column_index'],
                                           min_border=column_info['min_border'],
                                           max_border=column_info['max_border'],
                                           include_min=column_info['include_min'],
                                           include_max=column_info['include_max'])
                    if res:
                        res_array[row_index][column_info['column_index']] = 1
        return res_array
