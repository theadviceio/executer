import utils.errors
import sys

__version__ = 0.1
__author__ = 'weldpua2008@gmail.com'

PY3 = sys.version_info[0] == 3

if PY3:
    string_types = (str, bytes)
    long = int
else:
    string_types = basestring,


def split_str(str_to_split, mask):
    if sys.version_info < (3,):
        result = str_to_split.split(mask)
    else:
        if isinstance(str_to_split, str):
            result = str_to_split.split(mask)
        else:
            result = str_to_split.decode('utf8').split(mask)
    return result

def is_dict(test_variable=None):
    try:
        return isinstance(test_variable, dict)
    except Exception as error:
        utils.errors.get_runtime_error("Can't check is_dict because: %s" % error)


def is_list(test_variable=None):
    try:
        return isinstance(test_variable, list)
    except Exception as error:
        utils.errors.get_runtime_error("Can't check is_list because: %s" % error)



def is_numeric(test_variable):
    try:
        return isinstance(test_variable, (int, float, long, complex))
    except Exception as error:
        utils.errors.get_runtime_error("Can't check is_numeric because: %s" % error)


def is_string(test_variable=None):
    try:
        return isinstance(test_variable, string_types)
    except Exception as error:
        utils.errors.get_runtime_error("Can't check is_string because: %s" % error)


def is_bool(test_variable=None):
    try:
        return isinstance(test_variable, bool)
    except Exception as error:
        utils.errors.get_runtime_error("Can't check is_string because: %s" % error)


def typeerror_on_not_string(test_variable=None):
    if not isinstance(test_variable, string_types):
        utils.errors.get_type_error("Wrong type %s not a string" % type(test_variable))
    return test_variable


def is_none_return_list(test_variable=None):
    if test_variable is None:
        return []
    return test_variable


def is_none_return_dict(test_variable=None):
    if test_variable is None:
        return {}
    return test_variable


def is_none_return_hosts(hosts=None):
    if hosts is None:
        return ["127.0.0.1"]
    return hosts


# def to_json(someting, is_formated=True):
#     """return someting as json"""
#     if is_formated:
#         return json.dumps(someting, sort_keys=True, indent=4)
#     return json.dumps(someting)

def get_from_kwargs_or_none(key, kwargs):
    """return none or value of key
    :param key:
    :param kwargs: dict or ignore
    :return: return kwargs[key] or None
    """
    value = None
    if isinstance(kwargs, dict):
        try:
            if key in kwargs:
                value = kwargs[key]
        except Exception as error:
            utils.errors.get_runtime_error("Can't get_from_kwargs_or_none because %s" % error)
    return value

def to_list(argms):
    """return List if it was None/List/Dict/String"""
    result = []
    if isinstance(argms, string_types) or result is None:
        result = [argms]
    elif isinstance(argms, list):
        result = argms
    elif isinstance(argms, dict):
        result = list(argms.keys())
    else:
        result = [argms]
    return result


def str_to_str(convert_str):
    result = convert_str
    if not is_string(convert_str):
        utils.errors.get_type_error("Can't convert to str %s" % type(str_to_str))
    if sys.version_info > (3, 0, 0):
        if isinstance(convert_str, str):
            result = bytes(convert_str, 'UTF-8')
    return result