from selenium.webdriver.common.by import By


class SortablePageLocators:

    TAB_LIST = (By.CSS_SELECTOR, "div[id='demo-tabpane-list']")

    LIST_ITEM = (By.CSS_SELECTOR, "div[id='demo-tabpane-list'] div[class='list-group-item list-group-item-action']")

    TAB_GRID = (By.CSS_SELECTOR, "div[id='demo-tabpane-grid']")

    GRID_ITEM =(By.CSS_SELECTOR, "div[id='demo-tabpane-grid'] div[class='list-group-item list-group-item-action']")

    BUTTON_LIST = (By.CSS_SELECTOR, 'button[id="demo-tab-list"]')

    BUTTON_GRID = (By.CSS_SELECTOR, 'button[id="demo-tab-grid"]')


class SelectablePageLocators:
        BUTTON_LIST = (By.CSS_SELECTOR, 'button[id="demo-tab-list"]')
        BUTTON_GRID = (By.CSS_SELECTOR, 'button[id="demo-tab-grid"]')

        TAB_LIST = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"]')
        TAB_GRID = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"]')

        LIST_ITEM = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item list-group-item-action"]')
        LIST_GRID = (By.CSS_SELECTOR, 'li[class="list-group-item list-group-item-action"]')

        ACTIVE_ITEM_LIST = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item active list-group-item-action"]')
        ACTIVE_ITEM_GRID = (By.CSS_SELECTOR, 'li[class="list-group-item active list-group-item-action"]')



class ResizablePageLocators:

        # большая коробка с ограничениями по размеру
    RESIZABLE_BOX = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]') # берём высоту и ширину
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, 'div[class="constraint-area"] span[class="react-resizable-handle react-resizable-handle-se"]')

        # маленькая коробка без ограничений по размеру
    RESIZABLE = (By.CSS_SELECTOR, 'div[id="resizable"]') # берём высоту и ширину
    RESIZABLE_HANDLE = (By.CSS_SELECTOR, 'div[class="resizable-nolimit mt-4"] span[class="react-resizable-handle react-resizable-handle-se"]')


class DroppablePageLocators:

    #simple_page
    TAB_SIMPLE = (By.CSS_SELECTOR, 'button[id="droppableExample-tab-simple"]')
    SIMPLE_DRUG = (By.CSS_SELECTOR, '#draggable')
    SIMPLE_DROP = (By.CSS_SELECTOR, '#simpleDropContainer #droppable')

    #accept_page
    TAB_ACCEPT = (By.CSS_SELECTOR, 'button[id="droppableExample-tab-accept"]')
    ACCEPTABLE_DRUG = (By.CSS_SELECTOR, 'div[id="acceptable"]')
    NOT_ACCEPTABLE_DRUG = (By.XPATH, '//*[@id="acceptDropContainer"]/div[1]/div[2]')
    ACCEPTABLE_DROP = (By.XPATH, '//*[@id="acceptDropContainer"]/div[2]/p')


    #prevent_propogation_page
    TAB_PREVENT = (By.CSS_SELECTOR, 'button[id="droppableExample-tab-preventPropogation"]') # кнопка
    PREVENT_DRUG = (By.CSS_SELECTOR, 'div[id="dragBox"]') # drug - то шо тянем
    # верхний дроп
    NOT_GREEDY_DROP_BOX_TEXT = (By.XPATH, '//*[@id="notGreedyDropBox"]/p')
    NOT_GREEDY_INNER_BOX = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"] p')
    # нижний дроп
    GREEDY_DROP_BOX_TEXT = (By.XPATH, '//*[@id="greedyDropBox"]/p')
    GREEDY_INNER_BOX = (By.XPATH, '//*[@id="greedyDropBoxInner"]/p')

    #revent_draggable_page
    TAB_REVERT = (By.CSS_SELECTOR, 'button[id="droppableExample-tab-revertable"]')
    WILL_REVENT_DRUG = (By.CSS_SELECTOR, '#revertable')
    NOT_REVENT_DRUG = (By.CSS_SELECTOR, '#notRevertable')
    REVENT_DROP = (By.CSS_SELECTOR, '#revertableDropContainer #droppable')


class DragabblePageLocators:


 #SIMPLE
    TAB_SIMPLE = (By.CSS_SELECTOR, '#draggableExample-tab-simple')
    DRUG_SIMPLE = (By.CSS_SELECTOR, '#dragBox') #style

 #AXIS
    TAB_AXIS_REST = (By.CSS_SELECTOR, '#draggableExample-tab-axisRestriction')
    X_DRUG_AXIS_REST = (By.CSS_SELECTOR, '#restrictedX')
    Y_DRUG_AXIS_REST = (By.CSS_SELECTOR, '#restrictedY')

 #CONTAINER
    TAB_CONTAINER_REST = (By.CSS_SELECTOR, '#draggableExample-tab-containerRestriction')
    DRUG_CONTAINER_BOX = (By.CSS_SELECTOR, '#containmentWrapper div[class="draggable ui-widget-content ui-draggable ui-draggable-handle"]')
    DRUG_CONTAINER_PARENT = (By.CSS_SELECTOR, 'span[class="ui-widget-header ui-draggable ui-draggable-handle"]')

 #CURSOR
    TAB_CURSOR = (By.CSS_SELECTOR, '#draggableExample-tab-cursorStyle')
    DRUG_CENTER_STICK = (By.CSS_SELECTOR, '#cursorCenter')
    DRUG_TOP_LEFT_STICK = (By.CSS_SELECTOR, '#cursorTopLeft')
    DRUG_BUTTON_STICK = (By.CSS_SELECTOR, '#cursorBottom')






































