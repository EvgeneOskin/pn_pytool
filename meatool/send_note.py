from pushbullet import Pushbullet
from decouple import config
import logging
from cliff.command import Command


class SendNote(Command):
    "A simple command that prints a message."

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.log.info('sending greeting')
        self.pb = Pushbullet(config('PUSHBULLET_TOKEN'))

	self.send_note(parsed_args.title, parsed_args.body)

    def send_note(self, title, body):
        self.pb.push_note(title, body)
	self.log.info('Sent')

    def get_parser(self, prog_name):
        parser = super(SendNote, self).get_parser(prog_name)
        parser.add_argument('-t', '--title', type=str)
        parser.add_argument('-b', '--body', type=str, default='')
        return parser
