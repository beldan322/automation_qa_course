import random
import time

from locators.Interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators
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



class DroppablePage(BasePage):
    locators = DroppablePageLocators

    def drop_simple(self):
        drug_div = self.element_is_visible(self.locators.SIMPLE_DRUG)
        drop_div = self.element_is_visible(self.locators.SIMPLE_DROP)
        time.sleep(0.5)
        self.drug_and_drop_element(drug_div, drop_div)
        time.sleep(0.5)
        return drop_div.text


    def not_acceptable_drop(self):
        self.element_is_visible(self.locators.TAB_ACCEPT).click()
        drug_div = self.element_is_visible(self.locators.NOT_ACCEPTABLE_DRUG)
        drop_div = self.element_is_visible(self.locators.ACCEPTABLE_DROP)
        time.sleep(0.5)
        self.drug_and_drop_element(drug_div, drop_div)
        time.sleep(0.5)
        return drop_div.text

    def acceptable_drop(self):
        self.element_is_visible(self.locators.TAB_ACCEPT).click()
        drug_div = self.element_is_visible(self.locators.ACCEPTABLE_DRUG)
        drop_div = self.element_is_visible(self.locators.ACCEPTABLE_DROP)
        time.sleep(0.5)
        self.drug_and_drop_element(drug_div, drop_div)
        time.sleep(0.5)
        return drop_div.text

    def drop_prevent_propogation(self):
        self.element_is_visible(self.locators.TAB_PREVENT).click()
        drug_div = self.element_is_visible(self.locators.PREVENT_DRUG)
        not_greedy_drop_dox_div = self.element_is_visible(self.locators.NOT_GREEDY_DROP_BOX_TEXT)
        not_greedy_inner_div = self.element_is_visible(self.locators.NOT_GREEDY_INNER_BOX)
        greedy_drop_dox_div = self.element_is_visible(self.locators.GREEDY_DROP_BOX_TEXT)
        greedy_inner_div =  self.element_is_visible(self.locators.GREEDY_INNER_BOX)
        time.sleep(0.5)
        self.drug_and_drop_element(drug_div, not_greedy_drop_dox_div)
        time.sleep(0.5)
        self.drug_and_drop_element(drug_div, not_greedy_inner_div)
        time.sleep(0.5)
        self.drug_and_drop_element(drug_div, greedy_inner_div)
        time.sleep(0.5)
        self.drug_and_drop_element(drug_div, greedy_drop_dox_div)
        time.sleep(0.5)
        return not_greedy_drop_dox_div.text, not_greedy_inner_div.text, greedy_inner_div.text, greedy_drop_dox_div.text


    def will_revert(self):
        self.element_is_visible(self.locators.TAB_REVERT).click()
        time.sleep(0.5)
        drug_div = self.element_is_visible(self.locators.WILL_REVENT_DRUG)
        time.sleep(0.5)
        drop_div = self.element_is_visible(self.locators.REVENT_DROP)
        time.sleep(0.5)
        self.drug_and_drop_element(drug_div, drop_div)
        position_after_move = drug_div.get_attribute('style')
        time.sleep(1)
        position_after_revert = drug_div.get_attribute('style')
        return position_after_move, position_after_revert


    def not_revert(self):
        self.element_is_visible(self.locators.TAB_REVERT).click()
        time.sleep(0.5)
        drug_div = self.element_is_visible(self.locators.NOT_REVENT_DRUG)
        time.sleep(0.5)
        drop_div = self.element_is_visible(self.locators.REVENT_DROP)
        time.sleep(0.5)
        self.drug_and_drop_element(drug_div, drop_div)
        position_after_move = drug_div.get_attribute('style')
        time.sleep(1)
        position_after_revert = drug_div.get_attribute('style')
        return position_after_move, position_after_revert




















































