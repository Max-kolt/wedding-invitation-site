import requests
from config import tg_config, logger
from schema import GuestSchema


def send_to_chat(data: GuestSchema):
    response = requests.post(
        url='https://api.telegram.org/bot{0}/{1}'.format(tg_config.TOKEN, 'sendMessage'),
        data={
            'chat_id': tg_config.CHAT_ID,
            'text': f"{data.name}\n"
                    f"{'Будет' if data.present else 'Не сможет'}\n"
                    f"{'Хочет быть в загсе' if data.marry else 'Пропустит регистрацию'}\n"
                    f"{'Хочет второй день' if data.twoday else 'Не хочет второй день'}\n"
                    f"{data.food}\n"
        }
    ).json()

    logger.info(response)

