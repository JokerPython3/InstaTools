#Use Vpn
import subprocess
import random
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


try:
    import telebot
    from telebot import types
    from Topython import Instagram
except ImportError:
    install("curl2pyreqs")
    install("user_agent")
    install("pysocks")
    install("telebot")
    install('pyTelegramBotAPI')
    install('Topython')
    import telebot
    from telebot import types
    from Topython import Instagram


token = input("Enter Token Bot : ")
bot = telebot.TeleBot(token)
print("روح للبوت ودز /start")
good = 0  
bad = 0   

@bot.message_handler(commands=['start'])
def s1(mes):
    try:
        c = types.InlineKeyboardButton(text='مطور', url='https://t.me//jokerpython3')
        b = types.InlineKeyboardButton(text='قناة مطور', url='https://t.me//jokerpython3')
        q = types.InlineKeyboardButton(text='بدا صيد يوزرات', callback_data='g')

        x = types.InlineKeyboardMarkup(row_width=1)
        x.add(b, q, c)

        bot.send_message(mes.chat.id, 'هااااا وللك ', reply_markup=x)
    except Exception as e:
        bot.send_message(mes.chat.id, f"حدث خطأ: {e}")

@bot.callback_query_handler(func=lambda call: True)
def ded(call):
    global good, bad, bot

    try:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'''
انتضر اصيدلك يوزراات 
#_#_#
عدد يوزرات متاحات : {good}
عدد يوزرات غير متاحات : {bad}
''')

        while True:
            uh = "".join(random.choice("1234567890") for _ in range(1))
            ns = "".join(random.choice("qwertyuiopasdfghjklzxcvbnm._") for _ in range(1))
            j = "".join(random.choice("1234567890qwertyuiopasdfghjklzxcvbnm._") for _ in range(1))
            user = f"{j}_{ns}_{uh}"

            check = Instagram.CheckUsers(f"{user}")
            if check:
                good += 1
                bot.send_message(call.message.chat.id, f'{user} متاح')
            else:
                bad += 1

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'''
انتضر اصيدلك يوزراات 
#_#_#
عدد يوزرات متاحات : {good}
عدد يوزرات غير متاحات : {bad}
''')
    except Exception as e:
        bot.send_message(call.message.chat.id, f"حدث خطأ أثناء محاولة الصيد: {e}")


bot.infinity_polling()#تباً