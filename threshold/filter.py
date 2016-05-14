from threshold.config.tornado_config import Config
from threshold.error import FilterException

class Filter():
    def __init__(self, argument_items, request):
        self.result_param = dict()
        self.argument_items = argument_items
        self.config = Config(request)

    def parse(self, argument_item): # 参数解析
        # 得到 argument 的值
        try:
            if self.config.is_get_method():
                argument = self.config.get_argument(argument_item.name)
                argument = self._convert_data_type(argument, argument_item._type)
                print(argument, type(argument))
        except Exception as e:
            raise e

    def _is_exist_name(self, name): # 是否存在该参数
        pass

    def _convert_data_type(self, value, _type): # 转换参数类型
        return _type(value)

    def __call__(self):
        self.parse(self.argument_items[0])
        return "test"
