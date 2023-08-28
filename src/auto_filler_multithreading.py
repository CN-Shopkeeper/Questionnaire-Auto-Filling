from selenium import webdriver  # selenium库
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # 用于延时
import concurrent.futures
import threading

# ! ignored by .gitignore
import environments as env

import questionnaire as ques

# 准备工作

url = env.url_survey  # 此处为你要填写的问卷网 问卷的地址

option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
# 只输出报错
option.add_argument('--log-level=3')


# 本地下载的谷歌浏览器地址
option.binary_location = env.binary_path

# 全局变量
count = 0
count_lock = threading.Lock()  # 创建互斥锁


def fill_a_questionnaire():
    driver = webdriver.Chrome(options=option)
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                           {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
    # 获取问卷答案
    a, b0, b1, c, c7, d = ques.getAnswers()

    # 启动要填写的地址
    driver.get(url)
    questionsBox = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, 'question-box')))
    # print("question", questionsBox, len(questionsBox))

    # 3-8是A
    questionBoxA = questionsBox[3:9]
    for index, boxA in enumerate(questionBoxA):
        radios = WebDriverWait(boxA, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'ws-radio')))
        # print("A{0}有{1}个选项".format(index+1, len(radios)))
        # 获取这一题的答案
        ans_ = a[index]
        for ans in ans_:
            radioIndex = ans-1
            # print("A{0}的答案是{1}".format(index+1, ans))
            driver.execute_script(
                "arguments[0].scrollIntoView();", radios[radioIndex])
            driver.execute_script("arguments[0].click();", radios[radioIndex])
            # time.sleep(0.2)

    # 11是B0
    questionBoxB0 = questionsBox[11: 12]
    for index, boxB0 in enumerate(questionBoxB0):
        radios = WebDriverWait(boxB0, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'ws-radio')))
        # print("B{0}有{1}个选项".format(index, len(radios)))
        # 获取这一题的答案
        ans_ = b0[index]
        for ans in ans_:
            radioIndex = ans-1
            # print("B{0}的答案是{1}".format(index, ans))
            driver.execute_script(
                "arguments[0].scrollIntoView();", radios[radioIndex])
            driver.execute_script("arguments[0].click();", radios[radioIndex])
            # time.sleep(0.2)

    # 12是B1~B24
    questionBoxB1 = questionsBox[12: 13]
    for index, boxB1 in enumerate(questionBoxB1):
        optionRowContents = WebDriverWait(boxB1, 10).until(
            EC.visibility_of_all_elements_located((
                By.CLASS_NAME, 'option-row-content')))
        # print("B{0}有{1}个问题".format(index+1, len(optionRowContents)))
        for index, orc in enumerate(optionRowContents):
            rowStyles = WebDriverWait(orc, 10).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, "circle-icon")))
            # print("B1_{0}有{1}个选项".format(index+1, len(rowStyles)))
            # 获取这一题的答案
            ans_ = b1[index]
            for ans in ans_:
                rowStyle = ans-1
                # print("B{0}的答案是{1}".format(index+1, ans))
                driver.execute_script(
                    "arguments[0].scrollIntoView();", rowStyles[rowStyle])
                driver.execute_script(
                    "arguments[0].click();", rowStyles[rowStyle])
                # time.sleep(0.2)

    # 15~20是C1~C6
    questionBoxC = questionsBox[15: 21]
    for index, boxC in enumerate(questionBoxC):
        if index in [0, 3, 4]:
            # 这几题是单选
            radios = WebDriverWait(boxC, 10).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, 'ws-radio')))
            # print("C{0}是单选，有{1}个选项".format(index+1, len(radios)))
            # 获取这一题的答案
            ans_ = c[index]
            for ans in ans_:
                radioIndex = ans-1
                # print("c{0}的答案是{1}".format(index+1, ans))
                driver.execute_script(
                    "arguments[0].scrollIntoView();", radios[radioIndex])
                driver.execute_script(
                    "arguments[0].click();", radios[radioIndex])
                # time.sleep(0.2)
        elif index in [1, 2, 5]:
            # 这几题是多选
            checkboxs = WebDriverWait(boxC, 10).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, 'ws-checkbox')))
            # print("C{0}是多选，有{1}个选项".format(index+1, len(radios)))
            # 获取这一题的答案
            ans_ = c[index]
            for ans in ans_:
                checkboxIndex = ans-1
                # print("c{0}的答案是{1}".format(index+1, ans))
                driver.execute_script(
                    "arguments[0].scrollIntoView();", checkboxs[checkboxIndex])
                driver.execute_script(
                    "arguments[0].click();", checkboxs[checkboxIndex])
                # time.sleep(0.2)

    # 21是C7
    questionBoxC7 = questionsBox[21: 22]
    for index, boxC7 in enumerate(questionBoxC7):
        matrixRowContents = WebDriverWait(boxC7, 10).until(
            EC.visibility_of_all_elements_located((
                By.CLASS_NAME, 'matrix-row-content')))
        # print("B{0}有{1}个问题".format(index+1, len(matrixRowContents)))
        for index, mrc in enumerate(matrixRowContents):
            optionTds = WebDriverWait(mrc, 10).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, "option-td")))
            anses_ = c7[index]
            for index_, otd in enumerate(optionTds):
                ans_ = anses_[index_]
                symbolItems = WebDriverWait(otd, 10).until(
                    EC.visibility_of_all_elements_located((
                        By.CLASS_NAME, "symbol.minimum")))
                for ans in ans_:
                    itemIndex = ans-1
                    # print("C7_{0}第{1}小问的答案是{2}".format(index+1, index_+1, ans))
                    driver.execute_script(
                        "arguments[0].scrollIntoView();", symbolItems[itemIndex])
                    driver.execute_script(
                        "arguments[0].click();", symbolItems[itemIndex])
                    # time.sleep(0.1)

    # 24是D
    questionBoxD = questionsBox[24: 25]
    for index, boxD in enumerate(questionBoxD):
        optionRowContents = WebDriverWait(boxD, 10).until(
            EC.visibility_of_all_elements_located((
                By.CLASS_NAME, 'option-row-content')))
        # print("D有{0}个问题".format(len(optionRowContents)))
        for index, orc in enumerate(optionRowContents):
            rowStyles = WebDriverWait(orc, 10).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, "circle-icon")))
            # print("B{0}有{1}个选项".format(index+1, len(rowStyles)))
            # 获取这一题的答案
            ans_ = d[index]
            for ans in ans_:
                rowStyle = ans-1
                # print("D{0}的答案是{1}".format(index+1, ans))
                driver.execute_script(
                    "arguments[0].scrollIntoView();", rowStyles[rowStyle])
                driver.execute_script(
                    "arguments[0].click();", rowStyles[rowStyle])
                # time.sleep(0.2)
    # 提交结果
    submit = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "answer-submit-btn")))
    driver.execute_script(
        "arguments[0].scrollIntoView();", submit)
    driver.execute_script(
        "arguments[0].click();", submit)
    time.sleep(10)
    driver.quit()


def worker(thread_id):
    try:
        global count
        for i in range(20):
            print(f"Thread {thread_id}: Iteration {i+1}, started")
            fill_a_questionnaire()
            with count_lock:  # 使用互斥锁来保护对全局变量的访问
                count += 1
                print(
                    f"Thread {thread_id}: Iteration {i+1}, finished, Count {count}")

    except Exception as e:
        print(f"Exception in Thread {thread_id}: {e}")


def main():
    max_threads = 5
    with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
        # 提交任务给线程池执行
        for thread_id in range(max_threads):
            time.sleep(5)
            executor.submit(worker, thread_id)


if __name__ == "__main__":
    main()
