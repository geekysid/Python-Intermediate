import requests
from config_data import TELEGRAM_SEND_MESSAGE_URL
from Crypto_Data import CryptoCoinInformation

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
        try:
            self.incoming_message_text = message['text'].lower().strip()
        except:
            self.incoming_message_text = ''
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

            if message[0] == '/p':
                self.outgoing_message_text = self.get_crypto_data(message, '/p')
            elif message[0] == '/pc':
                self.outgoing_message_text = self.get_crypto_data(message, '/pc')
            elif message[0] == '/help_pc':
                self.outgoing_message_text = self.get_crypto_data(message, '/help_pc')
            elif message[0] == '/help_p':
                self.outgoing_message_text = self.get_crypto_data(message, '/help_p')
            elif message[0] == '/help':
                self.outgoing_message_text = ''\
                        '<b>Price of Coin</b>:\n/p coinSymbol\nEx: /p BTC'\
                        '\n\n'\
                        '<b>Price of Coin wrt to other Currency</b>:\n/pc numberOfCoin coinSymbol currencySymbol\nEx: /pc 1 BTC ETH\nEx: /pc 1 BTC USD'
            else:
                self.outgoing_message_text = 'Buddy thats not a valid command... Type /help to know all the services I provide..'


    def get_crypto_data(self, message, command):
        
        token = ''
        number_of_token = ''
        base_currency = None

        if command == '/p':
            if len(message) < 3:
                if len(message) > 1:
                    token = message[1].upper()
                else: 
                    return 'Not a Valid Command. Token not provided.\nEnter <b>/help_p</b> to know the proper command.'
                
                crypto_inf = CryptoCoinInformation(token)
                return crypto_inf.fetch_crypto_price()
            else:
                return 'Not a Valid Command. Too many inputs.\nEnter <b>/help_p</b> to know the proper command.'


        elif command == '/pc':
            if len(message) < 5:
                if len(message) > 1:
                    number_of_token = message[1]
                    if not number_of_token.isnumeric():
                        return f'"{number_of_token}" is not a Number.\nEnter <b>/help_pc</b> to know the proper command.'
                else: 
                    return 'Not a Valid Command. Number of Token not provided.\nEnter <b>/help_pc</b> to know the proper command.'
                if len(message) > 2:
                    token = message[2].upper()
                else: 
                    return 'Not a Valid Command. Token not provided.\nEnter <b>/help_pc</b> to know the proper command.'
                if len(message) > 3:
                    base_currency = message[3].upper()
                else: 
                    return 'Not a Valid Command. Base Currencries not provided.\nEnter <b>/help_pc</b> to know the proper command.'
                
                crypto_inf = CryptoCoinInformation(token, base_currency=base_currency, number_of_token=number_of_token)
                return crypto_inf.fetch_price_conversion()

        elif command == '/help_p':
            string = '/p --> Used to know price of a Token/Coin wrt USD\n'\
                        'command --> <b>/p {1}</b>\n'\
                        '{1} --> Symbol of token/con whose price is to be predicted\n'\
                        'eg:\n/p btc\n/p eth'

            return string

        elif command == '/help_pc':
            string = '/pc --> Used to know price of a Token/Coin wrt fiat or other crypto currencies\n'\
                        'command --> <b>/pc {1} {2} {3}</b>\n'\
                        '{1} --> number of tokens\n'\
                        '{2} --> Symbol of token/con whose price is to be predicted\n'\
                        '{3} --> Symbol of currency wrt to which price is to be determined\n'\
                        'eg:\n/pc 10 btc usd\n/pc 5 eth btc\n/pc 10 btc eth\n/pc 10 btc nex\n'

            return string

        else:
            return 'Sorry To many inputs....\nEnter <b>/help</b> to know the all commands.'


    def send_message(self):
        """
            Sends message to Telegram
            Returns:
                True of message successfully sent else false
        """

        resp = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(self.chat_id, self.outgoing_message_text, 'HTML'))

        return True if resp.status_code == 200 else False