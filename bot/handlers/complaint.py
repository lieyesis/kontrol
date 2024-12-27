from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove
from bot.database import save_complaint

router = Router()

class ComplaintForm(StatesGroup):
    name = State()
    contact = State()
    complaint = State()

@router.message(commands=["complaint"])
async def start_complaint(message: types.Message, state: FSMContext):
    await state.set_state(ComplaintForm.name)
    await message.answer("Введите ваше имя:")

@router.message(ComplaintForm.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(ComplaintForm.contact)
    await message.answer("Введите ваш контакт (телефон или соцсети):")

@router.message(ComplaintForm.contact)
async def process_contact(message: types.Message, state: FSMContext):
    await state.update_data(contact=message.text)
    await state.set_state(ComplaintForm.complaint)
    await message.answer("Введите вашу жалобу:")

@router.message(ComplaintForm.complaint)
async def process_complaint(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    save_complaint(user_data['name'], user_data['contact'], message.text)
    await message.answer("Спасибо! Ваша жалоба сохранена.", reply_markup=ReplyKeyboardRemove())
    await state.clear()
