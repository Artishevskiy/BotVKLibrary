import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random

hellos = ['Привет', 'привет', 'прив', 'ку', 'ку', 'здаров', 'здарова', 'q', 'куку', 'ку-ку', 'здравствуйте', 'здравствуй']


def main():
    vk_session = vk_api.VkApi(
        token='64f7d38df6cbac49f2146d5037a93647b83f9897e355478551f3bee2d393cc2a8f57aefd5803bf5b88750')
    longpoll = VkBotLongPoll(vk_session, 203632426)
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()
            ID = event.obj.message['from_id']
            response = vk.users.get(user_ids=ID)
            first_name = response[0]['first_name']
            last_name = response[0]['last_name']
            txt_msg = event.obj.message['text']
            vk.messages.send(user_id=ID,
                             message=first_name + ' ' + last_name,
                             random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()