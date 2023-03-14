import time

from behave import given, then, when
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@given(u'I open application URL in the browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.asianpaints.com/")
    context.driver.maximize_window()


@then(u'i click on the view cart tab so it will open')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"header-minicart\"]/div/button").click()
    time.sleep(10)
    context.driver.quit()


@given(u'i click on search bar to search the paint name')
def step_impl(context):
    context.driver.find_element(By.NAME, "q").send_keys("lucid dream")
    context.driver.find_element(By.CLASS_NAME, "js-header-search-handle").click()


@when(u'i click the paint name it redirects to paint page')
def step_impl(context):
    context.driver.find_element(By.XPATH,
                                "/html/body/div[1]/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[1]/div/div[2]/div/a[1]/div").click()
    context.driver.find_element(By.ID, "checkPincode").send_keys("600037")
    context.driver.find_element(By.XPATH,
                                "/html/body/div[1]/div/div[2]/div/div[2]/div/div[7]/div/form/div[1]/div[1]/button").click()
    context.driver.find_element(By.ID, "add-to-cart-click").click()
    time.sleep(10)
    element_to_hover_over = context.driver.find_element(By.XPATH, "//*[@id=\"headerNav\"]/div[1]/ul/li[1]/a[2]/span[1]")
    actions = ActionChains(context.driver)
    actions.move_to_element(element_to_hover_over).perform()
    time.sleep(5)
    context.driver.find_element(By.LINK_TEXT, "Exterior Textures").click()
    context.driver.find_element(By.XPATH, "//*[@id=\"plpListing\"]/section[2]/div[2]/ul/li[2]/a/span").click()
    time.sleep(4)
    context.driver.find_element(By.XPATH, "//*[@id=\"checkPincode\"]").send_keys("600037")
    time.sleep(5)
    context.driver.execute_script("window.scrollTo(0,400);")
    time.sleep(3)
    context.driver.find_element(By.XPATH,
                                "/html/body/div[1]/div/div[2]/div/div[2]/div/div[8]/div/form/div[1]/div[1]/button").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH,
                                "/html/body/div[1]/div/div[2]/div/div[2]/div/div[8]/div/div[1]/div[3]/button").click()


@then(u'product will be added to view cart tab')
def step_impl(context):
    context.driver.quit()


@then(u'click on remove button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"header-minicart\"]/div/button").click()
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//*[@id=\"header-minicart\"]/div/div/div/ul/li[1]/span").click()
    time.sleep(10)


@then(u'i click on increase button so, the product quantity will increase')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"header-minicart\"]/div/button").click()
    for a in range(14):
        context.driver.find_element(By.XPATH,
                                    "//*[@id=\"header-minicart\"]/div/div/div/ul/li[1]/div/div/div/div/span[2]/button").click()
    for b in range(10):
        context.driver.find_element(By.XPATH,
                                    "//*[@id=\"header-minicart\"]/div/div/div/ul/li[2]/div/div/div/div/span[2]/button").click()


@then(u'i click on decrease button so, the product decrease')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"header-minicart\"]/div/button").click()
    for a in range(14):
        context.driver.find_element(By.XPATH, "//*[@id=\"header-minicart\"]/div/div/div/ul/li[1]/div/div/div/div/span["
                                              "2]/button").click()
    for b in range(10):
        context.driver.find_element(By.XPATH, "//*[@id=\"header-minicart\"]/div/div/div/ul/li[2]/div/div/div/div/span["
                                              "2]/button").click()
    for c in range(10):
        context.driver.find_element(By.ID, "cart-quantity-minus0").click()
    for d in range(5):
        context.driver.find_element(By.ID, "cart-quantity-minus1").click()


@when(u'i click on the view cart tab so it will open')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"header-minicart\"]/div/button").click()


@when(u'i click on start shopping option')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, "ctaText").click()


@then(u'it redirects to start shopping page')
def step_impl(context):
    context.driver.quit()


@then(u'i can see the total amount in view cart tab')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"header-minicart\"]/div/button").click()
    context.driver.find_element(By.XPATH, "//*[@id=\"header-minicart\"]/div/div/div/div[2]/h2/span")
    context.driver.find_element(By.XPATH, "//*[@id=\"header-minicart\"]/div/div/div/div[2]/h2/label")


@then(u'i click on checkout option')
def step_impl(context):
    context.driver.find_element(By.XPATHs, "//*[@id=\"header-minicart\"]/div/button").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//*[@id=\"header-minicart\"]/div/div/div/div[2]/div/div/a").click()
    context.driver.find_element(By.ID, "loginMobile").send_keys("8668129276")
    context.driver.find_element(By.ID, "loginMobile").submit()
    time.sleep(30)


@then(u'i click on product so, it redirects to product page')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"header-minicart\"]/div/button").click()
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//*[@id=\"header-minicart\"]/div/div/div/ul/li[1]/a/img").click()
