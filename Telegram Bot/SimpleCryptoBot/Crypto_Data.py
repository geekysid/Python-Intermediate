import requests
import os, json
from config_data import CMC_API_KEYS, BASE_CMC_URL
from random import choice

class CryptoCoinInformation:

    def __init__(self, token, base_currency='USD', number_of_token=1):
        """
            Initializes all instances of the Telegrambot Class

            Attributes:
                token:str: symbol of token whose data is to be fetched
                current_price:float: current price of coin
                change_in_24_hours:float: change in price of token in last 24 hours.
                change_in_7_days:float: change in price of token in last 7 days.
                API_KEY:list: list of api keys of cmc
                base_currency:str: currency into against which conversion is done
                number_of_token:int: number of tokens
            Args:
                token:str: symle of token enquired
        """
        self.token = token
        self.current_price = 0.0
        self.change_in_24_hours = 0.0
        self.change_in_7_days = 0.0
        self.API_KEY = None
        self.base_currency = base_currency
        self.number_of_token = number_of_token


    def get_params_crypto_price(self):
        """
            Evaluates parameters to be passed depending on value of base_currency
        """
        if self.base_currency is not None:
            params = {'symbol':self.token, 'convert': self.base_currency}
        else:
            params = {'symbol':self.token.upper()}
        return params


    def get_api_Keys(self):
        """
            Selectes api key from a list.
        """
        if len(CMC_API_KEYS) > 0:
            api_key = choice(CMC_API_KEYS)
        else:
            api_key = None

        return api_key
        

    def fetch_crypto_price(self):
        """
            Makes api call to the CMC api ad gets the data
        """
        while True:
            api_key = self.get_api_Keys()

            if api_key is not None:

                headers = {
                    'Accepts': 'application/json',
                    'X-CMC_PRO_API_KEY': api_key,
                    }
                
                resp = requests.get(BASE_CMC_URL, headers=headers, params=self.get_params_crypto_price())

                if resp.status_code == 200:
                    return self.price_data_display(json.loads(resp.text))
                    break
                elif resp.status_code == 429:
                    print('Daily Quota Exhausted')
                else:
                    return self.error_messagae(resp)
                    break
            else:
                print('All APIS used')


    def price_data_display(self, data):
        if data['status']['error_message'] == None or data['status']['error_message'] == '':
            result = data['data'][self.token.upper()]
            token_short = result['symbol']
            token_long = result['name']
            try:
                mineable = 'Mineable' if result['tags'][0] == 'mineable' else 'Not Mineable'
            except:
                mineable = 'Not Mineable'
            circulating_supply = str(result['circulating_supply'])
            cmc_rank = str(result['cmc_rank'])
            base_currency = list(result['quote'].keys())[0]
            price = str(result['quote'][base_currency]['price'])
            volume_24h = str(result['quote'][base_currency]['volume_24h'])
            percent_change_1h = str(result['quote'][base_currency]['percent_change_1h'])
            percent_change_24h = str(result['quote'][base_currency]['percent_change_24h'])
            percent_change_7d = str(result['quote'][base_currency]['percent_change_7d'])
            market_cap = str(result['quote'][base_currency]['market_cap'])

            # display_str s
            display_str1 = f'<b>Coin</b>: {token_long} - {token_short} ({mineable})\n'
            display_str2 = f'<b>Price</b>: {price} {base_currency} | CMC Rank: {cmc_rank}\n'
            display_str3 = f'<b>Market Cap</b>: {market_cap} {base_currency}\n'
            display_str4 = f'<b>24 Hr Vol</b>: {volume_24h} {base_currency}\n'
            display_str5 = f'<b>1 Hour</b>: {percent_change_1h}%\n'
            display_str6 = f'<b>24 Hour</b>: {percent_change_24h}%\n'
            display_str7 = f'<b>7 Days</b>: {percent_change_7d}%\n'
            
            return display_str1+display_str2+display_str3+display_str4+display_str5+display_str6+display_str7
            
        else:
            return f'Error occured. {data["status"]["error_message"]}.\nPlease contact @siddhantshah to get this fixed.'
    

    def fetch_price_conversion(self):
        """
            Represents price of token into diffrent currencies which are passed as a comma separated string
            Here class variable token, represents token whose price is to be determined and class variable 
            base_currency represents one or more currency (comma separated) wrt which price is to be determined
            and another class variable number_of_token represents total number of token.
        """
        while True:
            api_key = self.get_api_Keys()

            if api_key is not None:

                headers = {
                    'Accepts': 'application/json',
                    'X-CMC_PRO_API_KEY': api_key
                }

                parameters = {
                    'symbol': self.token,               # 'symbol':'1',
                    'amount': self.number_of_token,     # 'amount':'50',
                    'convert': self.base_currency       # 'convert':'GPB,LTC,USD'
                }

                url = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion'

                resp = requests.get(url, headers=headers, params=parameters)
                
                if resp.status_code == 200:
                    return self.price_conversion_data_display(json.loads(resp.text))
                    break
                elif resp.status_code == 429:
                    print('Daily Quota Exhausted')
                else: 
                    return self.error_messagae(resp)
                    break


    def price_conversion_data_display(self, json_data):
        """
            Compute data received from fetch_price_conversion() and fetch the required output and 
            returns string that represents the output.
        """

        if json_data['status']['error_message'] == None or data['status']['error_message'] == '':
            result = json_data['data']
            token_short = result['symbol']
            token_long = result['name']
            number_of_token = result['amount']
            last_updated = result['last_updated']
            quotes = result['quote']
            conversion = []
            for quote in quotes:
                conversion.append((quote, quotes[quote]['price'], quotes[quote]['last_updated']))

            # display_str s
            display_str1 = f'<b>Coin</b>: {token_long} - {token_short}\n'
            display_str2 = ''
            for (currency, price, last_updated) in conversion:
                display_str2 = f'{number_of_token} {token_short} = {price} {currency}\n'
            display_str3 = f'<b>Last Updated</b>: {last_updated}'

            return display_str1+display_str2+display_str3
        else:
            return f'Error occured. {data["status"]["error_message"]}.\nPlease contact @siddhantshah to get this fixed.'


    def error_messagae(self, resp):
        print(resp.url)
        print(resp.status_code)
        data = json.loads(resp.text)
        if len(data['status']['error_message']) > 1:
            return data['status']['error_message']
        else:
            return json.dumps(data, indent=4)
