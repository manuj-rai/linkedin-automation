from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# LinkedIn Credentials
LINKEDIN_EMAIL = "email_id"
LINKEDIN_PASSWORD = "password"

# Setup WebDriver
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--disable-webrtc")
options.add_argument('--ignore-certificate-errors')
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 15)  # Explicit wait

# Function to log in to LinkedIn
def login_to_linkedin():
    driver.get("https://www.linkedin.com/login")
    
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(LINKEDIN_EMAIL)
    driver.find_element(By.ID, "password").send_keys(LINKEDIN_PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'feed')]")))  # Wait until login is successful
    print("✅ Successfully logged in.")

# Function to scroll down to load more invitations
def scroll_down():
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    print("✅ Finished scrolling.")

# Function to withdraw sent invitations
def withdraw_sent_invitations():
    driver.get("https://www.linkedin.com/mynetwork/invitation-manager/sent/")
    time.sleep(5)
    print("🔎 Current URL:", driver.current_url)

    # Wait for the "Sent invitations" page to load
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Sent Invitations')]")))
        print("✅ 'Sent invitations' page loaded successfully.")
    except:
        print("❌ ERROR: 'Sent Invitations' page did not load. Please check the XPath.")
        driver.quit()
        exit()

    scroll_down()  # Ensure all requests are loaded
    time.sleep(5)  # Let LinkedIn load elements properly

    while True:
        # Refresh list of withdraw buttons
        withdraw_buttons = driver.find_elements(By.XPATH, "//button[contains(@class, 'invitation-card__action-btn') and contains(., 'Withdraw')]")
        print(f"🔹 Found {len(withdraw_buttons)} withdraw buttons.")

        if len(withdraw_buttons) == 0:
            print("✅ No more pending requests.")
            break  # Exit loop when no buttons are left

        for button in withdraw_buttons:
            try:
                wait.until(EC.element_to_be_clickable(button))

                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                time.sleep(1)
                driver.execute_script("arguments[0].click();", button)  # Click withdraw button
                time.sleep(3)  # Allow popup to appear

                # Handle the confirmation popup withdraw button
                try:
                    withdraw_popup_button = wait.until(EC.element_to_be_clickable(
                        (By.XPATH, "//button[contains(@class, 'artdeco-modal__confirm-dialog-btn') and contains(., 'Withdraw')]")
                    ))
                    driver.execute_script("arguments[0].click();", withdraw_popup_button)  # Click confirmation button
                    print("✅ Invitation withdrawn via popup.")
                    time.sleep(2)  # Small delay to prevent too-fast interactions

                except Exception as popup_error:
                    print(f"❌ Error clicking popup withdraw button: {popup_error}")

            except Exception as main_error:
                print(f"❌ Error clicking withdraw button: {main_error}")

# Main Execution
try:
    login_to_linkedin()
    withdraw_sent_invitations()
finally:
    driver.quit()

