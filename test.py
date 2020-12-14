from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import re
from selenium import webdriver  # 导入必要的库
from selenium.webdriver.support import expected_conditions as EC

option = webdriver.ChromeOptions()
option.add_argument("headless")
# chromedriver.exe的存放路径
driver_path = 'E:\zhangxu\pythonanzhuang\python-3.9\Scripts\chromedriver.exe'

# 通过webdriver对象的Chrome方法【不同的浏览器对应不同的方法】，获取到chromedriver.exe
# browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
browser_1 = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
# browser_2 = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

# browser = webdriver.Chrome(executable_path=driver_path)
# browser_1 = webdriver.Chrome(executable_path=driver_path)
browser_2 = webdriver.Chrome(executable_path=driver_path)


time.sleep(3)

class Author:
    def __init__(self, name, title, department, homepage, papers, citation, hindex, interests):
        self.name = name
        self.title = title
        self.department = department
        self.homepage = homepage
        self.papers = papers
        self.citation = citation
        self.hindex = hindex
        self.interests = interests

    def print(self):
        print(self.name, self.title, self.department, self.homepage, self.papers, self.citation, self.hindex, self.interests)

# 抓取【个人主页】的详细信息
def author_info_scratch(url):
    browser_2.get(url)
    # time.sleep(5)

    # print(browser_2.page_source)

    # username=browser_2.find_element_by_id('userPhone')
    # username.clear()
    # username.send_keys('18347989110')
    # password=browser_2.find_element_by_id('phonePassword')
    # password.clear()
    # password.send_keys('aminer9110')
    # loginbtn=browser_2.find_element_by_xpath('//*[@class="ant-btn a-aminer-core-auth-c-login-login-loginBtn a-aminer-core-auth-c-login-login-ready loginBtn"]')
    # loginbtn.click()
    # time.sleep(3)

    # 作者的各项资料
    try:
        name = WebDriverWait(browser_2, 15).until(EC.presence_of_element_located((By.XPATH,
                                                                                  '/html/body/div/section/main/main/article/section[1]/section[1]/div[1]/div/div[2]/div[1]/h1/span'))
                                                  ).text
        # name = browser_2.find_element_by_xpath(
        #     '/html/body/div/section/main/main/article/section[1]/section[1]/div[1]/div/div[2]/div[1]/h1/span').text
    except:
        name = "no name"


    try:
        title = browser_2.find_element_by_xpath(
            '/html/body/div/section/main/main/article/section[1]/section[1]/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/p[1]/span').text
    except:
        title = "no title"


    try:
        department = browser_2.find_element_by_xpath(
            '/html/body/div/section/main/main/article/section[1]/section[1]/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/p[2]/textarea').text
    except:
        department = "no department"


    try:
        # details=browser_2.find_element_by_xpath('//*[@class="expert_info_content"]')
        # homepage=details.find_elements_by_xpath('//*[@class="homepage baseInfo"]')
        # h=[]
        # for url in homepage:
        #     h=h+[url.text]
        #     print(h)
        # homepage=h

        #——————————————————re 正则表达式写法——————————————————————————————————
        url_list = re.findall('"url":\"(.*?)\"', browser_2.page_source, re.S)
        homepage=[]
        for url in url_list:
            homepage=homepage+[url.replace("\\u002F", "/")]
    except:
        homepage="no homepage"


    try:
        papers = re.findall('"pubs":(.*?)}', browser_2.page_source, re.S)
    except:
        papers = "no papers"


    try:
        citation = re.findall('"citations":(.*?),', browser_2.page_source, re.S)
    except:
        citation = "no citation"


    try:
        hindex = re.findall('"hindex":(.*?),', browser_2.page_source, re.S)
    except:
        hindex = "no hindex"


    try:
        interests = browser_2.find_elements_by_class_name("nv-legend-text")
        interests_list = []
        for span in interests:
            interests_list = interests_list + [span.text]
        interests=interests_list
    except:
        interests = "no interests"


    author = Author(name, title, department, homepage, papers, citation, hindex, interests)
    author.print()


# 挨个点击【作者列表】，进入【个人主页】后调用author_info_scratch
def author_list(url):
    browser_1.get(url)
    for num in range(6):

        time.sleep(2)


        # b=browser_1.find_elements_by_xpath('/html/body/div[2]/div/div/ul/li[5]')
        # b.click()

        # num=browser_1.find_element_by_xpath('/html/body/div/section/main/main/article/div[2]/div[3]/div[1]/div[2]/div[1]/div[3]/div[2]/div[2]/ul/li[2]').text
        # print(num)
        # links = browser_1.find_elements_by_xpath(
        #     '/html/body/div[1]/section/main/main/article/div[2]/div[3]/div[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div//div[@class="person_name"]//*[@href]')
        #
        # for span in links:
        #     # rightnowwindow=browser.current_window_handle
        #     # print("rightnowwindow:",rightnowwindow)
        #     print(span)
            # print(span.get_attribute("href"))
            # author_info_scratch(span.get_attribute("href"))

        # a = browser_1.find_element_by_xpath(
        #     '/html/body/div[1]/section/main/main/article/div[2]/div[3]/div[1]/div[2]/div[1]/div[3]/div[3]/div[2]/ul/li[9]/a')
        # a.click()

        print("a爬取到了", num)

# author_list('https://www.aminer.cn/search/person?domain=143&t=b')
author_info_scratch('https://www.aminer.cn/profile/thomas-s-huang/53f48abedabfaea6fb77b490')



Subjects = [   #学科名    学科id   论文数
    ["哲学","12a032cb000c000",152],
    ["经济学","12a032e1000d000",978],
    ["法学","12a0343f0002000",1030],
    ["教育学","12a0345b0008000",526],
    ["文学","12a034700009000",1643],
    ["理学","12a034960010000",3343],
    #["历史学","12a03484000a000",5], 太少了，懒得下载
    # ["工学","12a034a70011000",32954],   下面都是工学。。。工学论文较多 进行分解，
    ["力学","1494ebd8000034c351",1201],
    ["机械工程","1494ec3000003ac351",4397],
    ["光学工程","12a15e740034000",1631],
    ["仪器科学与技术","1494eca2000042c351",805],
    ["动力工程及工程热物理","1494ed5400004cc351",981],
    ["电气工程", "12a16a6b0008000", 149],
    ["矿业工程", "1494f0ec000071c351",223],
    ["交通运输工程", "1494f127000074c351",207],
    ["环境科学与工程", "1494f2c6000087c351",487],
    ["生物医学工程", "12a16c730041000",465],
    ["材料科学与工程", "1494ed12000047c351",1752],
    ["电子科学与技术", "1494edbc000053c351",2301],
    ["信息与通信工程", "1494ee20000059c351",3180],
    ["控制科学与工程", "1494ee7700005ec351",3278],
    ["计算机科学与技术", "1494ef1d000065c351",3278],
    ["化学工程与技术", "1494ef7d00006bc351",2063],
    ["兵器科学与技术", "1494f239000081c351",1791],
    ["航空宇航科学与技术", "1494f1af00007bc351",1649],
    ["软件工程", "1494ef69000069c351",2401],
    #["农学",""], 没有论文
    #["军事学",""],没有论文
    #["医学","12a034c50013000",58],太少了，懒得下载
    ["管理学","12a034e0001a000",9910],
    ["艺术学","12a034ed001b000",571]]

# print(Subjects[1])
# print(Subjects[1][1])

# for i in range(3,5):
#     print(i)