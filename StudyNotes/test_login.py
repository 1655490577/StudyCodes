import pytest
import requests
from config import config


url = config.url + '/supervisor/admin/sysadmin/login'
headers = {'Content-Type': 'application/json'}


class TestLogin():

    @pytest.mark.parametrize(("password", "phone"), [('123456', '13168775547'), ('123456', '13168775501')])
    def test_login_success(self, password, phone):
        """
        登录成功
        :return:
        """
        a = {'password': password, 'phone': phone, 'rememberMe': True}
        r = requests.post(url, json=a, headers=headers)
        assert r.status_code == 200
        assert '用户列表' and '菜单列表' in r.text
        # return r

    def test_login_fail(self):
        """
        登录失败
        :return:
        """
        a = {'password': 'admin', 'phone': 'admin', 'rememberMe': True}
        r = requests.post(url, json=a, headers=headers)
        pass


if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py'])
# print(test_login().status_code)
# print(test_login().text)
