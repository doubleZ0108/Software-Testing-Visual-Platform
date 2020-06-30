from app.csv.index import commission as commission_index
from app.common.commonUtil import df_update, df_read


def commission_atom(arg_list):
    host_price, display_price, peripheral_price = 25, 30, 45
    host_num, display_num, peripheral_num = arg_list[0], arg_list[1], arg_list[2]
    if host_num <= 0 or display_num <= 0 or peripheral_num <= 0 or host_num > 70 or display_num > 80 or peripheral_num > 90:
        return 'error', 'error'
    commission = host_num * host_price + display_num * display_price + peripheral_num * peripheral_price
    if commission <= 1000:
        return commission, float('%.2f' % (commission * 0.1))
    elif commission <= 1800:
        return commission, float('%.2f' % (commission * 0.15))
    else:
        return commission, float('%.2f' % (commission * 0.2))


class question2:
    def __init__(self):
        pass

    @staticmethod
    def commission(method_type):
        csv_path = commission_index[method_type]
        df, arg_start, arg_end = df_read(csv_path, arg_end_label='ExpectedOutput1')
        output1 = []
        output2 = []
        for i in range(0, len(df)):
            arg_list = df.iloc[i, arg_start:arg_end].values.tolist()
            output_1, output_2 = commission_atom(arg_list)
            output1.append(output_1)
            output2.append(output_2)
        return df_update(df=df, csv_path=csv_path, actual_outputs=[output1, output2], tester_name='anonymous')

    @staticmethod
    def commission_method_test(request):
        arg_list = [request['host'], request['display'], request['peripheral']]
        sales, commission = commission_atom(arg_list)
        return {'sales': sales, 'commission': commission}
