from threshold.config.tornado_config import Config
from threshold.error import CheckException, AfterHandlerException

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
                argument_item.value = argument
                self.check(argument_item)
                self.after_handler(argument_item)
                # 将结果添加到结果集中
                if argument_item.result_name:
                    self.result_param[argument_item.result_name] = argument_item.value
                else:
                    self.result_param[argument_item.name] = argument_item.value 
        except Exception as e:
            raise e

    def check(self, argument_item):
        if not argument_item.check_functions:
            return
        for check_function, kwargs, error_message in argument_item.check_functions:
            assert hasattr(check_function, "__call__"), "请设置正确的check function"
            assert type(kwargs) == type(dict()) or kwargs is None, "kwargs必须是 dict 或者 None"
            if kwargs:
                if not check_function(argument_item.value, **kwargs):
                    raise CheckException(name=check_function.__name__, message=error_message)
            else:
                if not check_function(argument_item.value):
                    raise CheckException(name=check_function.__name__, message=error_message)

    def after_handler(self, argument_item):
        if not argument_item.after_handler_functions:
            return
        for after_handler_function, kwargs, error_message in argument_item.after_handler_functions:
            assert hasattr(after_handler_function, "__call__"), "请设置正确的after handler function"
            assert type(kwargs) == type(dict()) or kwargs is None, "kwargs必须是 dict 或者 None"
            if kwargs:
                argument_item.value = after_handler_function(argument_item.value, **kwargs)
            else:
                argument_item.value = after_handler_function(argument_item.value)

    def _is_exist_name(self, name): # 是否存在该参数
        pass

    def _convert_data_type(self, value, _type): # 转换参数类型
        return _type(value)

    def __call__(self):
        for argument_item in self.argument_items:
            self.parse(argument_item)
        return self.result_param
