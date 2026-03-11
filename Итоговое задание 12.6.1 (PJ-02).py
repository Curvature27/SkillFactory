import telebot
import requests
import json

from configuration_data import TOKEN, currencies
from utilities import ConversionException, data_checking

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def instruction(message: telebot.types.Message):
    instructions = 'сначала напиши сколько у тебя этого есть\n' \
                   'потом что это у тебя такое\n' \
                   'и в конце что тебе собственно надо.\n' \
                   '- одним сообщением ! - \n' \
                   'например:\n' \
                   '1 доллар рубль\n\n' \
                   'а чтоб я показал что есть у меня\n' \
                   'нажми /currencies'
    bot.reply_to(message, instructions)


@bot.message_handler(commands=['currencies'])
def list_currencies(message: telebot.types.Message):
    list_names = []
    for key in currencies.keys():
        list_names.append(key)
    bot.reply_to(message, "У меня есть:\n" + ", ".join(list_names))


@bot.message_handler(content_types=['text'])
def conversion(message: telebot.types.Message):
    try:
        input_data = message.text.split()
        if len(input_data) > 3:
            raise ConversionException("получены лишние вводные")
        elif len(input_data) < 3:
            raise ConversionException("чегото не хватает")

        amount, quote, base = input_data
        data_checking(quote, base, amount)
        res = requests.get(f"https://min-api.cryptocompare.com/data/price?"
                           f"fsym={currencies[quote]}&tsyms={currencies[base]}")
        if "," in amount:
            amount = amount.replace(",", ".")
        conversion_result = json.loads(res.content)[currencies[base]] * float(amount)
    except ConversionException as e:
        bot.reply_to(message, f"{e}")
    except Exception as e:
        bot.reply_to(message, f"что-то пошло не так\n{e}")
    else:
        answer = f"у тебя было {amount} {quote} теперь будет {round(conversion_result, 2)} {base}"
        bot.send_message(message.chat.id, answer)


bot.polling()
