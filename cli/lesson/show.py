


__version__ = 0.1
__author__ = 'weldpua2008@gmail.com'


class LessonShowCli(LessonListCli):

    # pylint: disable=unused-argument
    def complete_show(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        args = mline.split()
        self.showlessons = []

        curr_lessons = self.Lessonlessonget.get_cur_sublessons()
        # print curr_lessons
        if isinstance(curr_lessons, dict):
            self.showlessons = curr_lessons.keys()

        self.completions_show = self.showlessons
        if len(args) > 0:
            lesson_for_complete = args[0]
            if lesson_for_complete in self.showlessons:
                sublessons, _ = self.Lessonlessonget.get_sublessons(
                    lessonss=lesson_for_complete)
                keys = sublessons[lesson_for_complete].keys()

                if len(keys) > 0:
                    self.completions_show = []
                    for sublesson in keys:
                        self.completions_show.append(
                            "%s %s" % (lesson_for_complete, sublesson))
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.completions_show if s.startswith(mline)]

    complete_showless = complete_show

   
    def _show(self, args, full_output):
        self._print_changes()
        _args = args.split()
        curr_sublessons_and_lessons = self.Lessonlessonget.get_cur_sublessons()
        try:
            header = "Current Lesson lessons:"
            entered_sublesson = []
            if len(_args) > 0:
                entered_lesson = _args[0]
                if entered_lesson in curr_sublessons_and_lessons:
                    curr_sublessons_and_lessons = {
                        entered_lesson: curr_sublessons_and_lessons[entered_lesson]}

                    if len(_args) == 2:
                        entered_sublesson = _args[1]
                        curr_sublessons_and_lessons = {
                            entered_lesson: [entered_sublesson]}

                else:
                    header = "Please provide right lesson!"
                    curr_sublessons_and_lessons = {}

            print header
            for lesson in curr_sublessons_and_lessons:
                print "%s:" % lesson
                sublessons = curr_sublessons_and_lessons[lesson]
                if len(entered_sublesson) > 0:
                    sublessons = entered_sublesson
                description = self.Lessonlessonget.get_sublesson_descr(
                    lesson=lesson,
                    sublessons=sublessons)
                for sublesson_in_descr in description:
                    print "   %s:" % sublesson_in_descr
                    for sublesson_descr in description[sublesson_in_descr]:
                        print "      - %s" % sublesson_descr

        # pylint: disable=broad-except
        except Exception as error:
            print "<ERROR>Can't show lesson: %s" % error

    def do_show(self, args):
        """show lesson details

        'show' with no arguments prints a list of current lessons
        'show all'  prints current lessons and description
        'show' [lesson] [sublesson] show lesson/sublesson details
        """
        try:
            self._show(args=args, full_output=True)
        except Exception as error:
            print "<ERROR>%s" % error

    # def do_showless(self, args):
    #     """show lesson details
    #
    #     'show' with no arguments prints a list of current lessons
    #     'show all'  prints current lessons and description
    #     'show' [lesson] [sublesson] show lesson/sublesson details
    #     """
    #     try:
    #         self._show(args=args, full_output=False)
    #     except Exception as error:
    #         print "<ERROR>%s" % error
