from loader import dp
from aiogram import types
from checkWord import checkWords, get_available, trans_matches
from krill_latin import krill_latin



@dp.message_handler()
async def response(message: types.Message):
    msg = message.text
    msg_list = msg.split()
    for s in msg_list:
        if ',' in s:
            sz = s.replace(',', '')
            word = sz
            words = checkWords(word)
            get = get_available(words)
            if get:
                await message.answer(f"✅ {word}")
            else:
                related = trans_matches(words)
                sozlar = {}
                sozlar['word'] = f"❌ {word}"
                sozlar['words'] = "\n".join(related)
                await message.answer(f"{sozlar['word']} \n{sozlar['words']}")
        elif '.' in s:
            sz = s.replace('.', '')
            word = sz
            words = checkWords(word)
            get = get_available(words)
            if get:
                await message.answer(f"✅ {word}")
            else:
                related = trans_matches(words)
                sozlar = {}
                sozlar['word'] = f"❌ {word}"
                sozlar['words'] = "\n".join(related)
                await message.answer(f"{sozlar['word']} \n{sozlar['words']}")

        else:
            word = s
            words = checkWords(word)
            get = get_available(words)
            if get:
                await message.answer(f"✅ {word}")
            else:
                related = trans_matches(words)
                sozlar = {}
                sozlar['word'] = f"❌ {word}"
                sozlar['words'] = "\n".join(related)
                await message.answer(f"{sozlar['word']} \n{sozlar['words']}")