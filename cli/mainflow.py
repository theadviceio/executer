# -*- coding: utf-8 -*-
# pylint: disable=logging-not-lazy,no-self-use
CLI_PROMT = '#'
LESSON_PROMT = ':Lesson>'

import sys
#import os
# sys.path.append(
#    os.path.dirname(os.path.dirname(os.path.realpath(__file__)) ))

from icli import CLI_BASE
from lesson import LessonCli
import signal

__version__ = 1.0
__author__ = 'weldpua2008@gmail.com'

class EXECUTERCli(CLI_BASE):

    """CLI Help:

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

    def default(self, line):
        cmd, arg, line = self.parseline(line)
        cmds = self.completenames(cmd)
        num_cmds = len(cmds)
        if num_cmds == 1:
            getattr(self, 'do_' + cmds[0])(arg)
        elif num_cmds > 1:
            sys.stdout.write('%% Ambiguous command:\t"%s"\n' % cmd)
        else:
            sys.stdout.write('% Unrecognized command\n')

    # pylint: disable=unused-argument
    def do_lesson(self, run_once_str):
        """manage lesson role"""
        # completekey=self.completekey
        prompt = self.prompt[:-1] + LESSON_PROMT
        postloop_exit_msg = ""
        history_size = 300
        intro = ""
        lesson_instance = LessonCli(
            using_readline=self.using_readline,
            prompt=prompt,
            postloop_exit_msg=postloop_exit_msg,
            history_size=history_size,
            intro=intro,
            run_once=self.run_once)
        try:
            if self.run_once:
                lesson_instance.onecmd(run_once_str)
            else:
                lesson_instance.cmdloop()
        except KeyboardInterrupt:
            print "Exit from role..."
        # clean changes by signal
        signal.signal(signal.SIGINT, signal.SIG_DFL)    

    # pylint: disable=unused-argument
    def do_about(self, run_once_str):
        """Show about information"""
        print """
    theadvice.io CLI provides following benefits to be used throughout on-premise:
        * Easy management of your progress
        """

    def do_exit(self, run_once_str):
        """Exit from CLI"""
        return True
    #do_EOF = do_exit
    do_quit = do_exit
