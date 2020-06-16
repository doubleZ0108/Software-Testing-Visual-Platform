from app.csv.index import sales as sales_index
from app.common.commonUtil import df_update, df_read


def sales_atom(arg_list):
    annual_sales, leave_days, rate_cash_to_account = arg_list[0], arg_list[1], arg_list[2]
    commission = 0
    if annual_sales < 0 and leave_days < 0 and 0 > rate_cash_to_account > 1:
        return 'error'
    if annual_sales > 200 and leave_days <= 10:
        if rate_cash_to_account >= 0.6:
            commission = annual_sales / 7
        else:
            commission = 0
    else:
        if rate_cash_to_account <= 0.85:
            commission = annual_sales / 6
        else:
            commission = annual_sales / 5
    return float('%.2f' % commission)


class question8:
    def __init__(self):
        pass

    @staticmethod
    def sales(method_type):
        csv_path = sales_index[method_type]
        df, arg_start, arg_end = df_read(csv_path)
        output1 = []
        for i in range(0, len(df)):
            arg_list = df.iloc[i, arg_start:arg_end].values.tolist()
            output1.append(sales_atom(arg_list))
        return df_update(df=df, csv_path=csv_path, actual_outputs=[output1], tester_name='anonymous')

    @staticmethod
    def sales_method_test(request):
        arg_list = [request['annual_sales'], request['leave_days'], request['rate_cash_to_account']]
        return sales_atom(arg_list)
