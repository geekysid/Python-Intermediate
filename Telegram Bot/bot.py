from bottle import run, post, request as bottle_request
from Telegram_Bot import TelegramBot

@post('/')  # our python function based endpoint
def main():
    data = bottle_request.json  # extract all request data
    
    tgb = TelegramBot()
    
    tgb.convert_webhook_data(data)
    
    tgb.message_generator()
    

    # print('Hello')
    # print(data)


    return



if __name__ == '__main__':
    run(host='localhost', port=5000, debug=True)


# ./ngrok http 5000
