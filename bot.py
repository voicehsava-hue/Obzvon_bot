import telebot

bot = telebot.TeleBot('8321837734:AAHhrlBFMQO8-4bbSkwd52Saf_vVVDMldHw')

TARGET_CHAT_ID = '-1002901497821'
MESSAGE_THREAD_ID = '19'


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f"Список команд:\n/start\n/all\n/starosta", parse_mode='MarkdownV2')

@bot.message_handler(commands=['all'])
def main(message):
    msg = bot.send_message(message.chat.id, '@austriackiiPingwin'
                                            '\n@EROS625'
                                            '\n@MrPr1de'
                                            '\n@bequiteanddriive'
                                            '\n@Иван'
                                            '\n@Lexa2513'
                                            '\n@Iirit22'
                                            '\n@Reshetov111'
                                            '\n@MaximumPulse3566'
                                            '\n@vladkaqk'
                                            '\n@Sok_D0bri'
                                            '\n@Xepneon'
                                            '\n@iZanchixk'
                                            '\n@VASYYYYYYYYYa'
                                            '\n@strekoza_20'
                                            '\n@M888EF'
                                            '\n@plinkisx'
                                            '\n@utxpftphpx'
                                            '\n@shev4iks'
                                            '\n@Max1mWW'
                                            '\n@edgar_k4'
                                            '\n@thing_man'
                                            '\n@Andromeda124')
    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text='Люди')

@bot.message_handler(commands=['starosta'])
def main(message):
    msg = bot.send_message(message.chat.id, '@austriackiiPingwin @MrPr1de')
    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text='|Старосты')










@bot.message_handler(func=lambda message: True)
def echo_message(message):
    chat_id = message.chat.id
    try:
        msg_thread_id = message.reply_to_message.message_thread_id
    except AttributeError:
        msg_thread_id = "General"
    bot.reply_to(message, f"Chat ID этого чата: {chat_id}\nИ message_thread_id: {msg_thread_id}")

bot.polling()





bot.polling(none_stop=True)


