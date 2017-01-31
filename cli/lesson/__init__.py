import conf
from cli.icli import CLI_BASE

__version__ = 0.1
__author__ = 'weldpua2008@gmail.com'


# pylint: disable=too-many-instance-attributes
class LessonCliBase(CLI_BASE):

    def setUp(self):
        self.showlessons = []
        self.roleaddtype = "append"
        self.roledeltype = "delete"
        self.completions_del = []
        self.assign_lessons = []
        self.completions_show = []
        kwargs = {
            "config_path": conf.lesson.PATH
            }

        # self.lessondel = DeleteLesson(**kwargs)
        # self.lessonmodify = ModifyLesson(**kwargs)
        self.lessonget = GetLesson(**kwargs)

        self.completions_list = []
        self.completions_del = []
        self.assign_lessons = []
        self.completions_add = []
        # setUp cliases for cmd
        self.command_alias = {}
        self.allowedlessons = self.lessonget.lessons_list()
        self.completions_add = self.allowedlessons
        self.cache_add = {}
        #self.cache_changed = False

