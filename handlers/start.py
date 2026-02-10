from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from keyboars.inline import start_inline_keyboard
from aiogram.fsm.context import FSMContext
from states.register import RegisterState

router = Router()

@router.message(CommandStart())
async def start_command_handler(msg: Message):
    await msg.answer(
        f"Assalomu alaykum!\n"
        f"{msg.from_user.full_name}!\n"
        f"Smart Shop botiga xush kelibsiz! 😊",
        reply_markup=start_inline_keyboard()
    )

@router.callback_query(lambda c: c.data == "register")
async def start_register_callback(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Ism va familiyangizni kiriting:")
    await state.set_state(RegisterState.full_name)
    await call.answer()
