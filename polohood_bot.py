import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Логування
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Ваш токен бота
TOKEN = '7011040152:AAGyPzfw-tEiAgwrDN_SXmmvSS8MoEjCnTU'

# Головне меню
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Міти", callback_data='meetings'),
            InlineKeyboardButton("Останій реліз", callback_data='latest_release')
        ],
        [
            InlineKeyboardButton("Музика", callback_data='music'),
            InlineKeyboardButton("Інстаграм", callback_data='instagram')
        ],
        [
            InlineKeyboardButton("СоундКлауд", callback_data='soundcloud'),
            InlineKeyboardButton("Змінити мову", callback_data='change_language')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Виберіть опцію:', reply_markup=reply_markup)

# Обробка кнопок
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == 'meetings':
        show_meetings(query)
    elif query.data == 'latest_release':
        show_latest_release(query)
    elif query.data == 'music':
        show_music(query)
    elif query.data == 'instagram':
        show_instagram(query)
    elif query.data == 'soundcloud':
        show_soundcloud(query)
    elif query.data == 'change_language':
        show_language_options(query)

# Показати зустрічі
def show_meetings(query):
    keyboard = [
        [
            InlineKeyboardButton("Повернутись на головну", callback_data='start'),
            InlineKeyboardButton("Забронювати міт", callback_data='book_meeting'),
            InlineKeyboardButton("Перенести міт", callback_data='reschedule_meeting')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = "Міти у нас в Неділю на 21:00 (9 p.m) і в Четверг на 21:00 (9 p.m)"
    query.edit_message_text(text=text, reply_markup=reply_markup)

# Показати останній реліз
def show_latest_release(query):
    keyboard = [
        [InlineKeyboardButton("Повернутись на головну", callback_data='start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = "Останій реліз: [Назва релізу]\nСилка на пост: [посилання]\nСилка на YouTube: [посилання]"
    query.edit_message_text(text=text, reply_markup=reply_markup)

# Показати музику
def show_music(query):
    keyboard = [
        [InlineKeyboardButton("Повернутись на головну", callback_data='start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = "Музика: [Кілька секунд музики для захисту авторських прав]"
    query.edit_message_text(text=text, reply_markup=reply_markup)

# Показати Instagram
def show_instagram(query):
    keyboard = [
        [InlineKeyboardButton("Повернутись на головну", callback_data='start')],
        [InlineKeyboardButton("Instagram PoloHood", url='https://www.instagram.com/polohood')],
        [InlineKeyboardButton("Instagram засновників", url='https://www.instagram.com/засновник')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Instagram", reply_markup=reply_markup)

# Показати SoundCloud
def show_soundcloud(query):
    keyboard = [
        [InlineKeyboardButton("Повернутись на головну", callback_data='start')],
        [InlineKeyboardButton("SoundCloud PoloHood", url='https://soundcloud.com/polohood')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="SoundCloud", reply_markup=reply_markup)

# Показати опції зміни мови
def show_language_options(query):
    keyboard = [
        [
            InlineKeyboardButton("Українська", callback_data='start'),
            InlineKeyboardButton("English", callback_data='start')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Оберіть мову:", reply_markup=reply_markup)

def main() -> None:
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
