import telebot
from binance.client import Client
import time

# API keys
api_key = 'api_key'
api_secret = 'api_secret'
API_TOKEN = 'API_TOKEN'
bot = telebot.TeleBot(API_TOKEN)
client = Client(api_key, api_secret)

print("Send /start command to the bot. It will automatically update (edit) it's message every *update_timer* seconds")

summ = 0.0


@bot.message_handler(commands='start')
def showprice(message):
    update_timer = 2 # (sec) how often the information will be updated
    new_result = ' '

    msg = bot.send_message(message.chat.id, f'{update_timer} sec...')
    while True:

        time.sleep(update_timer)

        uprftall = 0

        prices = client.futures_position_information()
        for i in range(len(prices)):
            position_amt = float((prices[i]['positionAmt']))

            if position_amt > float(0):

                symbol = str((prices[i]['symbol']))
                mark_price = str(round(float((prices[i]['markPrice'])), 3))
                unrealized_profit = str(round(float((prices[i]['unRealizedProfit'])), 3))
                liquidation_price = str(round(float((prices[i]['liquidationPrice'])), 3))
                uprftall += float(unrealized_profit)
                total = client.futures_account_balance()[6]['balance'][:7]

                if float(unrealized_profit) > float(0):
                    emj = '📈'
                else:
                    emj = '📉'
                new_result += (f'<b>▪️{str(symbol)}</b> ({str(mark_price)} USDT) '
                               f'\nProfit: {str(unrealized_profit)}{str(emj)}\n'
                               f'Liquidation price - {str(liquidation_price)}\n\n')
        last_result = f"{new_result}\nВсего: {total}  USDT"
        new_result = ' '

        if not last_result == msg.text:

            msg = bot.edit_message_text(last_result, msg.chat.id, msg.id, parse_mode='HTML')


bot.infinity_polling()
