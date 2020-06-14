from mycroft import MycroftSkill, intent_file_handler
from mycroft.messagebus import message


class FirstTestSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self): 
        my_setting = self.settings.get('my_setting')

    @intent_file_handler('test.first.intent')
    def handle_test_first(self, message):
        self.speak_dialog('test.first')


def create_skill():
    return FirstTestSkill()

def stop(self):
    pass

