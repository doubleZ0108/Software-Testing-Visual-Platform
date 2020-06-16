import os

BASE_DIR = os.path.dirname(__file__)

calendar = {
    'boundary': BASE_DIR + '/q1/calendar-boundary.csv',
    'equivalence': BASE_DIR + '/q1/calendar-equivalent.csv'
}

triangle = {
    'boundary': BASE_DIR + '/q1/triangle-boundary.csv',
    'equivalence': BASE_DIR + '/q1/triangle-equivalent.csv'
}

commission = {
    'boundary': BASE_DIR + '/q2/commission-boundary.csv'
}

charge = {
    'boundary': BASE_DIR + '/q7/charge-boundary.csv',
    'equivalence': BASE_DIR + '/q7/charge-equivalent.csv',
    'decision': BASE_DIR + '/q7/charge-decision.csv'
}

sales = {
    'statement': BASE_DIR + '/q8/sales-statement-cov.csv',
    'judge': BASE_DIR + '/q8/sales-judge-cov.csv',
    'condition': BASE_DIR + '/q8/sales-condition-cov.csv',
    'judge-condition': BASE_DIR + '/q8/sales-judge-condition-cov.csv',
    'condition-combination': BASE_DIR + '/q8/sales-condition-combination-cov.csv'
}

csv_dir = {
    'calendar': calendar,
    'triangle': triangle,
    'commission': commission,
    'charge': charge,
    'sales': sales
}
