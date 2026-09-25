from pages.Alerts_Frame_Windows_page import BrowserWindowsPage


class TestAlertsFrameWindows:
    class TestBrowserWindowsPage:

        def test_new_tab_browser_windows(self, driver):
            browser_windows = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows.open()
            result = browser_windows.check_opened_new_tab()
            assert result == True, f'Неверный текст, вернулось {result}'

        def test_new_window(self, driver):
            new_browser_windows = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_browser_windows.open()
            text_new_window = new_browser_windows.check_opened_new_window()
            assert text_new_window == 'This is a sample page', f'Неверный текст, вернулось {text_new_window}'



