from aiogram.filters import BaseFilter


class MyFalseFilter(BaseFilter):
    def __call__(self, ) -> bool:
        return False


class MyTrueFilter(BaseFilter):
    def __call__(self, ) -> bool:
        return True
