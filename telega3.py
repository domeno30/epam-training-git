##############################################
### The test project for using telegram api###
##############################################
import telebot
from telebot import types

import ch_data_in_xml
import configure
# import pogoda
import pogoda_tel

client = telebot.TeleBot(configure.BOT_TOKEN)
whook = client.delete_webhook(configure.admin_id)
###DATA
curr = (
#    str(ch_data_in_xml.USD + ' ' + ch_data_in_xml.GBP + ' ' + ch_data_in_xml.RUB + ' ' + ch_data_in_xml.EUR + ' ' + ch_data_in_xml.date_of_rate))
     str(ch_data_in_xml.USD + ' ' + ch_data_in_xml.GBP + ' ' + ' ' + ch_data_in_xml.EUR + ' ' + ch_data_in_xml.date_of_rate))
wheath = (str(pogoda_tel.loc)) + (str(pogoda_tel.j)) + (str(pogoda_tel.time_local)) + (str(pogoda_tel.k))


# print(whook)
##Handeler
@client.message_handler(commands=['app'])
# wh = client.delete_webhook()
def app(message):
    rmk = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    #    rmk = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button_phone = types.KeyboardButton(text='Отправить свой контакт ☎️',
                                        request_contact=True)  # Specify the name of the button that the user will  see
    button_location = types.KeyboardButton(text='Отправить свою локацию 🗺️', request_location=True)
    #    button_currency = types.KeyboardButton (text = 'Отправить курсы валют ЦБ РА 💱️')
    #    button_pogoda   = types.KeyboardButton (text = 'ПОГОДА 🗺️')
    button_back = types.KeyboardButton(text='BACK 🗺️')
    rmk.add(types.KeyboardButton("Отправить курсы валют ЦБ РА 🗺"), types.KeyboardButton("Погода 🌦"), (button_phone),
            (button_location), (button_back))

    msg = client.send_message(message.chat.id, "You can get info about Wheather, Your Location or Currency",
                              reply_markup=rmk)
    client.register_next_step_handler(msg, user_answer)


@client.message_handler(commands=['number'])
def phone(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)  # Connect the keyboard
    button_phone = types.KeyboardButton(text='Отправить свой контакт ☎️',
                                        request_contact=True)  # Specify the name of the button that the user will  see
    button_location = types.KeyboardButton(text='Отправить свою локацию 🗺️', request_location=True)
    button_currency = types.KeyboardButton(text='Отправить курсы валют ЦБ РА 💱️')
    button_back = types.KeyboardButton(text='BACK 🗺')
    keyboard.add((button_phone), (button_location), (button_currency), (button_pogoda),
                 (button_back))  # Add this button
    client.send_message(message.chat.id, 'Phone number',
                        reply_markup=keyboard)  # Duplicate with a message that the user will now send his phone number to the bot)


@client.message_handler(content_types=[
    'contact'])  # Announced a branch in which we prescribe logic in case the user decides to send a phone number :)
def contact(message):
    if message.contact is not None:  # If the sent object <strong> contact </strong> is not zero
        print(
            message.contact)  # We display the contact information in our panel. But in general, you can save them, or do something else, for example.


# curr = (str(ch_data_in_xml.USD +' '+ch_data_in_xml.GBP+' '+ch_data_in_xml.RUB+' '+ch_data_in_xml.EUR+' '+ch_data_in_xml.date_of_rate))
# wheath = (str(pogoda_tel.loc)) + (str(pogoda_tel.j)) + (str(pogoda_tel.time_local)) + (str(pogoda_tel.k))

# loc = request_contact(True)

def user_answer(message):
    if message.text == "Currency 💱":
        msg = client.send_message(message.chat.id, curr)
        client.register_next_step_handler(msg, user_reg)
    elif message.text == "Погода 🌦":
        client.send_message(message.chat.id, wheath)


    elif message.text == "Отправить свой контакт ☎️":
        client.send_message(message.chat.id, wheath)

    elif message.text == "Отправить свою локацию 🗺️":
        client.send_message(message.chat.id, wheath)
    elif message.text == 'Отправить курсы валют ЦБ РА 🗺':
        client.send_message(message.chat.id, curr)
    elif message.text == 'BACK 🗺':
        client.send_message(message.chat.id, "/app")
    else:
        client.send_message(message.chat.id, "Наберите /app")


def user_reg(message):
    client.send_message(message.chat.id, f"Your data: {message.text}")


#     client.send_message(message.chat.id, "{Наберите /app}")

client.polling()
