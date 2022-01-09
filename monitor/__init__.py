import textwrap

from telethon import TelegramClient, events, tl
import yaml


def main():
    with open("./credentials.yaml") as f:
        credentials = yaml.safe_load(f)

    api_id = credentials['api_id']
    api_hash = credentials['api_hash']
    print(80 * '-')
    print('Monitoring...')
    with TelegramClient('user', api_id, api_hash) as client:
        client.add_event_handler(new_message, events.NewMessage)
        client.loop.run_forever()


async def new_message(event):
    message = event.message
    print(80 * '-')
    chat = await message.get_chat()
    chat_title = 'Unknown chat_title'
    if isinstance(chat, tl.types.User):
        if chat.is_self:
            chat_title = 'Me'
        else:
            chat_title = f'{chat.first_name} {chat.last_name}'
    elif isinstance(chat, tl.types.Chat) or isinstance(chat, tl.types.Channel):
        chat_title = chat.title

    sender = await message.get_sender()
    sender_title = 'Unknown sender'
    if isinstance(sender, tl.types.User):
        if sender.is_self:
            sender_title = 'Me'
        else:
            sender_title = f'{sender.first_name} {sender.last_name}'
    elif isinstance(sender, tl.types.Channel):
        sender_title = sender.title

    print(f'{message.date:%Y-%m-%d, %H:%M:%S}: {chat_title}')
    print(f'From: {sender_title}')
    print(
        '\n'.join(
            textwrap.wrap(
                message.message, width=80, replace_whitespace=False,
                drop_whitespace=False
            )
        )
    )
