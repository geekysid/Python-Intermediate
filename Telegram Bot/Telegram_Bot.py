import requests
from config_data import TELEGRAM_SEND_MESSAGE_URL

class TelegramBot:

    def __init__(self):
        """
            Initializes all instances of the Telegrambot Class

            Attributes:
                chat_id:str: Chat ID of the Telegram chat, used to identify which conversation
                    outgoing message should be sent to.
                incoming_message_text:str: message of the Telegram chat
                first_name:str: First Name of the user who sent the message
                last_name:str: Last Name of the user who sent the message
        """

        self.chat_id = None
        self.incoming_message_text = None
        self.outgoing_message_text = None
        self.first_name = None
        self.last_name = None

    # {'update_id': 506185193, 'message': {'message_id': 9, 'from': {'id': 406450196, 'is_bot': False, 'first_name': 'Weird', 'last_name': 'Gambler', 'username': 'siddhantshah', 'language_code': 'en'}, 'chat': {'id': 406450196, 'first_name': 'Weird', 'last_name': 'Gambler', 'username': 'siddhantshah', 'type': 'private'}, 'date': 1582819558, 'text': 'This is a test message'}}
    def convert_webhook_data(self, data):
        """
            Recives data received from webhook in the form of Json and sets class variables

            Args:
                data:str: Json string of data
        """

        message = data['message']

        self.chat_id = message['chat']['id']
        self.incoming_message_text = message['text'].lower().strip()
        self.first_name = message['from']['first_name']
        self.last_name = message['from']['last_name']


    def message_generator(self):
        """
            Generating text and sending as reply to the user depending on the messages received from user

            Returns:
                bool: True if message was sent to user successfully else False
        """

        success = None

        if len(self.incoming_message_text) > 0:
            # evaluating condition if the message sent to bot is a command
            if self.incoming_message_text[0] == '/':
                self.command_reply()
                success = self.send_message()
            else:
                success = True
        else:
            success = True
        
        return success


    def command_reply(self):
        """
            Generating reply depending on the message received
        """

        if len(self.incoming_message_text) > 0:
            message = self.incoming_message_text.split(' ')

            if message[0] == '/hello':
                self.outgoing_message_text = 'Hey mate... Nice to see you...'
            elif message[0] == '/help':
                self.outgoing_message_text = ''\
                        '**Price of Coin**:\n/p coinSymbol currency\nEx: /p BTC INR'\
                        '\n\n'\
                        '**Market Cap of Coin**:\n/mc coinSymbol\nEx: /mc BTC'
            else:
                self.outgoing_message_text = 'Buddy thats not a valid command... Type /help to know all the services I provide..'


    def send_message(self):
        """
            Sends message to Telegram
            Returns:
                True of message successfully sent else false
        """

        resp = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(self.chat_id, self.outgoing_message_text))

        return True if resp.status_code == 200 else False