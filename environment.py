from selenium import webdriver 
  
def before_all(context):  
    #desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
    desired_capabilities = webdriver.DesiredCapabilities.CHROME
    context.browser = webdriver.Remote(  
        desired_capabilities=desired_capabilities,  
        command_executor="http://localhost:4444/wd/hub"  
    ) 
  
def after_all(context):  
    context.browser.quit() 
