import allure

from pages.Alerts_Frame_Windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramePage, \
    ModalDialogsPage

@allure.suite('Группа "Alerts"')
class TestAlertsFrameWindows:

    @allure.feature('Подгруппа "Browser Windows"')
    class TestBrowserWindowsPage:

        @allure.title('Тест "Check new tab"')
        def test_new_tab_browser_windows(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            result = browser_windows_page.check_opened_new_tab()
            assert result == True, f'Неверный текст, вернулось {result}'

        @allure.title('Тест "Check new tab window"')
        def test_new_window(self, driver):
            new_browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_browser_windows_page.open()
            text_new_window = new_browser_windows_page.check_opened_new_window()
            assert text_new_window == 'This is a sample page', f'Неверный текст, вернулось {text_new_window}'



    @allure.feature('Подгруппа "Alerts"')
    class TestAlertsPage:

        @allure.title('Тест "Check button "see alert""')
        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == 'You clicked a button'

        @allure.title('Тест "Check button "see alert after 5 second""')
        def test_see_alert_after_five_second(self, driver):
            after_alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            after_alert_page.open()
            result = after_alert_page.check_alert_after_five_second()
            assert result == 'This alert appeared after 5 seconds'

        @allure.title(f'Тест "Check button "confirm box""')
        def test_confirm_alert(self, driver):
            confirm_alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            confirm_alert_page.open()
            alert_text = confirm_alert_page.check_alert_confirm_text()
            assert alert_text == 'Do you confirm action?'

        @allure.title(f'Тест "Check button "confirm box YES""')
        def test_conform_alert_yes(self, driver):
            confirm_alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            confirm_alert_page.open()
            no_alert = confirm_alert_page.check_alert_confirm_button_no()
            assert no_alert == 'Do you confirm action?'

        @allure.title(f'Тест "Check button "confirm box NO""')
        def test_conform_alert_no(self, driver):
            confirm_alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            confirm_alert_page.open()
            yes_alert = confirm_alert_page.check_alert_confirm_button_yes()
            assert yes_alert == 'Do you confirm action?'

        @allure.title(f'Тест "Check button "prompt alert""')
        def test_prompt_alert(self, driver):
            prompt_alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            prompt_alert_page.open()
            text = prompt_alert_page.check_prompt_alert()
            assert text is True, 'чот не так'



    @allure.feature('Подгруппа "Frames"')
    class TestFramesPage:

        @allure.title(f'Тест "Check "frames"')
        def test_frames(self, driver):
            frames_page = FramesPage(driver, 'https://demoqa.com/frames')
            frames_page.open()
            result_frame1 = frames_page.check_frame("frame1")
            result_frame2 = frames_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px']
            assert result_frame2 == ['This is a sample page', '100px', '100px']



    @allure.feature('Подгруппа "Nested Frames"')
    class TestNestedFramePage:

        @allure.title(f'Тест "Check "nested frames"')
        def test_nested_frame(self, driver):
            nested_frames_page = NestedFramePage(driver, 'https://demoqa.com/nestedframes')
            nested_frames_page.open()
            parent_frame, child_frame = nested_frames_page.check_nested_frame()
            assert parent_frame == 'Parent frame'
            assert child_frame == 'Child Iframe'



    @allure.feature('Подгруппа "Modal Dialogs"')
    class TestModalDialogsPage:

        @allure.title(f'Тест "Check "modal dialog"')
        def test_modal_dialog(self, driver):
            modal_dialog_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialog_page.open()
            small_modal_title, small_modal_body = modal_dialog_page.check_simple_modal_dialog()
            large_modal_title, large_modal_body = modal_dialog_page.check_large_modal_dialog()
            assert small_modal_title == 'Small Modal'
            assert small_modal_body == 'This is a small modal. It has very less content'
            assert large_modal_title == 'Large Modal'
            assert large_modal_body == ("Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
                                        "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
                                        "when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
                                        "It has survived not only five centuries, but also the leap into electronic typesetting, remaining "
                                        "essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing "
                                        "Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including "
                                        "versions of Lorem Ipsum.")














