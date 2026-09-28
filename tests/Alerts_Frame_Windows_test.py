from pages.Alerts_Frame_Windows_page import BrowserWindowsPage, AlertsPage, FramesPage


class TestAlertsFrameWindows:
    class TestBrowserWindowsPage:

        def test_new_tab_browser_windows(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            result = browser_windows_page.check_opened_new_tab()
            assert result == True, f'Неверный текст, вернулось {result}'

        def test_new_window(self, driver):
            new_browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_browser_windows_page.open()
            text_new_window = new_browser_windows_page.check_opened_new_window()
            assert text_new_window == 'This is a sample page', f'Неверный текст, вернулось {text_new_window}'




    class TestAlertsPage:


        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == 'You clicked a button'


        def test_see_alert_after_five_second(self, driver):
            after_alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            after_alert_page.open()
            result = after_alert_page.check_alert_after_five_second()
            assert result == 'This alert appeared after 5 seconds'



        def test_conform_alert(self, driver):
            confirm_alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            confirm_alert_page.open()
            alert_text = confirm_alert_page.check_alert_confirm_text()
            assert alert_text == 'Do you confirm action?'


        def test_conform_alert_yes(self, driver):
            confirm_alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            confirm_alert_page.open()
            no_alert = confirm_alert_page.check_alert_confirm_button_no()
            assert no_alert == 'Do you confirm action?'


        def test_conform_alert_no(self, driver):
            confirm_alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            confirm_alert_page.open()
            yes_alert = confirm_alert_page.check_alert_confirm_button_yes()
            assert yes_alert == 'Do you confirm action?'


        def test_prompt_alert(self, driver):
            prompt_alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            prompt_alert_page.open()
            text = prompt_alert_page.check_prompt_alert()
            assert text is True, 'чот не так'


    class TestFramesPage:

        def test_frames(self, driver):
            frames_page = FramesPage(driver, 'https://demoqa.com/frames')
            frames_page.open()
            result_frame1 = frames_page.check_frame("frame1")
            result_frame2 = frames_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px']
            assert result_frame2 == ['This is a sample page', '100px', '100px']








