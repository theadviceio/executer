# -*- coding: utf-8 -*-
from cmd import Cmd
import sys
#import os
import signal
# pylint: disable=logging-not-lazy

__version__ = 1.0
__author__ = 'weldpua2008@gmail.com'

# pylint: disable=too-many-instance-attributes
class CLI_BASE(Cmd, object):

    """
    Help For CLI:

    Help may be requested at any point in a command by entering
    a question mark '?'.  If nothing matches, the help list will
    be empty and you must backup until entering a '?' shows the
    available options.
    Two styles of help are provided:
    1. Full help is available when you are ready to enter a
       command argument (e.g. 'show ?') and describes each possible
       argument.
    2. Partial help is provided when an abbreviated argument is entered
       and you want to know what arguments match the input
       (e.g. 'show pr?'.)
    """
    # pylint: disable=too-many-arguments
    def __init__(
            self,
            prompt="#",
            postloop_exit_msg="",
            history_size=300,
            intro="",
            using_readline=False,
            run_once=False):
        Cmd.__init__(self)
        if not using_readline:
            self.completekey = None
        self._hist = []
        # self.completekey=completekey
        self.postloop_exit_msg = None
        self.history_size = history_size
        self.intro = intro
        self.postloop_exit_msg = postloop_exit_msg
        self.prompt = prompt
        # self.completions=None
        self.setUp()
        self.using_readline = using_readline
        self.changes = []
        self._old_signal_handler = {}
        self._hist = []
        self._locals = {}
        self._globals = {}
        self.run_once = run_once

    def setUp(self):
        pass

    # pylint: disable=unused-argument
    def do_commit(self, args):
        """commit changes"""
        self.changes = []

    # pylint: disable=unused-argument
    def do_cancel(self, args):
        """Undo and cancel changes"""
        self.changes = []
    do_undo = do_cancel

    def _print_changes(self):
        if isinstance(self.changes, list):
            if len(self.changes) > 0:
                print "!!!You have uncommitted changes:!!!"
                for _changes in self.changes:
                    msg = _changes
                    if isinstance(_changes, dict):
                        if "desc" in _changes:
                            msg = _changes["desc"]
                    print " * %s" % msg
                print "-------"
                print "use 'commit' or 'discart' to commit them"

    def default(self, line):
        cmd, arg, line = self.parseline(line)
        cmds = self.completenames(cmd)
        num_cmds = len(cmds)

        if num_cmds == 1:
            getattr(self, 'do_' + cmds[0])(arg)
        elif num_cmds > 1:
            sys.stdout.write('%% Ambiguous command:\t"%s"\n' % cmd)
        else:
            # print self.command_alias
            if cmd in self.command_alias:
                el_alias = str(self.command_alias[cmd])
                getattr(self, el_alias)(arg)
            else:
                sys.stdout.write('% Unrecognized command\n')

    def emptyline(self):
        pass

    def do_help(self, args):
        """help on commands

        Usage:
        'help' or '?' with no arguments prints a list of commands for which help is available
        'help <command>' or '? <command>' gives help on <command>
        """
        Cmd.do_help(self, args)

    def do_history(self, args):
        """Print a list of last commands"""
        if args == "descr":
            print "History of commands:"
        if isinstance(self._hist, list):
            for _history in self._hist:
                print _history

    def preloop(self):
        """Initialization before prompting user for commands.

        Despite the claims in the Cmd documentaion, Cmd.preloop() is not a stub.
        """
        Cmd.preloop(self)  # # sets up command completion
        self._hist = []  # # No history yet
        self._locals = {}  # # Initialize execution namespace for user
        self._globals = {}

    def postloop(self):
        """Take care of any unfinished business.

        Despite the claims in the Cmd documentaion, Cmd.postloop() is not a stub.
        """
        Cmd.postloop(self)  # # Clean up command completion
        if self.postloop_exit_msg is not None:
            print "%s" % self.postloop_exit_msg

    def precmd(self, line):
        if line != '':
            if isinstance(self._hist, list):
                # print type(self.history_size)
                # if isinstance(self.history_size,(int,float)):

                if len(self._hist) > self.history_size:
                    del self._hist[0]
                self._hist += [line.strip()]
        if line.strip() == 'help':
            sys.stdout.write('%s\n' % self.__doc__)
            return ''
        cmd, arg, line = self.parseline(line)
        if arg == '?':
            cmds = self.completenames(cmd)
            if cmds:
                self.columnize(cmds)
                sys.stdout.write('\n')
            return ''
        return line

    def stop_handler(self, handler=None):
        if handler is None:
            handler = signal.SIGINT
        if not isinstance(self._old_signal_handler, dict):
            self._old_signal_handler = {}
        if handler in self._old_signal_handler:
            signal.signal(handler, self._old_signal_handler[handler])

    def start_handler(self, handler=None, _handler=None):
        if handler is None:
            handler = signal.SIGINT
        if _handler is None:
            _handler = self.sigint_handler

        if not isinstance(self._old_signal_handler, dict):
            self._old_signal_handler = {}
        try:
            self._old_signal_handler[handler] = signal.getsignal(handler)
            signal.signal(handler, _handler)
        except Exception as error:
            print "error add %s as signal.handler because %s" % (handler, error)

    # if user Did Ctrl-c we can ask her if break
    # signal.signal(signal.SIGINT,self.sigint_handler)
    def sigint_handler(self, f, z, msg="Press Y to exit without saving"):
        try:
            Exit = (str(raw_input(msg)))
            Exit = Exit.lower()
            if Exit == "y" or Exit == "yes":
                raise KeyboardInterrupt()
        except KeyboardInterrupt:
            signal.signal(signal.SIGINT, signal.SIG_DFL)
            raise KeyboardInterrupt()
        except RuntimeError:
            pass

    # pylint: disable=unused-argument
    def do_exit(self, e):
        """Exit to main CLI"""
        if not isinstance(self.changes, list):
            self.changes = []

        if len(self.changes) > 0:
            self._print_changes()
            running = True
            while running:
                Exit = (str(raw_input("Exit without saving ? Y/N")))
                if Exit == "Y" or Exit == "y":
                    return True
                if Exit == "N" or Exit == "n":
                    break

        else:
            return True
    do_quit = do_exit
