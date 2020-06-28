from app.csv.index import sales as sales_index
from app.common.commonUtil import df_update, df_read


def sales_atom(arg_list):
    annual_sales, leave_days, rate_cash_to_account = arg_list[0], arg_list[1], arg_list[2]
    zero = float('%.2f' % 0)
    if annual_sales < 0 or leave_days < 0 or rate_cash_to_account > 1 or rate_cash_to_account < 0:
        return 'error', 'error'
    if annual_sales > 200 and leave_days <= 10:
        if rate_cash_to_account >= 0.6:
            commission_rate = 7
        else:
            commission_rate = 0
    else:
        if rate_cash_to_account <= 0.85:
            commission_rate = 6
        else:
            commission_rate = 5
    if commission_rate == 0:
        return 'no commission', 'no commission'
    else:
        return commission_rate, float('%.2f' % (annual_sales / commission_rate))


class question8:
    def __init__(self):
        pass

    @staticmethod
    def sales(method_type):
        csv_path = sales_index[method_type]
        df, arg_start, arg_end = df_read(csv_path,arg_end_label='ExpectedOutput1')
        output1 = []
        output2 = []
        for i in range(0, len(df)):
            arg_list = df.iloc[i, arg_start:arg_end].values.tolist()
            output_1, output_2 = sales_atom(arg_list)
            print(output_1, output_2)
            output1.append(output_1)
            output2.append(output_2)
        return df_update(df=df, csv_path=csv_path, actual_outputs=[output1, output2], tester_name='anonymous')

    @staticmethod
    def sales_method_test(request):
        arg_list = [request['annual_sales'], request['leave_days'], request['rate_cash_to_account']]
        return sales_atom(arg_list)
