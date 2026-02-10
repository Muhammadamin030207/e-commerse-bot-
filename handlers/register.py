from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.register import RegisterState
from keyboars.reply import contact_keyboard, confirm_keyboard

router = Router()

@router.message(RegisterState.full_name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await message.answer("Yoshingizni kiriting:")
    await state.set_state(RegisterState.age)

@router.message(RegisterState.age)
async def get_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Yosh raqam bo'lishi kerak!")
    elif int(message.text) <= 15:
        await message.answer("Siz 15 yoshdan katta bo'lishingiz kerak!")
        return

    await state.update_data(age=message.text)
    await message.answer("Gmail manzilingizni kiriting:")
    await state.set_state(RegisterState.email)

@router.message(RegisterState.email)
async def get_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer(
        "Kontaktni tugma orqali yuboring:",
        reply_markup=contact_keyboard()
    )
    await state.set_state(RegisterState.phone)

@router.message(RegisterState.phone)
async def get_phone(message: Message, state: FSMContext):
    if not message.contact:
        await message.answer("Kontaktni faqat tugma orqali yuboring!")
        return

    await state.update_data(phone=message.contact.phone_number)
    data = await state.get_data()

    text = (
        "Ma'lumotlaringizni tekshiring:\n\n"
        f"Ism: {data['full_name']}\n"
        f"Yosh: {data['age']}\n"
        f"Gmail: {data['email']}\n"
        f"Telefon: {data['phone']}"
    )

    await message.answer(text, reply_markup=confirm_keyboard())
    await state.set_state(RegisterState.confirm)

@router.message(RegisterState.confirm)
async def confirm_handler(message: Message, state: FSMContext):
    data = await state.get_data()

    if message.text == "Tasdiqlash":
        await message.answer(
            "Siz muvaffaqiyatli ro'yxatdan o'tdingiz!\n\n"
            f"Ism: {data['full_name']}\n"
            f"Yosh: {data['age']}\n"
            f"Gmail: {data['email']}\n"
            f"Telefon: {data['phone']}"
        , reply_markup=None)
        await state.clear()
        

    elif message.text == "Tahrirlash":
        await message.answer("Qayta kiriting.\nIsm familiyangizni yozing:")
        await state.set_state(RegisterState.full_name)

    else:
        await message.answer("Tugmalardan foydalaning")
