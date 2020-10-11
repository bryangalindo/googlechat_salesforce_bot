from datetime import datetime

def update_error_log_transactions(log, error):
    if log == 'db':
        log = 'log/database_error.txt'
        error = '{}: {}\n\n'.format(datetime.now(), error[-2])
    elif log == 'sf':
        log = 'log/salesforce_error.txt'
        error = '{}: {}\n\n'.format(datetime.now(), error)
    elif log =='bot':
        log = 'log/bot_error.txt'
        error = '{}: {}\n\n'.format(datetime.now(), error)

    with open(log, 'a') as f:
        f.write(error)

def convert_list_to_tuple_str(lst):
    tuple_str = '()'.join([''for case in lst])
