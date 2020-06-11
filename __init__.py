from mycroft import MycroftSkill, intent_file_handler


class FirstTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.first.intent')
    def handle_test_first(self, message):
        self.speak_dialog('test.first')


def create_skill():
    return FirstTest()

