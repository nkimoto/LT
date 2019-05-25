from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# ヘッドレスモードを有効にする（次の行をコメントアウトすると画面が表示される）。
options.add_argument('--headless')
options.add_argument("--no-sandbox")
# ChromeのWebDriverオブジェクトを作成する。
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.google.com/')
print(driver.page_source)
driver.close()
