from aiogram.dispatcher.filters import BoundFilter, IsSenderContact

from aiogram import types

class IsGroup(BoundFilter):
    async def check(self,message:types.Message):
        return message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPERGROUP,
        )