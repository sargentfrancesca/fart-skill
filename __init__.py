from mycroft import MycroftSkill, intent_file_handler


class Fart(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('fart.intent')
    def handle_fart(self, message):
        typeof = message.data.get('typeof')

        self.speak_dialog('fart', data={
            'typeof': typeof
        })


def create_skill():
    return Fart()

