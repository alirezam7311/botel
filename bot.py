from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# توکن ربات تلگرام شما
TOKEN = '6738356391:AAEIYgvmIQv1xa4pSmaqFy70zSDDpl6Ed_w'

# تابع برای پاسخ به دستور /start
def start(update, context):
    update.message.reply_text('سلام! من یک ربات تلگرام هستم.')

# تابع برای پاسخ به هر پیام متنی
def echo(update, context):
    update.message.reply_text(update.message.text)

# تنظیمات ربات و شروع به کار
def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
