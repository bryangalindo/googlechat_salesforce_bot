from collections import OrderedDict
from pprint import pprint

from constants import INSTANCE_URL, SESSION_ID
from queries import TEST_SINGLE_RECORD_QUERY, TEST_MULTI_RECORD_QUERY
from salesforce import get_cases_ordered_dict, transform_cases_into_dict


def pass_or_fail_message(funct, _object):
    if _object:
        print('{} - {}'.format(funct.__name__, 'Successful!'))
    else:
        print('{} - {}'.format(funct.__name__, 'Failed!'))


def test_single_case_extraction():
    ordered_dict = get_cases_ordered_dict(INSTANCE_URL,
                                          SESSION_ID,
                                          TEST_SINGLE_RECORD_QUERY)
    return pass_or_fail_message(test_single_case_extraction, ordered_dict)


def test_multi_case_extraction():
    ordered_dict = get_cases_ordered_dict(INSTANCE_URL,
                                          SESSION_ID,
                                          TEST_MULTI_RECORD_QUERY)
    return pass_or_fail_message(test_multi_case_extraction, ordered_dict)


def test_single_case_transform():
    single_ordered_dict = OrderedDict([('totalSize', 1), ('done', True),
    ('records', [OrderedDict([('attributes', OrderedDict([('type', 'Case'),
    ('url', '/services/data/v42.0/sobjects/Case/5000d00001dIoOUAA0')])),
    ('CaseNumber', '00942893'),
    ('Description', 'A surveyor was missing access to HCSS Plans.'),
    ('Priority', 'Level 4 - Low'),
    ('OwnerId', '0050d000007SxccAAC')])])])
    case = transform_cases_into_dict(single_ordered_dict)
    return pass_or_fail_message(test_single_case_transform, case)


def test_multi_case_transform():
    multi_ordered_dict = OrderedDict([('totalSize', 2), ('done', True),
    ('records', [OrderedDict([('attributes', OrderedDict([('type', 'Case'),
    ('url', '/services/data/v42.0/sobjects/Case/5000d00001dIoOUAA0')])),
    ('CaseNumber', '00942893'),
    ('Description', 'A surveyor was missing access to HCSS Plans.'),
    ('Priority', 'Level 4 - Low'), ('OwnerId', '0050d000007SxccAAC')]),
    OrderedDict([('attributes', OrderedDict([('type', 'Case'),
    ('url', '/services/data/v42.0/sobjects/Case/5000d00001dIpt4AAC')])),
    ('CaseNumber', '00942913'),
    ('Description', 'Customer was attempting something.'),
    ('Priority', 'Level 4 - Low'), ('OwnerId', '0050d000007SxccAAC')])])])
    cases = transform_cases_into_dict(multi_ordered_dict)
    return pass_or_fail_message(test_multi_case_transform, cases)


if __name__ == '__main__':
    test_single_case_extraction()
    test_multi_case_extraction()
    test_single_case_transform()
    test_multi_case_transform()
