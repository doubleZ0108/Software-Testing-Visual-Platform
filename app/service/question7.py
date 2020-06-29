from app.csv.index import charge as charge_index
from app.common.commonUtil import df_update, df_read


def charge_atom_v1(arg_list):
    pay_method_list = ['Alipay', 'BankCard']
    monthly_fee, cost_per_min = 25, 0.15
    talk_time_month, unpaid_num_year, unpaid_cost_across_year, pay_method = \
        arg_list[0], arg_list[1], arg_list[2], arg_list[3]
    cost = monthly_fee
    if talk_time_month < 0 or talk_time_month > 44640 or unpaid_num_year < 0 or unpaid_num_year > 11 or pay_method not in pay_method_list or unpaid_cost_across_year < 0 or unpaid_cost_across_year > 500:
        return 'error'
    if talk_time_month <= 60 and unpaid_num_year <= 1:
        cost += talk_time_month * cost_per_min * 0.01
    elif talk_time_month <= 120 and unpaid_num_year <= 2:
        cost += talk_time_month * cost_per_min * 0.015
    elif talk_time_month <= 180 and unpaid_num_year <= 3:
        cost += talk_time_month * cost_per_min * 0.02
    elif talk_time_month <= 300 and unpaid_num_year <= 3:
        cost += talk_time_month * cost_per_min * 0.025
    elif talk_time_month > 300 and unpaid_num_year <= 6:
        cost += talk_time_month * cost_per_min * 0.03
    else:
        cost += talk_time_month * cost_per_min
    cost += unpaid_cost_across_year * 0.05
    return cost


def charge_atom_v2(arg_list):
    pay_method_list = ['Alipay', 'BankCard']
    monthly_fee, cost_per_min = 25, 0.15
    talk_time_month, unpaid_num_year, unpaid_cost_across_year, pay_method = \
        arg_list[0], arg_list[1], arg_list[2], arg_list[3]
    cost = monthly_fee
    if talk_time_month < 0 or talk_time_month > 44640 or unpaid_num_year < 0 or unpaid_num_year > 11 or pay_method not in pay_method_list or unpaid_cost_across_year < 0 or unpaid_cost_across_year > 500:
        return 'error'
    if talk_time_month <= 60 and unpaid_num_year <= 1:
        cost += talk_time_month * cost_per_min * (1 - 0.01)
    elif talk_time_month <= 120 and unpaid_num_year <= 2:
        cost += talk_time_month * cost_per_min * (1 - 0.015)
    elif talk_time_month <= 180 and unpaid_num_year <= 3:
        cost += talk_time_month * cost_per_min * (1 - 0.02)
    elif talk_time_month <= 300 and unpaid_num_year <= 3:
        cost += talk_time_month * cost_per_min * (1 - 0.025)
    elif talk_time_month > 300 and unpaid_num_year <= 6:
        cost += talk_time_month * cost_per_min * (1 - 0.03)
    else:
        cost += talk_time_month * cost_per_min
    cost += unpaid_cost_across_year * 0.05
    return float('%.2f' % cost)


code_v = {
    'v1': charge_atom_v1,
    'v2': charge_atom_v2
}


class question7:
    def __init__(self):
        pass

    @staticmethod
    def charge(method_type, code_version='v2'):
        csv_path = charge_index[method_type]
        df, arg_start, arg_end = df_read(csv_path)
        output1 = []
        for i in range(0, len(df)):
            arg_list = df.iloc[i, arg_start:arg_end].values.tolist()
            output1.append(code_v[code_version](arg_list))
        return df_update(df=df, csv_path=csv_path, actual_outputs=[output1], tester_name='anonymous')

    @staticmethod
    def charge_method_test(request, code_version='v2'):
        arg_list = [request['talk_time_month'], request['unpaid_num_year'], request['unpaid_cost_across_year'],
                    request['pay_method']]
        return code_v[code_version](arg_list)
