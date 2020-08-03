import telebot 
from time import sleep

bot = telebot.TeleBot('token')

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, "Давай поиграем в игру! Напиши :game_die  или 🎲 и отправь смайлик, который предложит тебе телеграм. Если на нём выпадет 6, то ты выйграл! Если нет, то попробуй ещё раз! (значение на смайлике слуйчайно)") #bot.send_message(message.chat.id, "Dorou" + str(group))
	print("ok")
@bot.message_handler(content_types=["dice"])
def emoji(message):
	print("poluchil")
	emojjji = message.dice.value
	sleep(3)
	if emojjji == 6:
		bot.send_message(message.chat.id, "Вы выйграли! Вот значение смайлика: " + str( emojjji))
	else:
		bot.send_message(message.chat.id, "Вы проиграли( Вот значение смайлика: " + str( emojjji))
	#bot.send_message(message.chat.id, "Значение смайлика: " + str( emojjji))


if __name__ == '__main__':
	while True:
		try:
			bot.polling(none_stop=True)
		except Exception as e:
			time.sleep(15)