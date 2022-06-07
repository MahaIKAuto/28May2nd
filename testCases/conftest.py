import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome("C://Users//Hi//PycharmProjects//Seleniumproj1307//venv//Scripts//chromedriver.exe")
        # driver=webdriver.Chrome(executable_path ="C://Users//Hi//Desktop//SeleniumProjJune21//chromedriver.exe")
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    elif browser =='ie':
        driver=webdriver.Safari()
        print ("Launching IE Browser")
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################
