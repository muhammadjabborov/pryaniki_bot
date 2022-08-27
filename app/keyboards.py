from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

keyboards_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='💬 Biz haqimizda'), KeyboardButton("📍 Bizning manzilimiz")],
        [KeyboardButton(text='≡ Menu'), KeyboardButton(text="✍ Izoh qoldirish")],
        [KeyboardButton(text='🛍 Bizning Mahsulotlar')]
    ],
    resize_keyboard=True, one_time_keyboard=True
)

keyboards_product = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sgushonkali Pryanik"), KeyboardButton(text="Kakosli Pryanik")
        ],
        [
            KeyboardButton(text="Kakaoli Pryanik"), KeyboardButton(text="Kunjutli Pryanik"),
            KeyboardButton(text="Oddiy Pryanik")
        ],
        [
            KeyboardButton(text="🔙 Ortga")
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

keyboards_kilogram = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='3kg'), KeyboardButton(text='5kg'), KeyboardButton(text='10kg')]
    ], resize_keyboard=True, one_time_keyboard=True
)

keyboard_back_complain = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔙 Orqaga')
        ]
    ],
    resize_keyboard=True
)

keyboard_cancel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='❌ Bekor qilish')
        ]
    ], resize_keyboard=True
)

keyboards_of_biscuit = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Sgushonkali Pryanik", callback_data='1')],
        [InlineKeyboardButton(text="Kakaoli Pryanik", callback_data='2')],
        [InlineKeyboardButton(text="Kakosli Pryanik", callback_data='3')],
        [InlineKeyboardButton(text="Kunjutli Pryanik", callback_data='4')],
        [InlineKeyboardButton(text="Oddiy Pryanik", callback_data='5')]
    ], one_time=True
)

keyboard_phone = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📞 Telefon raqamni jonatish", request_contact=True)
        ]
    ], resize_keyboard=True, one_time_keyboard=True,
)

keyboard_adress = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍 Adresni jonatish", request_location=True)
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

keyboard_t_f = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Ha"), KeyboardButton(text="❌ Yoq")
        ]
    ], resize_keyboard=True
)
