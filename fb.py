from selenium.webdriver import Chrome
import urllib.request
from time import sleep
from random import randint
import pandas as pd
from selenium.webdriver.chrome.options import Options
opts = Options()

opts.add_experimental_option("excludeSwitches", ["enable-logging"])
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
opts.add_argument("--disable-infobars")
opts.add_argument("start-maximized")
opts.add_argument("--disable-extensions")
opts.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
opts.add_argument("--ignore-certificate-error")
opts.add_argument("--ignore-ssl-errors")

filename = 'Worksheet9.csv'
photo_folder_path = 'Photos9/'
def Login(d):
    d.get('https://facebook.com')
    sleep(10)
    email = d.find_element_by_xpath("//input[@id='email']")
    # Please replace the email with your email
    email.send_keys('8801641527887')

    password = d.find_element_by_xpath("//input[@id='pass']")
    # Please replace the passowrd with your password
    password.send_keys('lovesociety7575')

    login = d.find_element_by_xpath("//button[@name='login']")
    login.click()

    sleep(randint(7, 13))

df = pd.read_csv(filename)
# nas = df.loc[df['Filename Profile Photo'] == 'n.a'].index.tolist()
# print(len(nas))
count = df['RIDN'].count()
print(count)
def GetPhotos(d,r,u,n,a):
    remarks = ''
    d.get(u)
    sleep(5)
    try:

        try:
            dp_icon = driver.find_element_by_xpath("//div[@class='aovydwv3 j83agx80 wkznzc2l dlu2gh78']/div/a")
            dp_icon.click()
            sleep(5)
        except:

            dp_icon = driver.find_element_by_xpath("//div[@class='aovydwv3 j83agx80 wkznzc2l dlu2gh78']")
            dp_icon.click()
            sleep(5)
            view_dp = driver.find_element_by_xpath("//span[text()='View profile picture']")

            view_dp.click()
        sleep(randint(5,10))
        dp = driver.find_element_by_xpath("//img[@*='media-vc-image']")
        dp_src = dp.get_attribute('src')
        dp_file_name = f"{n}-{a}-logo-square-{r}.jpg"
        dp_file_path = photo_folder_path + dp_file_name
        urllib.request.urlretrieve(dp_src, dp_file_path )
        d.back()
    except Exception as e:
        print(e)
        dp_file_name = 'n.a'
        remarks = 'Profile Photo Not Found.'


    sleep(randint(5, 10))

    try:
        cover_icon = driver.find_element_by_xpath("//img[@*='profileCoverPhoto']")
        d.execute_script("arguments[0].click();", cover_icon)
        sleep(randint(5, 10))
        cover = driver.find_element_by_xpath("//img[@*='media-vc-image']")
        cover_src = cover.get_attribute('src')
        cover_photo_file_name = f"{n}-{a}-logo-cover-{r}.jpg"
        cover_photo_file_path = photo_folder_path + cover_photo_file_name
        urllib.request.urlretrieve(cover_src, cover_photo_file_path )
    except Exception as e:
        print(e)
        cover_photo_file_name = 'n.a'
        remarks = remarks + ' Cover Photo Not Found'
    # sleep(randint(5,10))
    return {'remarks':remarks,'dp_file_name':dp_file_name,'cover_photo_file_name':cover_photo_file_name}
driver = Chrome('C:/users/user/chromedriver/chromedriver.exe',options=opts)
Login(driver)
x = 0
for i in range(428,600):
    print(i)
    ridn = df.loc[i,'RIDN'].replace('/','')
    fb_page_url = df.loc[i,'Facebook Page URL'].replace('/business.','/www.').replace('/m.','/www.').replace("https//","http://https//")
    try:
        name = df.loc[i,'Name'].replace('/','').replace(':',' ').replace('|','')
    except:
        name = 'Untitled'

    additional = str(df.loc[i,'Additional']).replace('/','')
    print(f'{name}-{additional}-logo-square-{ridn}')
    print(fb_page_url)
    fdata = GetPhotos(driver,ridn,fb_page_url,name,additional)
    for k,v in fdata.items():
        print(f'{k}:{v}')
    df.loc[i,'Filename Profile Photo'] = fdata['dp_file_name']
    df.loc[i,'Filename Cover Photo'] = fdata['cover_photo_file_name']
    df.to_csv(filename, index=False)
    x = x + 1
    if(x == 100):
        sleep(900)
        x = 0