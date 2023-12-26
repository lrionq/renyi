import pytest

import yaml

yaml.safe_load(open("./data.yml"))

def add_function(a, b):
    return a + b


@pytest.mark.parametrize("a,b,expected",
                         yaml.safe_load(open("./data.yml"))["datas"],
                         ids=yaml.safe_load(open("./data.yml"))["myid"])
def test_add(a, b, expected):
    assert add_function(a, b) == expected


def get_datas():
    with open("./data.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["datas"]
        add_ids = datas["myid"]
        return [add_datas, add_ids]


def add_function(a, b):
    return a + b


@pytest.mark.parametrize("a,b,expected",
                         get_datas()[0],
                         ids=get_datas()[1])
def test_add(a, b, expected):
    assert add_function(a, b) == expected

def step1():
    print("打开浏览器")


def step2():
    print("注册新账号")


def step3():
    print("登录新账号")


# 解析测试步骤⽂件
def steps(path):
    with open(path) as f:
        steps = yaml.safe_load(f)
    for step in steps:
        if "step1" in step:
            step1()
        elif "step2" in step:
            step2()
        elif "step3" in step:
            step3()


def test_foo():
    steps("./steps.yml")

