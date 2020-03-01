import os, json

file_path = os.path.dirname(os.path.abspath(__file__))
file_name = 'config.json'
file = os.path.join(file_path, file_name)

if os.path.isfile(file):
    with open(file, 'r') as f:
        data = json.load(f)
        TOKEN = data['TOKEN']
        NGROK_URL = data['NGROK_URL']
        API_KEYS = data['CoinMarketCap_API']
else:
    TOKEN = ''
    NGROK_URL = ''

BASE_TELEGRAM_URL = 'https://api.telegram.org/bot{}'.format(TOKEN)
LOCAL_WEBHOOK_ENDPOINT = '{}/webhook'.format(NGROK_URL)
TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_URL, LOCAL_WEBHOOK_ENDPOINT)
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_URL + '/sendMessage?chat_id={}&text={}&parse_mode={}'

BASE_CMC_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
CMC_API_KEYS = API_KEYS


