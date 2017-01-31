import utils.logs
import sys

__version__ = 0.1
__author__ = 'weldpua2008@gmail.com'


class TransitionError(Exception):

    """Raised when an operation attempts a state transition that's not allowed."""

    def __init__(self, message):
        """Attributes:

        _previous -- state at beginning of transition
        _next -- attempted new state
        message -- explanation of why the specific transition is not allowed
        """
        super(TransitionError, self).__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class NotFoundError(Exception):

    """Raised when an operation attempts a state transition that's not allowed."""

    def __init__(self, message):
        """Attributes:

        _previous -- state at beginning of transition
        _next -- attempted new state
        message -- explanation of why the specific transition is not allowed
        """
        super(NotFoundError, self).__init__(message)
        self.message = message

    def __str__(self):
        return self.message


def get_notfound_error(error, logging_type="critical", store_log=True):
    """logging error and after that raise SyntaxError"""
    try:
        _e = "Call from %s:%s" % (sys._getframe().f_back.f_code.co_name,sys._getframe( 1 ).f_lineno )
        utils.logs.log(error=_e, logging_type=logging_type)
    except Exception:
        pass
    utils.logs.log(error=error, logging_type=logging_type, store_log=store_log)
    raise NotFoundError("%s" % error)


def get_syntax_error(error, logging_type="critical"):
    """logging error and after that raise SyntaxError"""
    try:
        _e = "Call from %s:%s" % (sys._getframe().f_back.f_code.co_name,sys._getframe( 1 ).f_lineno )
        utils.logs.log(error=_e, logging_type=logging_type)
    except Exception:
        pass
    utils.logs.log(error=error, logging_type=logging_type)
    raise SyntaxError("%s" % error)


def get_runtime_error(error, logging_type="critical"):
    """logging error and after that raise Value error"""
    try:
        _e = "Call from %s:%s" % (sys._getframe().f_back.f_code.co_name,sys._getframe( 1 ).f_lineno )
        utils.logs.log(error=_e, logging_type=logging_type)
    except Exception:
        pass
    utils.logs.log(error=error, logging_type=logging_type)
    raise RuntimeError("%s" % error)


def get_io_error(error, logging_type="critical"):
    """logging error and after that raise Value error"""
    try:
        _e = "Call from %s:%s" % (sys._getframe().f_back.f_code.co_name,sys._getframe( 1 ).f_lineno )
        utils.logs.log(error=_e, logging_type=logging_type)
    except Exception:
        pass
    utils.logs.log(error=error, logging_type=logging_type)
    raise IOError("%s" % error)


def get_notimplemented_error(error, logging_type="critical"):
    """logging error and after that raise Value error"""
    try:
        _e = "Call from %s:%s" % (sys._getframe().f_back.f_code.co_name,sys._getframe( 1 ).f_lineno )
        utils.logs.log(error=_e, logging_type=logging_type)
    except Exception:
        pass
    utils.logs.log(error=error, logging_type=logging_type)
    raise NotImplementedError("%s" % error)


def get_transition_error(error, logging_type="critical"):
    """logging error and after that raise Value error"""
    try:
        _e = "Call from %s:%s" % (sys._getframe().f_back.f_code.co_name,sys._getframe( 1 ).f_lineno )
        utils.logs.log(error=_e, logging_type=logging_type)
    except Exception:
        pass
    utils.logs.log(error=error, logging_type=logging_type)
    raise TransitionError("%s" % error)


def get_key_error(error, logging_type="critical"):
    """logging error and after that raise Key error"""
    try:
        _e = "Call from %s:%s" % (sys._getframe().f_back.f_code.co_name,sys._getframe( 1 ).f_lineno )
        utils.logs.log(error=_e, logging_type=logging_type)
    except Exception:
        pass
    utils.logs.log(error=error, logging_type=logging_type)
    raise KeyError("%s" % error)


def get_type_error(error, logging_type="critical"):
    """logging error and after that raise Tyoe error"""
    try:
        _e = "Call from %s:%s" % (sys._getframe().f_back.f_code.co_name,sys._getframe( 1 ).f_lineno )
        utils.logs.log(error=_e, logging_type=logging_type)
    except Exception:
        pass
    utils.logs.log(error=error, logging_type=logging_type)
    raise TypeError("%s" % error)


def get_value_error(error, logging_type="critical"):
    """logging error and after that raise Value error"""
    try:
        _e = "Call from %s:%s" % (sys._getframe().f_back.f_code.co_name,sys._getframe( 1 ).f_lineno )
        utils.logs.log(error=_e, logging_type=logging_type)
    except Exception:
        pass
    utils.logs.log(error=error, logging_type=logging_type)
    raise ValueError("%s" % error)
