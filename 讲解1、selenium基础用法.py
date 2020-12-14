import time
from selenium import webdriver #导入必要的库
#功能需求：模仿人类使用搜索框进行搜索
# 业务分析：在搜索框中输入“关键字”，点击“百度一下”或者是“回车”

#有头浏览器，有操作界面的浏览器
def f1():
    #chromedriver.exe的存放路径
    driver_path='E:\zhangxu\pythonanzhuang\python-3.9\Scripts\chromedriver.exe'

    # 通过webdriver对象的Chrome方法【不同的浏览器对应不同的方法】，获取到chromedriver.exe
    browser = webdriver.Chrome(executable_path=driver_path)

    # 访问百度
    browser.get("http://www.baidu.com")

    # 根据页面的id值定位到搜索框的
    input_tag = browser.find_element_by_id("kw")

    #假如我们搜索“java”
    input_tag.send_keys("java")

    # 根据页面id获取到“百度一下”按钮
    submit_btn = browser.find_element_by_id("su")

    #这个方法其实就是模仿人们点击“百度一下”按钮或者是“回车”
    submit_btn.click()

    time.sleep(5)
    #关闭当前窗口
    browser.close()


def f2():
    print("111111")


f2()