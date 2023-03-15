from mycroft import MycroftSkill, intent_file_handler


class CoffeeShop(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('shop.coffee.intent')
    def handle_shop_coffee(self, message):
        flavour = message.data.get('flavour')

        self.speak_dialog('shop.coffee', data={
            'flavour': flavour
        })


def create_skill():
    return CoffeeShop()

