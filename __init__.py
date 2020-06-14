from mycroft import MycroftSkill, intent_file_handler
from mycroft.messagebus import message
from mycroft.skills.audioservice import AudioService

class FirstTestSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self): 
        self.setting_mp3_path = self.settings.get('path_for_mp3')
        self.audio_service = AudioService(self.bus)

    @intent_file_handler('test.first.intent')
    def handle_test_first(self, message):
        
        settingTxt = "Settings is set to " + self.setting_mp3_path
        self.speak(settingTxt)

        self.audio_service.play(self.setting_mp3_path)

        self.speak_dialog('test.first')
        


def create_skill():
    return FirstTestSkill()

def stop(self):
    pass

