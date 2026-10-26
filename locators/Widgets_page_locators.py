from selenium.webdriver.common.by import By


class AccordianPageLocators:

    SECTION_FIRST = (By.XPATH, '//*[@id="accordianContainer"]/div/div[1]')
    SECTION_SECOND = (By.XPATH, '//*[@id="accordianContainer"]/div/div[2]')
    SECTION_THIRD = (By.XPATH, '//*[@id="accordianContainer"]/div/div[3]')
    SECTION_FIRST_TEXT = (By.XPATH, '//*[@id="accordianContainer"]/div/div[1]/div/div/p')
    SECTION_SECOND_TEXT = (By.XPATH, '//*[@id="accordianContainer"]/div/div[2]/div/div/p')
    SECTION_THIRD_TEXT = (By.XPATH, '//*[@id="accordianContainer"]/div/div[3]/div/div/p')


class AutoCompletePageLocators:

        MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
        MULTI_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__multi-value__label css-9jq23d"]')
        DELETE_MULTI_VALUE = (By.CSS_SELECTOR, "div[role='button']")
        SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
        SINGLE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1dimb5e-singleValue"]')



class DatePickerPageLocators:

    DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, "div[class*='react-datepicker__day react-datepicker__day']")



    TIME_AND_DATE_INPUT = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    TIME_AND_DATE_MONTH = (By.CSS_SELECTOR, 'button[class="react-datepicker__month-read-view"]')
    MONTH_DROPDOWN = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]')
    TIME_AND_DATE_YEAR = (By.CSS_SELECTOR, 'button[class="react-datepicker__year-read-view"]')
    YEAR_DROPDOWN = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-option"]')
    TIME_DROPDOWN = (By.CSS_SELECTOR, 'div[class="react-datepicker__time-box"]')


class SliderPageLocators:


    SLIDER_INPUT = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')




class ProgressBarPageLocators:


    START_BUTTON = (By.CSS_SELECTOR, 'button[id="startStopButton"][class="mt-3 btn btn-primary"]')
    VALUE_BAR = (By.CSS_SELECTOR, 'div[class="progress-bar bg-info"]')



class TabsPageLocators:

    WHAT_TABS = (By.CSS_SELECTOR, 'button[id="demo-tab-what"]')
    ORIGIN_TABS = (By.CSS_SELECTOR, 'button[id="demo-tab-origin"]')
    USE_TABS = (By.CSS_SELECTOR, 'button[id="demo-tab-use"]')

    TEXT_WHAT_TAB = (By.CSS_SELECTOR, 'div[id="demo-tabpane-what"]')
    TEXT_ORIGIN_TAB = (By.CSS_SELECTOR, 'div[id="demo-tabpane-origin"]')
    TEXT_USE_TAB = (By.CSS_SELECTOR, 'div[id="demo-tabpane-use"]')


class ToolTipsLocators:


    BOTTON_HOVER = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    TOOL_TIP_BUTTON = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')


    INPUT_HOVER = (By.CSS_SELECTOR, 'input[id="toolTipTextField"]')
    TOOL_TIP_INPUT = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')

    CONTRARY_HOVER = (By.XPATH, "//*[.='Contrary']")
    TOOL_TIP_CONTRARY = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')

    SECTION_HOVER = (By.XPATH, "//*[.='1.10.32']")
    TOOL_TIP_SECTION = (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')

    TOOL_TIP_INNERS = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]') # You hovered over the Button
                                                                      # You hovered over the text field
                                                                      # You hovered over the Contrary
                                                                      # You hovered over the 1.10.32



