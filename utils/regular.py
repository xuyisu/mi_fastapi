def get_err(form):
    """
        获取form错误文本
    """
    error_list = []
    for item in form.errors:
        # 确保每个错误信息都是字符串
        for error in form.errors[item]:
            if isinstance(error, str):
                error_list.append(error)
            else:
                error_list.append(str(error))  # 将非字符串类型的错误转换为字符串
    err_str = '/'.join(error_list)
    return err_str