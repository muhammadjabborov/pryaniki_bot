from aiogram.dispatcher import FSMContext

from app.config import dp, bot
from aiogram import types
import app.database.db as db
import app.keyboards as kb
from app.state import Complain, Order


@dp.message_handler(commands=['start'])
async def bot_start_command(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id,
                           f"salom {message.from_user.first_name}", reply_markup=kb.keyboards_menu)
    async with state.proxy() as data:
        data['telegram_id'] = message.from_user.id
        data['username'] = message.from_user.username


@dp.message_handler(regexp="💬 Biz haqimizda")
async def process_about_as(message: types.Message):
    await bot.send_message(message.chat.id, "biz nmadur pryanikni baxriddin yozadi", reply_markup=kb.keyboards_menu)


@dp.message_handler(regexp="📍 Bizning manzilimiz")
async def process_our_address(message: types.Message):
    await bot.send_location(message.chat.id, latitude=41.3265461365974, longitude=69.22893186986677,
                            reply_markup=kb.keyboards_menu)


@dp.message_handler(regexp="🛍 Bizning Mahsulotlar")
async def process_my_orders(message: types.Message):
    await bot.send_message(message.chat.id, "Bizning mahsulotlar", reply_markup=kb.keyboards_product)


@dp.message_handler(regexp="Sgushonkali")
async def process_im(message: types.Message):
    rasm = open("app/images/sgushonkali.jpg", "rb")
    await bot.send_photo(message.chat.id, rasm, "Description", reply_markup=kb.keyboards_product)


@dp.message_handler(regexp="Kakosli")
async def process_im(message: types.Message):
    rasm = open("app/images/kakosli.jpg", "rb")
    await bot.send_photo(message.chat.id, rasm, "Description", reply_markup=kb.keyboards_product)


@dp.message_handler(regexp="Kakaoli")
async def process_im(message: types.Message):
    rasm = open("app/images/kakao.jpg", "rb")
    await bot.send_photo(message.chat.id, rasm, "Description", reply_markup=kb.keyboards_product)


@dp.message_handler(regexp="Kunjutli")
async def process_im(message: types.Message):
    rasm = open("app/images/kunjutli.jpg", "rb")
    await bot.send_photo(message.chat.id, rasm, "Description", reply_markup=kb.keyboards_product)


@dp.message_handler(regexp="Oddiy")
async def process_im(message: types.Message):
    rasm = open("app/images/oddiy.jpg", "rb")
    await bot.send_photo(message.chat.id, rasm, "Description", reply_markup=kb.keyboards_product)


@dp.message_handler(regexp="🔙 Ortga")
async def process_b(message: types.Message):
    await bot.send_message(message.chat.id, "Quyidagilardan birini tanlang 🔽", reply_markup=kb.keyboards_menu)


@dp.message_handler(regexp="✍ Izoh qoldirish")
async def complain(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, "Taklif yoki Shikoyatlaringizni kiriting",
                           reply_markup=kb.keyboard_back_complain)
    await Complain.next()


@dp.message_handler(state=Complain.complaint)
async def complain_process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['complain'] = message.text
    if message.text == '🔙 Orqaga':
        await state.finish()
        await bot.send_message(message.chat.id, "Quyidagilardan birini tanlang 🔽", reply_markup=kb.keyboards_menu)
    else:
        await bot.send_message(-1001684364895,
                               f'Takliflar va shikoyatdan\n'
                               f'Taklifi yoki shikoyati: {data.get("complain")}\n'
                               f'Ismi: {message.from_user.first_name}\n'
                               f'Username: @{message.from_user.username}\n')
        await bot.send_message(message.chat.id, "Taklifingiz yokida Shikoyatingiz qabul qilindi☺",
                               reply_markup=kb.keyboards_menu)

        await state.finish()


products = {
    '1': 'Sgushonkali Pryanik',
    '2': 'Kakaoli Pryanik',
    '3': 'Kakosli Pryanik',
    '4': 'Kunjutli',
    '5': 'Oddiy'
}


@dp.message_handler(regexp="≡ Menu")
async def menu_process(message: types.Message):
    rasm = open("app/images/Prjaniki.jpg", "rb")
    await bot.send_photo(message.chat.id, rasm, "Menumizga xush-kelibsiz 🤗", reply_markup=kb.keyboards_of_biscuit)
    await Order.next()


@dp.callback_query_handler(state=Order.proudct_title)
async def callback_peoduct_handler(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
        data['product_title'] = products[callback.data]
    await callback.message.answer(text=products[callback.data], reply_markup=kb.keyboards_kilogram)
    await Order.next()


@dp.message_handler(state=Order.product_kilo)
async def order_process(message: types.Message, state=FSMContext):
    if message.text == '3kg' or '5kg' or '10kg':
        async with state.proxy() as data:
            data['product_kilo'] = message.text
        await bot.send_message(message.chat.id, 'Nechta xoxlaysiz', reply_markup=kb.keyboard_cancel)
        await Order.next()
    else:
        await bot.send_message(message.chat.id, "Iltimos togri vazni jonating", reply_markup=kb.keyboards_kilogram)


@dp.message_handler(state=Order.product_count)
async def order_process_count(message: types.Message, state=FSMContext):
    if message.text.isalpha():
        await state.finish()
        await bot.send_message(message.chat.id, "Iltimos togri son yuboring")
        return Order.product_count
    if message.text == '❌ Bekor qilish':
        await state.finish()
        await bot.send_message(message.chat.id, "Quyidagilardan birini tanlang 🔽", reply_markup=kb.keyboards_menu)
    else:
        async with state.proxy() as data:
            data['product_count'] = message.text
        await bot.send_message(message.chat.id, "Nomeringizni jonating", reply_markup=kb.keyboard_phone)
        await Order.next()


@dp.message_handler(state=Order.phone_number, content_types=['contact'])
async def order_process_number(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.contact.phone_number
    await bot.send_message(message.chat.id, "Adressingizni yuboring", reply_markup=kb.keyboard_adress)
    await Order.next()


@dp.message_handler(content_types=types.ContentType.LOCATION, state=Order.address)
async def order_process_adres(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['latitude'] = message.location['latitude']
        data['longitude'] = message.location['longitude']
        data['address'] = f"{message.location['latitude']} {message.location['longitude']}"
        await state.finish()
        await bot.send_message(message.chat.id, "Shu malumotlaringizni tasdiqlaysizmi? ")
        await bot.send_message(message.chat.id, f'Pryanik Turi: {data.get("product_title")}\n'
                                                f'Pryanik Kilosi: {data.get("product_kilo")}\n'
                                                f'Pryanik Soni: {data.get("product_count")}\n'
                                                f'TelNomer: {data.get("phone_number")}', reply_markup=kb.keyboard_t_f)


@dp.message_handler(regexp="✅ Ha")
async def order_t_process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        db.new_order(
            data.get("phone_number"), data.get("location"), data.get("product_title"), data.get("product_kilo"),
            data.get("product_count"), data.get("telegram_id"), data.get("username")
        )
        await bot.send_message(-1001684364895, f'Pryanik Turi: {data.get("product_title")}\n'
                                               f'Pryanik Kilosi: {data.get("product_kilo")}\n'
                                               f'Pryanik Soni: {data.get("product_count")}\n'
                                               f'TelNomer: {data.get("phone_number")}')
        await bot.send_location(-1001684364895, latitude=data.get('latitude'), longitude=data.get('longitude'))
        await bot.send_message(message.chat.id, "Siz muvaffaqiyatli buyurtma qildiz", reply_markup=kb.keyboards_menu)


@dp.message_handler(regexp="❌ Yoq")
async def order_t_process(message: types.Message):
    await bot.send_message(message.chat.id, "Quyidagilardan birini tanlang 🔽", reply_markup=kb.keyboards_menu)
