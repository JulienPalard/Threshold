
class ArgumentItem():
    """
        参数数据结构

        假设指定了 require 为 False 且 default 为 None, 则是在有该参数的情况下进行验证，
    如果没有该参数则直接跳过，返回结果也不包含该参数，但如果在指定 require 为 False 的
    情况下, default 不为 None 则如果请求里面没有该参数则在返回结果里面加入该参数并且设
    置值为 default.
    """

    def __init__(self, name, _type, require=True, default=None, not_exists_message=None, result_name=None, check_functions=None, after_handler_functions=None):
        self.name = name                                         # 参数名
        self._type = _type                                       # 参数类型
        self.require = require                                   # 是否一定存在该参数
        self.default = default                                   # 参数默认值
        self.not_exists_message = not_exists_message             # 如果不存在该参数时返回的错误信息
        self.result_name = result_name if result_name else name  # 最后返回给请求处理阶段的参数名称
        self.check_functions = check_functions                   # 参数验证函数元组列表，(function, kwargs, error message)
        self.after_handler_functions = after_handler_functions   # 参数验证通过之后进行处理的函数元组列表, (function, kwargs, error message)
        self.value = None                                        # 验证处理之后的返回值
