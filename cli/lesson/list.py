from api.cli.lessons import lessonCliBase


__version__ = 0.1
__author__ = 'weldpua2008@gmail.com'


class LessonListCli(lessonCliBase):

    def do_list(self, args, full=True):
        """list lessons

        list lessons - list of all sllowed Sublesson
        list lesson sublesson sublesson1 - list of sublesson1, sublesson2 and descriptions
        """
        try:
            desc = "No such %s" % args
            if not isinstance(args, basestring):
                args = ""
            _args = args.split()
            lesson = None
            sublessons = {}
            sublessonsnotexists = []
            if len(_args) == 0:
                desc = "Please write lesson"
            elif len(_args) > 0:

                lesson = _args[0]
                argsublessons = _args[1:]
                if not isinstance(argsublessons, list):
                    argsublessons = []
                sublessons, _ = self.lessonget.get_sublessons(lessonss=lesson)

                keys = sublessons[lesson].keys()
                for _sublessons in keys:
                    if _sublessons not in argsublessons and len(argsublessons) > 0:
                        del sublessons[lesson][_sublessons]
                for _sublessons in argsublessons:
                    if _sublessons not in sublessons[lesson]:
                        #sublessons[lesson][_sublessons]=["No such sublesson %s" % _sublessons]
                        sublessonsnotexists.append(_sublessons)
                #desc = "%s" % lesson
                # for _lesson in sublessons.keys():
                #    desc+="  %s"  % _lesson
                desc = ""
                for lesson in sublessons:
                    if len(sublessons[lesson]) > 0:
                        desc += "%s:\n" % lesson
                        for sublesson in sublessons[lesson]:
                            if full is True:
                                desc += " %s:\n" % sublesson
                                for description in sublessons[lesson][sublesson]:
                                    desc += "     %s\n" % description
                            else:
                                desc += " %s\n" % sublesson
                        if len(sublessonsnotexists) > 0:
                            desc += " Non-exist sublessons: %s\n" % sublessonsnotexists

                    else:
                        desc += "No such lesson %s:\n" % lesson
            print desc
        # pylint: disable=broad-except
        except Exception as error:
            print "<ERROR>Can't list: %s" % error

    # pylint: disable=unused-argument, redefined-outer-name
    def complete_list(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        args = mline.split()

        self.allowedlessons = self.lessonget.get_only_lessons_list()
        self.completions_list = self.allowedlessons
        if len(args) > 0:
            lesson = args[0]
            if lesson in self.allowedlessons:

                sublessons, _ = self.lessonget.get_sublessons(lessonss=lesson)
                keys = sublessons[lesson].keys()

                if len(keys) > 0:
                    self.completions_list = []
                    for sublesson in keys:
                        self.completions_list.append("%s %s" % (lesson, sublesson))
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.completions_list if s.startswith(mline)]
