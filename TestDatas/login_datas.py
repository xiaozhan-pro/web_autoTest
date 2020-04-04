# 正常场景 登录成功
success = ("18684720553","python")

# 异常场景 用户名为空/密码为空/用户名格式不正确
cases_from_form_wrong_format = [
    {"username": "",
     "password": "python",
     "expect_result": "请输入手机号"},

    {"username": "18684720553",
     "password": "",
     "expect_result": "请输入密码"},

    {"username": "1868472055",
     "password": "python",
     "expect_result": "请输入正确的手机号"}
]

cases_from_middle_wrong_format = [
    {"username": "18684720553",
     "password": "python123",
     "expect_result": "帐号或密码错误!"},

    {"username": "18684720550",
     "password": "python",
     "expect_result": "此账号没有经过授权，请联系管理员!"}
]