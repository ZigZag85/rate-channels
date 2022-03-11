from pyrogram import Client, CallbackQueryHandler, Filters
from pyromod import listen # noqa
from plugins.start_handler import start_handler


app = Client(
    'rateChannels',
    api_id=2328433,
    api_hash="499e1423e008e12e8909a18b2ecfc407",
    bot_token="5102085268:AAHQKo41OIWmuoH0y8EFUubgilrnaDzu2uQ",
    plugins={'root': 'plugins'}
)
app.add_handler(CallbackQueryHandler(start_handler, Filters.callback_data('home')))
app.run()
