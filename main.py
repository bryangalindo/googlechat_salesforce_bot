from datetime import datetime

from simple_salesforce import (SalesforceError, Salesforce as SimpleSalesforce)

import bot as bot
import constants as c
import database as db
import queries as q
from salesforce import Salesforce
import utility as util


def get_sorted_case_numbers(sf_cases, db_cases):
    set_a = set(sf_cases)
    set_b = set(db_cases)
    new_cases = list(set_a - set_b)
    duplicate_cases = list(set_a.intersection(set_b))
    sorted_cases_dict = {'new_cases': [], 'duplicate_cases': []}
    sorted_cases_dict['new_cases'] = new_cases
    sorted_cases_dict['duplicate_cases'] = duplicate_cases
    return sorted_cases_dict


try:
    salesforce = SimpleSalesforce(username=c.SF_USERNAME, password=c.SF_PASSWORD,
                                  security_token=c.SF_TOKEN)
except SalesforceError as e:
    util.update_error_log_transactions('sf', e)

sf = Salesforce(salesforce)
records = sf.get_unassigned_cases(q.TEST_MULTI_RECORD_QUERY)

if records:
    conn = db.create_connection('cases.db')
    sf_case_numbers = sf.get_case_numbers(records)
    db_case_numbers = db.get_case_numbers(conn, q.GET_CASE_NUMBERS_QUERY)

    sorted_case_numbers = get_sorted_case_numbers(sf_case_numbers, db_case_numbers)

    if sorted_case_numbers['new_cases']:
        duplicate_case_numbers = sorted_case_numbers['duplicate_cases']
        new_cases = sf.remove_duplicate_cases(records, duplicate_case_numbers)
        query_params = sf.create_list_of_param_tuples(new_cases)

        db.create_table(conn, q.CREATE_TABLE_QUERY)
        db.insert_new_cases_into_local_db(conn, q.INSERT_INTO_TABLE_QUERY, query_params)
        db.commit_and_close(conn)

        for case in new_cases:
            bot_message = c.BOT_MESSAGE_TEMPLATE.format(case['case_number'],
                                                        case['priority'],
                                                        case['subject'],
                                                        case['description'])
            bot.send_new_case_notification(bot_message)









# assigned_cases = sf.get_assigned_cases(db_case_numbers, q.ASSIGNED_RECORDS_QUERY)
