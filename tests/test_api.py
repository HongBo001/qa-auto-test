# 文件名以test_开头或者_test结尾的文件都会被pytest识别为测试文件
import time
import requests
import pytest
import allure
import logging

logger = logging.getLogger(__name__)
def test_with_logging(base_url):
    logger.info('开始测试接口')
    r = requests.get(f"{base_url}/posts/1")
    logger.debug(f"响应状态码：{r.status_code}")
    logger.info(f"响应数据：{r.text[:100]}...")
    assert r.status_code == 200
@pytest.mark.parametrize("resource, id", [("posts", 1), ("users", 1), ("comments", 1), ("todos", 1),("albums",1),("photos",1)])

def _test_get_status(resource, id):
    r = requests.get(f"https://jsonplaceholder.typicode.com/{resource}/{id}")
    print(r.json)
    assert r.status_code == 200
    data = r.json()
    assert data['id'] == id
    time.sleep(4)
def test_404():
    r = requests.get('https://jsonplaceholder.typicode.com/users/999')
    assert r.status_code == 404

#函数名 + 括号 = 执行函数，拿结果​
#只有函数名 = 拿到函数本身，不执行

# def test_add():
#     return {"name":"测试"} 
# data = test_add()
# assert data["name"] == "测试"
@allure.epic("pytest 自动化")
@allure.feature("接口测试")
@allure.story("mark标记和筛选")
@allure.title("test_get")
@allure.description("参数为 1 的时候，验证结果")
@pytest.mark.api
def test_get(base_url):
    with allure.step("发送请求"):
        r = requests.get(f'{base_url}/posts/1')
    with allure.step("验证状态码"):    
        assert r.status_code == 200

    with allure.step("验证响应数据"):
        assert r.json()['id'] == 1

@allure.epic("pytest 自动化")
@allure.feature("接口测试")
@allure.story("mark标记和筛选")
@allure.title("test_get_3")
@allure.description("参数为 3 的时候，验证结果")
@pytest.mark.api
def test_get_3(base_url):
    r = requests.get(f'{base_url}/posts/3')
    assert r.status_code == 200

@pytest.mark.api
def test_get_4(base_url):
    r = requests.get(f'{base_url}/posts/4')
    assert r.status_code == 200