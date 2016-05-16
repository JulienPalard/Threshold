
class ArgumentItem():
    """
        参数数据结构
    """

    def __init__(self, name, _type, default=None, result_name=None, check_functions=None, after_handler_functions=None):
        self.name = name                                         # 参数名
        self._type = _type                                       # 参数类型
        self.default = default                                   # 参数默认值
        self.result_name = result_name                           # 最后返回给请求处理阶段的参数名称
        self.check_functions = check_functions                   # 参数验证函数元组列表，(function, arguments, error message)
        self.after_handler_functions = after_handler_functions   # 参数验证通过之后进行处理的函数元组列表, (function, error message)
        self.value = None                                        # 验证处理之后的返回值
