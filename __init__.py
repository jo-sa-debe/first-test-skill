from mycroft import MycroftSkill, intent_file_handler
from mycroft.messagebus import message
from mycroft.skills.audioservice import AudioService


class FirstTestSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self): 
        my_setting = self.settings.get('my_setting')
        self.audioService = AudioService(self.bus)

    @intent_file_handler('test.first.intent')
    def handle_test_first(self, message):
        
        for backendval in AudioService.available_backends().values()
            self.speak(backendval)
            
        self.speak_dialog('test.first')
        


def create_skill():
    return FirstTestSkill()

def stop(self):
    pass

