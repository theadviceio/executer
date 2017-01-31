import sys
import conf
import api.utils.typeutils
import api.utils.errors

__version__ = 0.1

__author__ = 'weldpua2008@gmail.com'

quote_func = None
if sys.version_info > (3,0,0):
    import shlex
    quote_func = shlex.quote
else:
    import pipes
    quote_func = pipes.quote


def prepare_cmd(**kwargs):
    """Prepare cmd string for run with ansible
    :param hosts: List or string of hosts for an inventory (default: 127.0.0.1)
    :param host: A host where run this module (default: 127.0.0.1)
    :param module: Which ansible module run
    :param module_args: Arguments of the module
    :param connection: Connection type. By default (local)

    :return: cmd
    :raises SyntaxError: on non-standart values
    :raises ValueError: on unexpected types
    """
    cmd = "%s " % conf.BIN_RUN_ANSIBLE
    hosts = ['127.0.0.1']
    if 'hosts' in kwargs:
        hosts = api.utils.typeutils.to_list(kwargs['hosts'])

    try:
        _inventory = ",".join(hosts) + ","
        inventory = "%s %s" % (conf.ansible.ANSIBLE_INVENTORY_KEY, _inventory)
        cmd += " %s" % inventory
    except Exception as error:
        api.utils.errors.get_syntax_error("Can't prepare_cmd:inventory because %s" % error)

    if 'module' not in kwargs:
        api.utils.errors.get_key_error("Can't run ansible without specify a module")
    ansible_module = kwargs['module']
    cmd += " %s%s" % (conf.ansible.ANSIBLE_MODULE_KEY, ansible_module)

    if 'module_args' not in kwargs:
        api.utils.errors.get_key_error("Can't run ansible without specify a module arguments")
    ansible_module_args = kwargs['module_args']
    ansible_module_args_line = ""
    if api.utils.typeutils.is_string(ansible_module_args):
        ansible_module_args_line = quote_func(ansible_module_args)
    elif api.utils.typeutils.is_list(ansible_module_args):
        ansible_module_args_line = quote_func(";".join(ansible_module_args))
    else:
        api.utils.errors.get_syntax_error("Can't prepare_cmd:ansible_module_args because wrong type %s" % type(ansible_module_args))
    cmd += " %s %s" % (conf.ansible.ANSIBLE_MODULE_ARGS_KEY, ansible_module_args_line)

    try:
        connection = "%slocal " % conf.ansible.ANSIBLE_CONNECTION_KEY
        if 'connection' in kwargs:
            connection = kwargs["connection"]
            if not api.utils.typeutils.is_string(connection):
                api.utils.errors.get_syntax_error("Can't prepare_cmd:connection because wrong type %s" % type(connection))
            connection = "%s%s" % (conf.ansible.ANSIBLE_CONNECTION_KEY, connection)
        cmd += " %s" % connection
    except Exception as error:
        api.utils.errors.get_syntax_error("Can't prepare_cmd:connection because %s" % error)

    host = '127.0.0.1'
    if 'host' in kwargs:
        host = kwargs['host']
    cmd += " %s" % host
    return cmd
