import typing

from aiogram.dispatcher.filters import BoundFilter
from loader import admins, dp


class AdminFilter(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin: typing.Optional[bool] = None):
        self.is_admin = is_admin

    async def check(self, message):
        return (message.from_user.id in admins) == self.is_admin


dp.filters_factory.bind(AdminFilter)
