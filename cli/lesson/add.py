
__version__ = 0.1
__author__ = 'weldpua2008@gmail.com'


class LessonAddCli(LessonCliBase):

    def add_lesson(self, hosts, newlesson, new_sublessons):
        try:
            self.lessonmodify.add_sublesson(
                hosts=hosts,
                lessons=newlesson,
                sublessons=new_sublessons)
            return True
        # pylint: disable=broad-except
        except Exception as error:
            print "%s " % error
            return False

    def _allowed_lessons(self):
        print "Please choose one lesson from allowed lessons:"
        for lesson in self.allowedlessons:
            print " - %s" % lesson

    # pylint: disable=unused-argument,too-many-locals
    def complete_add(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        args = mline.split()
        is_cached = True
        file_cache = self.lessonmodify.is_use_cache_config_lessons_data()
        self.allowedlessons = self.lessonmodify.get_only_lessons_list()
        if not file_cache:
            self.cache_add = {}
            is_cached = False

        self.completions_add = self.allowedlessons
        if len(args) > 0:
            lesson = args[0]

            if lesson in self.allowedlessons:
                if lesson in self.cache_add and is_cached:
                    self.completions_add = self.cache_add[lesson]
                else:
                    try:
                        sublessons, _ = self.lessonmodify.get_sublessons(lessonss=lesson)
                        keys = sublessons[lesson].keys()
                        if len(keys) > 0:
                            self.completions_add = []
                            for sublesson in keys:
                                self.completions_add.append("%s %s" % (lesson, sublesson))
                            self.cache_add[lesson] = self.completions_add
                    except Exception as error:
                        print "<ERROR> %s "% error

        offs = len(mline) - len(text)

        return [s[offs:] for s in self.completions_add if s.startswith(mline)]

#    complete_addSublessonsTo = complete_add
    def do_add(self, args):
        """add sublesson to lesson

        empty arguments -- List lessons
        lesson -- List sublessons of 'lesson'
        lesson sublesson -- Adding 'sublesson' to 'lesson'
        """
        thistype = self.lessonaddtype
        hosts = ["127.0.0.1"]
        _newlesson = None
        new_sublessons = None
        if not isinstance(args, basestring):
            args = ""
        _args = []
        if len(args) > 0:
            _args = args.split()

        if len(_args) == 0:
            self._allowed_lessons()
        elif len(_args) == 1:
            try:
                lesson = _args[0]
                sublessons, sublessons_and_playbooks = self.lessonmodify.get_sublessons(
                    lessonss=lesson)
                # print sublessons_and_playbooks
                if lesson in sublessons_and_playbooks:
                    print "You can add this sublessons and descriptions:"
                    print "---------------------"
                    if len(sublessons_and_playbooks[lesson]) < 1:
                        print "There aren't sublessons for %s " % lesson
                    for playbook in sublessons_and_playbooks[lesson]:
                        # print "-----: %s" % playbook
                        for sublesson in sublessons_and_playbooks[lesson][playbook]:
                            print "%s:" % sublesson
                            for sublessondescription in sublessons_and_playbooks[
                                    lesson][playbook][sublesson]:
                                print "     | %s" % (sublessondescription)

                else:
                    print sublessons, sublessons_and_playbooks
            # pylint: disable=broad-except
            except Exception as error:
                print "<error>%s" % error
        elif len(_args) == 2:
            if isinstance(self.changes, list):
                _newlesson = _args[0]
                new_sublessons = _args[1]
                sublessons, sublessons_and_playbooks = self.lessonmodify.get_sublessons(
                    lessonss=_newlesson)
                desc = "Unexpected Error"
                if new_sublessons not in sublessons[_newlesson]:
                    desc = "For lesson %s are only allowed: %s" % (
                        _newlesson, sublessons[_newlesson].keys())
                    desc = desc.replace("'", "")

                if len(sublessons[_newlesson]) < 1:
                    desc = "No such lesson %s" % (_newlesson)

                if new_sublessons in sublessons[_newlesson]:
                    desc = "Sublesson will %s append to lesson %s \n " \
                           "commit changes with 'commit' or 'save'" % (
                               _newlesson, new_sublessons)
                    self.changes.append({"type": thistype,
                                         "lesson": _newlesson,
                                         "sublesson": {_newlesson: [new_sublessons]},
                                         "desc": desc,
                                         "hosts": hosts})
                print desc
        else:
            print "not support syntax '%s'\n Please use 'add lesson sublesson'" % args

    #do_addSublessonsTo = do_add
