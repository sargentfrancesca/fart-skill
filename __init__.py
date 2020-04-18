from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.audioservice import AudioService
import os


class Fart(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
    
    def initialize(self):
        self.audio_service = AudioService(self.bus)


    @intent_file_handler('fart.intent')
    def handle_fart(self, message):
        typeof = message.data.get('typeof')

        directory = os.path.dirname(os.path.realpath(__file__))

        self.log.info(directory)

        self.audio_service.play(f'file://{directory}/fart_sample.wav')

        self.speak_dialog('fart', data={
            'typeof': typeof
        })


def create_skill():
    return Fart()

