from uzwords import words
from difflib import get_close_matches
from krill_latin import krill_latin
# get_close_matches funksiyasi berilgan so'zga o'xshash so'zni berilgan ro'yxat ichidan qidiradi.


def checkWords(l_word, words=words):
    """Bu funksiya qabul qilingan so'zga o'xshash so'zlarni words ni ichidan qidiradi. \
    Agar so'z mavjud bo'lsa True hamda o'sha so'zni o'zini lotinchaga tarjima qilib qaytaradi\
    Agar mavjud bo'lmasa False hamda kiritilgan so'zga o'xshash so'zlarni to'plamini qaytaradi."""
    word = krill_latin(l_word).lower()
    matches = set(get_close_matches(word, words))
    available = False

    if word in matches:
        available = True
        matches = krill_latin(word)

    elif 'ҳ' in word:
        word = word.replace('ҳ', 'х')
        matches.update(get_close_matches(word, words))

    elif 'х' in word:
        word = word.replace('x', 'ҳ')
        matches.update(get_close_matches(word, words))

    dictionary = {'available' : available, 'matches' : matches}

    return dictionary


def trans_matches(dictionary):
    """Bu funksiya lug'at qabul qiladi. Lug'atni ichidan matches keys iga tegishli qiymatlarni ajratib oladi\
    hamda matches ni ichidagi har bir qiymatni ajratib olib trans listiga qo'shadi va \
     bu funksiya so'zlarni lotinga tarjimasi listini qaytaradi."""
    available = dictionary['available']
    matche = dictionary['matches']
    trans = []
    for w in matche:
        trans.append(krill_latin(f"✅ {w}"))
    return trans


def get_available(dictionary):
    """Bu funksiya faqat Boolean qiymat qaytaradi."""
    available = dictionary['available']
    return available