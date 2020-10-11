from datetime import datetime
import sys


class Salesforce:
    def __init__(self, driver):
        self.driver = driver

    def get_raw_records(self, query):
        records = self.driver.query(query)
        return records

    def convert_odict_into_list(self, records):
        new_cases_list = []
        print(records['records'])
        for case in records['records']:
            case_dict = dict(case_number=case['CaseNumber'], subject=case['Subject'],
                             description=case['Description'], priority=case['Priority'],
                             owner_id=case['OwnerId'])
            new_cases_list.append(case_dict)
        return new_cases_list

    def get_unassigned_cases(self, query):
        raw_records = self.get_raw_records(query)
        if raw_records:
            records = self.convert_odict_into_list(raw_records)
            return records

    def get_assigned_cases(self, records, query):
        records_tuple_str = str(tuple(records))
        query = query.format(records_tuple_str)
        assigned_cases_list = self.driver.query(query)
        return assigned_cases_list

    @staticmethod
    def remove_duplicate_cases(records, duplicate_cases):
        records[:] = [case for case in records if case['case_number'] not in duplicate_cases]
        return records

    @staticmethod
    def get_case_numbers(records):
        case_numbers_list = [case['case_number'] for case in records]
        return case_numbers_list

    @staticmethod
    def create_list_of_param_tuples(records):
        param_tuple_list = []
        for case in records:
            param_tuple_str = (case['case_number'], case['subject'], case['description'],
                               case['priority'], case['owner_id'],
                               1, str(datetime.now()))
            param_tuple_list.append(param_tuple_str)
        return param_tuple_list
