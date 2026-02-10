from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def contact_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📞Contact", request_contact=True)]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

def confirm_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Tasdiqlash")],
            [KeyboardButton(text="Tahrirlash")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
