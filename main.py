import os
import urllib
from dotenv import load_dotenv
from countryinfo import CountryInfo
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


load_dotenv()

Bot = Client(
    "Country-Info-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_TEXT = """ʜᴇʟʟᴏ {},

𝐈 𝐚𝐦 𝐚 𝐜𝐨𝐮𝐧𝐭𝐫𝐲 𝐢𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 𝐅𝐢𝐧𝐝𝐞𝐫 𝐁𝐨𝐭. \
𝐆𝐢𝐯𝐞 𝐦𝐞 𝐚 𝐜𝐨𝐮𝐧𝐭𝐫𝐲 𝐧𝐚𝐦𝐞 𝐈 𝐰𝐢𝐥𝐥 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐢𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧𝐬 𝐨𝐟 𝐭𝐡𝐞 𝐜𝐨𝐮𝐧𝐭𝐫𝐲.\

★ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @synaxnetwork 🦋 """

HELP_TEXT = """**𝐌𝐨𝐫𝐞 𝐇𝐞𝐥𝐩**

✰ ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ᴀ ᴄᴏᴜɴᴛʀʏ ɴᴀᴍᴇ.
✰ ᴛʜᴇɴ ɪ ᴡɪʟʟ ᴄʜᴇᴄᴋ ᴀɴᴅ sᴇɴᴅ ʏᴏᴜ ᴛʜᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴs.

**ɪɴғᴏʀᴍᴀᴛɪᴏɴs :-**
Name, Native Name, Capital, Population, Region, Sub Region, \
Top Level Domains, Calling Codes, Currencies, Residence, \
Timezone, Wikipedia, Google"""

ABOUT_TEXT = """**𝐀𝐛𝐨𝐮𝐭 𝐌𝐞**

- **ʙᴏᴛ :** `𝐂𝐨𝐮𝐧𝐭𝐫𝐲 𝐈𝐧𝐟𝐨 𝐁𝐨𝐭🦋`
- **ᴄʀᴇᴀᴛᴏʀ :**
  - [𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦](https://telegram.me/synaxnetwork)
  - [𝐆𝐢𝐭𝐡𝐮𝐛](https://github.com/SynaxBots)
- **sᴏᴜʀᴄᴇ :** [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://github.com/SynaxBots/CountryinfosynaxBot)
- **ʟᴀɴɢᴜᴀɢᴇ :** [𝐏𝐲𝐭𝐡𝐨𝐧3](https://python.org)
- **ғʀᴀᴍᴇᴡᴏʀᴋ :** [𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦](https://pyrogram.org)"""

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('🇮🇳 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ 🇮🇳', url='https://telegram.me/synaxnetwork')
        ],
        [
            InlineKeyboardButton('𝐇𝐞𝐥𝐩 🐰', callback_data='help'),
            InlineKeyboardButton('𝐀𝐛𝐨𝐮𝐭 ☢️', callback_data='about'),
            InlineKeyboardButton('𝐂𝐥𝐨𝐬𝐞 🍃', callback_data='close')
        ]
    ]
)
HELP_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('𝐇𝐨𝐦𝐞 🌷', callback_data='home'),
            InlineKeyboardButton('𝐀𝐛𝐨𝐮𝐭 ☢️', callback_data='about'),
            InlineKeyboardButton('𝐂𝐥𝐨𝐬𝐞 🍃', callback_data='close')
        ]
    ]
)
ABOUT_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('𝐇𝐨𝐦𝐞 🌷', callback_data='home'),
            InlineKeyboardButton('𝐇𝐞𝐥𝐩 🐰', callback_data='help'),
            InlineKeyboardButton('𝐂𝐥𝐨𝐬𝐞 🍃', callback_data='close')
        ]
    ]
)
ERROR_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('𝐇𝐞𝐥𝐩 🐰', callback_data='help'),
            InlineKeyboardButton('𝐂𝐥𝐨𝐬𝐞 🍃', callback_data='close')
        ]
    ]
)


@Bot.on_callback_query()
async def cb_data(bot, update):
    
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    
    else:
        await update.message.delete()


@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )


@Bot.on_message(filters.private & filters.text)
async def countryinfo(bot, update):
    
    try:
        country = CountryInfo(update.text)
    except KeyError:
        await update.reply_text(
            text="Key error.\nCan you check the name again."
        )
        return
    
    google_url = "https://www.google.com/search?q="+urllib.parse.quote(country.name())
    info = f"""**Country Information**

Name : `{country.name()}`
Native Name : `{country.native_name()}`
Capital : `{country.capital()}`
Population : `{country.population()}`
Region : `{country.region()}`
Sub Region : `{country.subregion()}`
Top Level Domains : `{country.tld()}`
Calling Codes : `{country.calling_codes()}`
Currencies : `{country.currencies()}`
Residence : `{country.demonym()}`
Timezone : `{country.timezones()}`

☢️ ʙᴏᴛ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @synaxnetwork 🇮🇳"""
    
    reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('𝐖𝐢𝐤𝐢𝐩𝐞𝐝𝐢𝐚 🤍', url=country.wiki()),
                InlineKeyboardButton('𝐆𝐨𝐨𝐠𝐥𝐞 🤍', url=google_url)
            ],
            [
                InlineKeyboardButton('🇮🇳 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ 🇮🇳', url='https://telegram.me/synaxnetwork')
            ]
        ]
    )
    
    try:
        await update.reply_text(
            text=info,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
    except Exception as error:
        print(error)


Bot.run()
