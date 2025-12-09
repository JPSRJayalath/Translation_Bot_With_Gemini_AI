from telethon import TelegramClient, events
from telethon.tl.types import MessageEntityTextUrl
from deep_translator import MyMemoryTranslator, GoogleTranslator
from google import genai

API_ID = 28600944
API_HASH = "d989819aaac1d8c68a05fa83ddfe3114"
BOT_TOKEN = "8574292178:AAHYcQiOUqBn3oyLXAFZdw02hOAKZb8gjq4"
SESSION = "GrammarBuddy"
Gemini_API_KEY = "AIzaSyCetdoR3kbsagJB8Xpmqybo9S0lucCu3mQ"
Gemini_model = "gemini-2.5-flash"

luka = 5556506142
mine = 1192506847
sago = 7983138320

client = TelegramClient(SESSION, API_ID, API_HASH).start(bot_token=BOT_TOKEN)
ai_client = genai.Client(api_key=Gemini_API_KEY)

change = { luka: 1, mine: 0 , sago: 0}

def print_error_pattern():
    w = "ABCDE"
    t = ""
    for i in range(len(w)):
        t = w[i] + t
        print(t)

@client.on(events.NewMessage())
async def handler(event):
    try:
        user_id = event.sender_id
        input_text = event.text

        if user_id != luka and user_id != mine and user_id != sago:
            return

        if input_text.startswith("/start"):
            await event.reply("Hello! I am a translation bot. Send me a message to translate it.")
            return
        elif input_text.startswith("/change"):
            if change[user_id] == 0:
                change[user_id] = 1
                await client.send_message(user_id, "You are now in Khmer to English mode.")
            else:
                change[user_id] = 0
                await client.send_message(user_id, "You are now in English to Khmer mode.")
            return

        if user_id == luka:
            if change[user_id] == 1:
                translated_text_mymemory = MyMemoryTranslator(source="km-KH", target="en-US").translate(input_text)
            else:
                translated_text_mymemory = MyMemoryTranslator(source="en-US", target="km-KH").translate(input_text)
            await client.send_message(user_id, f"`{translated_text_mymemory}`")
        
        if user_id == mine or user_id == sago:
            if change[user_id] == 1:
                translated_text_mymemory = MyMemoryTranslator(source="km-KH", target="en-US").translate(input_text)
            else:
                translated_text_mymemory = MyMemoryTranslator(source="en-US", target="km-KH").translate(input_text)
            await client.send_message(user_id, f"`{translated_text_mymemory}`")
        print(f"User {user_id} sent: {input_text} -> translated: {translated_text_mymemory}")
    except Exception as e:
        print(e)
        print_error_pattern()

# response = ai_client.models.generate_content(
#     model=Gemini_model,
#     contents="Explain how AI works in a few words",
# )

# print(response.text)

client.start()
client.run_until_disconnected()
