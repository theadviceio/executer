from __future__ import absolute_import

import json
import yaml
import tempfile
import os
import sys
import utils.logs
import utils.errors
import utils.typeutils
#from . import typeutils


__version__ = 0.2
__author__ = 'weldpua2008@gmail.com'


def str_to_tempfile(str_to_write, is_delete=False,prefix='rde_hosts'):
    """Write a string to tempfile and get it name"""
    f_descr = tempfile.NamedTemporaryFile(delete=is_delete, prefix='rde_hosts')
    f_name = f_descr.name
    converted = utils.typeutils.str_to_str(str_to_write)
    f_descr.write(converted)
    f_descr.close

    return f_name

def get_config_data_as_dict(file_init_value, config_path=None, config_path_when_is_none=None):
    """Get configuration data

    :param file_init_value: default file content if file not exist
    :param config_path: config path
    :param config_path_when_is_none: config path that will used when config_path is None
    :return: prepared data with keys
    """
    data = {}
    default_value = file_init_value
    if config_path is None:
        config_path = config_path_when_is_none
    #if isinstance(file_init_value, dict):
    if utils.typeutils.is_dict(file_init_value):
        default_value = file_init_value.copy()
    elif utils.typeutils.is_list(file_init_value):
            #isinstance(file_init_value, list):
        default_value = file_init_value[:]
    try:
        data = get_file_as_json(
            config_path=config_path,
            init_value=default_value)
    # pylint: disable=broad-except
    except Exception as error:
        utils.errors.get_value_error(
            "Can't parse %s because %s" % (config_path, error))

    if not utils.typeutils.is_dict(data):
    #isinstance(data, dict):
        utils.errors.get_type_error(
            "Data error in config. Expected dictionary but it's: %s " %
            type(data))

    return data


def get_config_data_as_list(file_init_value, config_path=None, config_path_when_is_none=None):
    """Get configuration data

    :param file_init_value: default file content if file not exist
    :param config_path: config path
    :param config_path_when_is_none: config path that will used when config_path is None
    :return: prepared data with keys
    """
    data = []
    default_value = file_init_value
    if config_path is None:
        config_path = config_path_when_is_none
    #if isinstance(file_init_value, dict):
    if utils.typeutils.is_dict(file_init_value):
        default_value = file_init_value.copy()
    #elif isinstance(file_init_value, list):
    elif utils.typeutils.is_list(file_init_value):
        default_value = file_init_value[:]
    try:
        data = get_file_as_json(
            config_path=config_path,
            init_value=default_value)
    # pylint: disable=broad-except
    except Exception as error:
        utils.errors.get_value_error(
            "Can't parse %s because %s" % (config_path, error))

    if not utils.typeutils.is_list(data):
            #isinstance(data, []):
        utils.errors.get_type_error(
            "Data error in config. Expected dictionary but it's: %s " %
            type(data))

    return data


def store_config_in_json(data, config_path=None):
    if config_path is None:
        utils.errors.get_value_error(
            "Can't store file because wasn't provided")
    data_json = ""
    try:
        data_json = json.dumps(data, sort_keys=True, indent=4)
    # pylint: disable=broad-except
    except Exception as error:
        utils.errors.get_type_error("Can't convert to json %s" % error)

    try:
        if not os.path.exists(config_path):
            create_file(
                config_path=config_path,
                init_value=data_json)
        with open(config_path, "w") as json_data:
            json_data.write(data_json)
    # pylint: disable=broad-except
    except Exception as error:
        utils.errors.get_io_error(
            "Can't write config %s because %s" % (config_path, error))


def get_file_as_json(config_path, init_value):
    """return json data from file(if not exist will init in with init_value"""
    create_file(config_path=config_path, init_value=init_value)
    data_json = onlyget_file_as_json(config_path=config_path)
    return data_json


def get_file(config_path):
    try:
        return open(config_path).read()
    # pylint: disable=broad-except
    except Exception as error:
        utils.errors.get_value_error(
            "Can't read data from %s because %s" % (config_path, error))


def onlyget_file_as_json(config_path):
    try:
        with open(config_path, "r") as json_data:
            data = json.load(json_data)
        return data
    # pylint: disable=broad-except
    except Exception as error:
        utils.errors.get_value_error(
            "Can't read data from %s because %s" % (config_path, error))


def onlyget_file_as_yaml(config_path):
    try:
        with open(config_path, "r") as json_data:
            data = yaml.load(json_data)
        return data
    # pylint: disable=broad-except
    except Exception as error:
        utils.errors.get_value_error(
            "Can't read data from %s because %s" % (config_path, error))


def create_file(config_path, init_value):
    """create file if it not exist

    :param config_path: path to file
    :param init_value: initial value for file
    :return: return read data from file or die
    """
    # if not isinstance(config_path, basestring):
    if not utils.typeutils.is_string(config_path):
        utils.errors.get_value_error(
            "config_path in create_file not string, it's %s" %
            type(config_path))
    if len(config_path) < 1:
        utils.errors.get_value_error("create_file config_path was empty")

    try:
        if not os.path.exists(config_path):
            try:
                if not os.path.exists(
                        os.path.dirname(config_path)) and len(
                        os.path.dirname(config_path)) > 0:
                    os.makedirs(os.path.dirname(config_path))
            # pylint: disable=broad-except,invalid-name
            except Exception as error:
                utils.errors.get_value_error(
                    "Can't create dir: %s because %s " %
                    (os.path.dirname(config_path), error))
            write_content_to_file(filepath=config_path, init_value=init_value)
    # pylint: disable=broad-except,invalid-name
    except Exception as error:
        utils.errors.get_value_error(
            "Can't create: %s because %s " % (config_path, error))


def write_content_to_file(filepath, init_value):
    """Create file with init_value"

    :param filepath: path to file
    :param init_value: initial value that will be wrote if file not exists
    """
    file_content = None
    try:
        file_content = open(filepath, 'w+')
        file_content.write(json.dumps(init_value))
        utils.logs.debug("create new file %s" % filepath)
    # pylint: disable=broad-except,invalid-name
    except Exception as error:
        utils.errors.get_value_error(error)
    finally:
        file_content.close()
