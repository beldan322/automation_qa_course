import random
import time

from locators.Interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()


    def get_sortable_item(self, element):
        item_list = self.elements_are_visible(element)
        return [item.text for item in item_list]

    def change_list_order(self):
        # self.element_is_visible(self.locators.BUTTON_LIST).click()
        time.sleep(0.2)
        order_before = self.get_sortable_item(self.locators.LIST_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEM), k=2)
        time.sleep(0.2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.drug_and_drop_element(item_what, item_where)
        time.sleep(0.2)
        order_after = self.get_sortable_item(self.locators.LIST_ITEM)
        time.sleep(0.2)
        return order_before, order_after


    def change_grid_order(self):
        self.element_is_visible(self.locators.BUTTON_GRID).click()
        time.sleep(0.2)
        order_before = self.get_sortable_item(self.locators.GRID_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.drug_and_drop_element(item_what, item_where)
        time.sleep(0.2)
        order_after = self.get_sortable_item(self.locators.GRID_ITEM)
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators()


    def random_click(self, element):
        item_list = self.elements_are_visible(element)
        time.sleep(0.3)
        random.sample(item_list, k=3)[0].click()

    def select_list_item(self):
        self.element_is_visible(self.locators.BUTTON_LIST).click()
        time.sleep(0.3)
        self.random_click(self.locators.LIST_ITEM)
        time.sleep(0.3)
        active_element = self.element_is_visible(self.locators.ACTIVE_ITEM_LIST)
        return active_element.text

    def select_grid_item(self):
        self.element_is_visible(self.locators.BUTTON_GRID).click()
        time.sleep(0.3)
        self.random_click(self.locators.LIST_GRID)
        time.sleep(0.3)
        active_element = self.element_is_visible(self.locators.ACTIVE_ITEM_GRID)
        return active_element.text





class ResizablePage(BasePage):
    locators = ResizablePageLocators()


    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height


    def get_max_mix_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value


    def change_size_resizable_box(self):
        time.sleep(0.2)
        self.action_drug_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        time.sleep(0.2)
        max_size = self.get_px_from_width_height(self.get_max_mix_size(self.locators.RESIZABLE_BOX))
        self.action_drug_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE), -500, -300)
        time.sleep(0.2)
        min_size = self.get_px_from_width_height(self.get_max_mix_size(self.locators.RESIZABLE_BOX))
        time.sleep(0.2)
        return max_size, min_size


    def change_size_resizable(self):
        time.sleep(0.2)
        self.action_drug_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE), random.randint(1, 300), random.randint(1, 300))
        time.sleep(0.2)
        max_size = self.get_px_from_width_height(self.get_max_mix_size(self.locators.RESIZABLE))
        self.action_drug_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE), random.randint(-200, -1), random.randint(-200, -1))
        time.sleep(0.2)
        min_size = self.get_px_from_width_height(self.get_max_mix_size(self.locators.RESIZABLE))
        time.sleep(0.2)
        return max_size, min_size


























































