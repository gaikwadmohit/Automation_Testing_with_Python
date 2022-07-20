class Locators():
    #loginPage
    username_textbox_ID = "email"
    passward_textbox_Name = "pass"
    login_button_Name = "login"

    #homepage
    select_home_logo = "//a[@aria-label='Home']"
    click_photo_video= "//span[contains(text(),'Photo/video')]"
    click_emoji = "(//i[@class='hu5pjgll bixrwtb6'])[4]"
    click_on_happy = "//div[contains(text(),'happy')]"
    click_on_post_button = "//span[contains(text(),'Post')]"



    #profile Page
    click_on_profilename = "//span[contains(text(),'Mohit Gaikwadmohit')]"
    click_on_post = "//span[contains(text(),'Posts')]"
    click_on_about = "//span[contains(text(),'About')]"
    click_on_friends = "//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w " \
                       "c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v lrazzd5p m9osqain'][" \
                       "normalize-space()='Friends'] "
    click_on_photos = "//span[contains(text(),'Photos')]"
    click_on_videos = "//span[contains(text(),'Videos')]"
    click_on_checkin = "//span[contains(text(),'Check-ins')]"



    #homepage2
    select_home_logo1 = "//a[@aria-label='Home']"
    click_on_findFriends = "//span[contains(text(),'Find Friends')]"
    click_on_menuBox = "//div[@aria-label='Menu']//*[name()='svg']"
    click_on_masanger = "(//*[name()='svg'])[10]"
    click_on_notification = "(//*[name()='path'])[13]"
    logo_button_logo = "(//*[name()='image'])[1]"
    logout_button_Link = "(//span[normalize-space()='Log Out'])[1]"
