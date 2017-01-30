import threading
import os
#  Cache that depend's on file modification time


__version__ = "1.0.0"
__author__ = 'weldpua2008@gmail.com'

# store cache data
__cache_store = {}
__lock = threading.Lock()
ttl = 86400
# # store file access time
# __cache_file_store = {}
# pylint: disable=logging-not-lazy



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


def get_cache_copy():
    """getting __cache_store"""
    global __cache_store
    if isinstance(__cache_store, dict):
        return __cache_store.copy()
    elif isinstance(__cache_store, list):
        return __cache_store[:]
    else:
        return __cache_store

def get(key=None, cache_type=None, file_path=None, ttl=None):
    """Get cache or raise Error"""
    global __cache_store
    # global __TTL
    # __ttl = ttl
    # if ttl is None:
    #     ttl = __TTL
    value = None
    #getted = False
    try:
        with __lock:
            if cache_type in __cache_store:
                if key in __cache_store[cache_type]:
                    if file_path in __cache_store[cache_type][key]:
                        if 'value' and 'access_time' in __cache_store[cache_type][key][file_path]:
                            access_time = __cache_store[cache_type][key][file_path]['access_time']
                            if os.path.exists(file_path):
                                statbuf = os.stat(file_path)
                                if statbuf.st_mtime == access_time:
                                    value = __cache_store[cache_type][key][file_path]['value']
    except TypeError:
        # if key has unhashable type
        pass
    except Exception as error:
        raise NotFoundError(" Can't get key: %s type: %s because %s " % (key, cache_type, error))


    return value


def update(key=None, value=None, cache_type=None, file_path=None):
    """Set the cache that depends on the file access time
    :param key: the key for the cache
    :param value: the value in the cache
    :param cache_type: when we are using cache in different modules this param
            can protects from the overradings
    :param file_path: path to the file
    :return: True - if cache was setted successful
            False - cache wasn't setted successful
    """
    global __cache_store
    __was_set = False
    try:
        with __lock:
            if cache_type not in __cache_store:
                __cache_store[cache_type] ={}
            if key not in __cache_store[cache_type]:
                __cache_store[cache_type][key] = {}
            if file_path not in __cache_store[cache_type][key]:
                __cache_store[cache_type][key][file_path] = {
                    "access_time": None,
                    "value": None
                }
            if os.path.exists(file_path):
                statbuf = os.stat(file_path)
                __cache_store[cache_type][key][file_path]['access_time'] = statbuf.st_mtime
                __cache_store[cache_type][key][file_path]['value'] = value
                __was_set = True
    except TypeError:
        # if key has unhashable type
        pass
    except Exception as error:
        raise RuntimeError(" Can't set key: %s type: %s because %s " % (key, cache_type, error))
    return __was_set


def clear(key=None, cache_type=None, file_path=None):
    """Get cache or raise Error"""
    global __cache_store
    __was_deleted = None
    try:
        __was_deleted = False
        with __lock:
            if cache_type in __cache_store:
                if key in __cache_store[cache_type]:
                    if file_path in __cache_store[cache_type][key]:
                        del __cache_store[cache_type][key][file_path]
                    __was_deleted = True
    except Exception as error:
        __was_deleted = None
        raise RuntimeError(" Can't clear key: %s type: %s because %s " % (key, cache_type, error))
    return __was_deleted


def flush_cache():
    """Clear current cache
    :return: True if was flushed
    """
    global __cache_store
    __cache_store = {}
    return True
