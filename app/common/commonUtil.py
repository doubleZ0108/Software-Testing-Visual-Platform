import datetime
import pandas as pd


def df_update(df, csv_path, actual_outputs, tester_name):
    """
    更新,并输出到csv
    :param df: 源 DataFrame
    :param csv_path: csv 所在路径
    :param actual_outputs: 实际输出列表(可能有多个)
    :param tester_name: 测试人员名称
    :return: {正确个数，错误个数，准确率}
    """
    total_case_num = len(df)
    output_num = len(actual_outputs)
    df['Correctness'] = None
    if output_num == 1:
        df['ActualOutput'] = actual_outputs[0]
        df['ActualOutput'] = df['ActualOutput'].astype(str)
        df.loc[df['ExpectedOutput'] != df['ActualOutput'], 'Correctness'] = False
    else:
        for i in range(0, output_num):
            ac_label = 'ActualOutput' + str(i + 1)
            ex_label = 'ExpectedOutput' + str(i + 1)
            df[ac_label] = actual_outputs[i]
            df[ac_label] = df[ac_label].astype(str)
            df.loc[df[ex_label] != df[ac_label], 'Correctness'] = False
    df['Correctness'] = df['Correctness'].fillna(True)
    df['Time'] = [datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')] * len(df)
    df['TesterName'] = [tester_name] * len(df)
    df.to_csv(csv_path, index=None)
    df = df.groupby(by=['Correctness'])['Correctness'].count()
    try:
        true_num = df[True]
    except Exception as e:
        true_num = 0
    return {'True': int(true_num), 'False': int(total_case_num - true_num),
            'accuracy': float(true_num / total_case_num)}


def df_read(csv_path, arg_start_label='TestCaseID', arg_end_label='ExpectedOutput'):
    """
    读取csv
    :param csv_path: csv 路径
    :param arg_start_label: 参数起始位置的前一个标签
    :param arg_end_label: 参数终止位置的后一个标签
    :return: DataFrame 参数起始索引，参数终止索引
    """
    df = pd.read_csv(csv_path)
    arg_start = df.columns.values.tolist().index(arg_start_label) + 1
    arg_end = df.columns.values.tolist().index(arg_end_label)
    return df, arg_start, arg_end



