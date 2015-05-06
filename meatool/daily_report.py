from datetime import date
from pyworksnaps import Worksnaps
from datetime import timedelta
from collections import defaultdict
from decouple import config
import logging
from cliff.command import Command


class SendReport(Command):
    """Command to generate and send a daily report"""

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.log.info('sending greeting')
        self.ws = Worksnaps(config('WORKSNAPS_TOKEN'))

        comments = self.get_ws_comments()
        self.log.info(self.format_ws_comments(comments))

    @property
    def today(self):
        return date.today()

    @property
    def tomorrow(self):
        return self.today + timedelta(days=1)

    def get_ws_comments(self):
        coments_per_task_per_project = defaultdict(
            lambda: defaultdict(lambda: defaultdict(list))
        )
        entry_filter = dict(
            start=self.today, end=self.tomorrow
        )
        for project in self.ws.projects():
            for entry in project.entries(**entry_filter):
                coments_per_task_per_project[
                    project.name
                ][entry.task_name][entry.user_comment].append(
                    entry.duration_in_minutes
                )
        return coments_per_task_per_project

    def format_ws_comments(self, coments_per_task_per_project, with_time=False):
        result = []

        def format_single_comment_with_time(task, comment, minutes_list):
            return ' - {task}: {comment} - {minutes};'.format(
                task=task, comment=comment,
                minutes=sum(map(int, minutes_list))
            )

        def format_single_comment_without_time(task, comment, _):
            return ' - {task}: {comment};'.format(
                task=task, comment=comment
            )

        if with_time:
            format_single_comment = format_single_comment_with_time
        else:
            format_single_comment = format_single_comment_without_time

        for project_k, project_v in coments_per_task_per_project.iteritems():
            result.append(project_k)

            for task_k, task_v in project_v.iteritems():
                for comment_k, comment_v in task_v.iteritems():
                    result.append(format_single_comment(
                        task_k, comment_k, comment_v
                    ))
        return '\n'.join(result)

    def get_parser(self, prog_name):
        parser = super(SendReport, self).get_parser(prog_name)
        return parser
