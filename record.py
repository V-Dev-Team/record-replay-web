from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

bundle_dir = Path(__file__).parent

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
options.add_experimental_option("useAutomationExtension", False)
options.add_extension(bundle_dir / "rrweb-extension.zip")

driver = webdriver.Chrome(options=options)

input("Press Enter to close the browser...")
