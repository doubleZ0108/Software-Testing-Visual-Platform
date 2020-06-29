import datetime
from app.csv.index import calendar as calender_index
from app.csv.index import triangle as triangle_index
from app.common.commonUtil import df_update, df_read


def calendar_atom(arg_list):
    v_list_new = [str(x) for x in arg_list]
    year, month, day = arg_list[0], arg_list[1], arg_list[2]
    if (year < 2000 or year > 2100) and (month < 1 or month > 12) and (day < 1 or day > 31):
        return 'Illegal Case'
    if year < 2000 or year > 2100:
        return 'Year Exceed'
    if month < 1 or month > 12:
        return 'Month Exceed'
    if day < 1 or day > 31:
        return 'Day Exceed'
    try:
        _date = datetime.datetime.strptime('-'.join(v_list_new), '%Y-%m-%d').date()
    except Exception as e:
        return str(e)
    return str(_date + datetime.timedelta(days=1))


def triangle_atom_v1(arg_list):
    a, b, c = arg_list[0], arg_list[1], arg_list[2]
    if a > 200 or b > 200 or c > 200:
        return '数值越界'
    if a <= 0 or b <= 0 or c <= 0:
        return '数值越界'
    if a + b > c and a + c > b and b + c > a:
        if a == b or a == c or b == c:
            if a == b and b == c:
                return '等边三角形'
            elif a * a + b * b == c * c or b * b + c * c == a * a or a * a + c * c == b * b:
                return '等腰直角三角形'
            else:
                return '直角三角形'
        elif a * a + b * b == c * c or b * b + c * c == a * a or a * a + c * c == b * b:
            return '直角三角形'
        else:
            return '普通三角形'
    else:
        return '非三角形'


def triangle_atom_v2(arg_list):
    a, b, c = arg_list[0], arg_list[1], arg_list[2]
    if a > 200 or b > 200 or c > 200:
        return '数值越界'
    if a <= 0 or b <= 0 or c <= 0:
        return '数值越界'
    if a + b > c and a + c > b and b + c > a:
        if a == b or a == c or b == c:
            if a == b and b == c:
                return '等边三角形'
            elif a * a + b * b == c * c or b * b + c * c == a * a or a * a + c * c == b * b:
                return '等腰直角三角形'
            else:
                return '等腰三角形'
        if a * a + b * b == c * c or b * b + c * c == a * a or a * a + c * c == b * b:
            return '直角三角形'
        else:
            return '普通三角形'
    else:
        return '非三角形'


triangle_code_v = {
    'v1': triangle_atom_v1,
    'v2': triangle_atom_v2
}


class question1:
    def __init__(self):
        pass

    @staticmethod
    def triangle(method_type, code_version='v2'):
        csv_path = triangle_index[method_type]
        df, arg_start, arg_end = df_read(csv_path=csv_path)
        output1 = []
        for i in range(0, len(df)):
            arg_list = df.iloc[i, arg_start:arg_end].values.tolist()
            output1.append(triangle_code_v[code_version](arg_list))
        return df_update(df=df, csv_path=csv_path, actual_outputs=[output1], tester_name='anonymous')

    @staticmethod
    def calendar(method_type):
        csv_path = calender_index[method_type]
        df, arg_start, arg_end = df_read(csv_path)
        output1 = []
        for i in range(0, len(df)):
            arg_list = df.iloc[i, arg_start:arg_end].values.tolist()
            output1.append(calendar_atom(arg_list))
        return df_update(df=df, csv_path=csv_path, actual_outputs=[output1], tester_name='anonymous')

    @staticmethod
    def triangle_method_test(request, code_version='v2'):
        arg_list = [request['edge1'], request['edge2'], request['edge3']]
        return triangle_code_v[code_version](arg_list)

    @staticmethod
    def calendar_method_test(request):
        arg_list = [request['year'], request['month'], request['day']]
        return calendar_atom(arg_list)
