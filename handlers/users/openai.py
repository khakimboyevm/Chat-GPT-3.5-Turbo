import openai
from aiogram import types
from loader import dp
from data.config import OPENAI_KEY

openai.api_key = OPENAI_KEY

@dp.message_handler(state=None)
async def gpt_answer(message: types.Message):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
)

    await message.answer(response['choices'][0]['text'])