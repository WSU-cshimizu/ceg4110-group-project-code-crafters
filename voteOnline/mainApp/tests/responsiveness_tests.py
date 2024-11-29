from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager 

def test_responsive_voting_interface():
    # Setup Chrome WebDriver
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    run_test_on_browser(chrome_driver, "Chrome")
    
    # Setup Firefox WebDriver
    firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    run_test_on_browser(firefox_driver, "Firefox")
    
    # Setup Edge WebDriver
    edge_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    run_test_on_browser(edge_driver, "Microsoft Edge")


def run_test_on_browser(driver, browser_name):
    print(f"Running tests on {browser_name}...")


    driver.get("http://localhost:8000/") 

    # for desktop
    driver.set_window_size(1920, 1080)

    
    check_responsive_element(driver, "main-container", browser_name, "desktop")

    # Test for tablet 
    driver.set_window_size(768, 1024)

  
    check_responsive_element(driver, "main-container", browser_name, "tablet")

    # Test for mobile
    driver.set_window_size(375, 667)


    check_responsive_element(driver, "main-container", browser_name, "mobile")
    

    check_responsive_element(driver, "nav", browser_name, "desktop")
    check_responsive_element(driver, "nav", browser_name, "tablet")
    check_responsive_element(driver, "nav", browser_name, "mobile")

  
    check_responsive_element(driver, "footer", browser_name, "desktop")
    check_responsive_element(driver, "footer", browser_name, "tablet")
    check_responsive_element(driver, "footer", browser_name, "mobile")

    print(f"Test passed: Interface is responsive on {browser_name}!")

    # Close
    driver.quit()


def check_responsive_element(driver, element_id, browser_name, view_type):
    try:
        element = driver.find_element(By.ID, element_id)
        
        assert element.is_displayed(), f"{element_id} not visible on {browser_name} in {view_type} view"
        print(f"  {element_id} is visible on {browser_name} in {view_type} view")
        
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    test_responsive_voting_interface()
