import random
import time

import allure

from locators.Interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DragabblePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    @allure.step('Получение сортированного элемента')
    def get_sortable_item(self, element):
        item_list = self.elements_are_visible(element)
        return [item.text for item in item_list]

    @allure.step('Получение списка элементов')
    def change_list_order(self):
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

    @allure.step('Получение списка элементов из сетки')
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

    @allure.step('Случайный клик по элементу из списка')
    def random_click(self, element):
        item_list = self.elements_are_visible(element)
        time.sleep(0.3)
        random.sample(item_list, k=3)[0].click()

    @allure.step('Выбор элемента из списка')
    def select_list_item(self):
        self.element_is_visible(self.locators.BUTTON_LIST).click()
        time.sleep(0.3)
        self.random_click(self.locators.LIST_ITEM)
        time.sleep(0.3)
        active_element = self.element_is_visible(self.locators.ACTIVE_ITEM_LIST)
        return active_element.text

    @allure.step('Выбор элемента из сетки')
    def select_grid_item(self):
        self.element_is_visible(self.locators.BUTTON_GRID).click()
        time.sleep(0.3)
        self.random_click(self.locators.LIST_GRID)
        time.sleep(0.3)
        active_element = self.element_is_visible(self.locators.ACTIVE_ITEM_GRID)
        return active_element.text





class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    @allure.step('Получение высоты и ширины пикселей')
    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    @allure.step('Получение максимального и минимального значения пикселей')
    def get_max_mix_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    @allure.step('Выбор размера изменяемой области "box"')
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

    @allure.step('Выбор размера изменяемой области "resizable"')
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

    @allure.step('"Simple"-Перемещение drug в drop')
    def drop_simple(self):
        drug_div = self.element_is_visible(self.locators.SIMPLE_DRUG)
        drop_div = self.element_is_visible(self.locators.SIMPLE_DROP)
        time.sleep(0.5)
        self.drug_and_drop_element(drug_div, drop_div)
        time.sleep(0.5)
        return drop_div.text

    @allure.step('"Accept"-Перемещение not_accept_drug в drop')
    def not_acceptable_drop(self):
        self.element_is_visible(self.locators.TAB_ACCEPT).click()
        drug_div = self.element_is_visible(self.locators.NOT_ACCEPTABLE_DRUG)
        drop_div = self.element_is_visible(self.locators.ACCEPTABLE_DROP)
        time.sleep(0.5)
        self.drug_and_drop_element(drug_div, drop_div)
        time.sleep(0.5)
        return drop_div.text

    @allure.step('"Accept"-Перемещение accept_drug в drop')
    def acceptable_drop(self):
        self.element_is_visible(self.locators.TAB_ACCEPT).click()
        drug_div = self.element_is_visible(self.locators.ACCEPTABLE_DRUG)
        drop_div = self.element_is_visible(self.locators.ACCEPTABLE_DROP)
        time.sleep(0.5)
        self.drug_and_drop_element(drug_div, drop_div)
        time.sleep(0.5)
        return drop_div.text

    @allure.step('"Prevent"-Перемещение drug в  two drop')
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

    @allure.step('"Revent"-Перемещение will_drug в drop')
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

    @allure.step('"Revent"-Перемещение no_revent_drug в drop')
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





class DragabblePage(BasePage):
    locators = DragabblePageLocators()

    @allure.step('"Simple"-Перемещение drug в случайное место')
    def drug_simple(self):
        drug_div = self.element_is_visible(self.locators.DRUG_SIMPLE)
        time.sleep(0.4)
        before = drug_div.get_attribute('style')
        time.sleep(0.4)
        self.action_drug_and_drop_by_offset(drug_div, random.randint(100, 1000), random.randint(1, 1000))
        time.sleep(0.4)
        after = drug_div.get_attribute('style')
        time.sleep(0.4)
        return before, after

    @allure.step('"Axis"-Перемещение drug по оси X')
    def drug_axis_x(self):
        time.sleep(0.5)
        self.element_is_visible(self.locators.TAB_AXIS_REST).click()
        time.sleep(0.5)
        drug_div = self.element_is_visible(self.locators.X_DRUG_AXIS_REST)
        time.sleep(0.5)
        before = drug_div.get_attribute('style')
        time.sleep(0.5)
        self.action_drug_and_drop_by_offset(drug_div, random.randint(-400, 1100), random.randint(1, 1000))
        time.sleep(0.5)
        after = drug_div.get_attribute('style')
        time.sleep(0.5)
        return before, after

    @allure.step('"Axis"-Перемещение drug по оси Y')
    def drug_axis_y(self):
        time.sleep(0.5)
        self.element_is_visible(self.locators.TAB_AXIS_REST).click()
        time.sleep(0.5)
        drug_div = self.element_is_visible(self.locators.Y_DRUG_AXIS_REST)
        time.sleep(0.5)
        before = drug_div.get_attribute('style')
        time.sleep(0.5)
        self.action_drug_and_drop_by_offset(drug_div, random.randint(-400, 500), random.randint(-200, 600))
        time.sleep(0.5)
        after = drug_div.get_attribute('style')
        time.sleep(0.5)
        return before, after

    @allure.step('"Container"-Перемещение drug внутри коробки "box"')
    def drug_container_box(self):
        self.element_is_visible(self.locators.TAB_CONTAINER_REST).click()
        time.sleep(0.1)
        drug_div = self.element_is_visible(self.locators.DRUG_CONTAINER_BOX)
        time.sleep(0.5)
        before = drug_div.get_attribute('style')
        time.sleep(0.5)
        self.action_drug_and_drop_by_offset(drug_div, random.randint(-100, 2000), random.randint(-100, 1000))
        time.sleep(0.5)
        after = drug_div.get_attribute('style')
        time.sleep(0.5)
        return before, after

    @allure.step('"Container"-Перемещение текста drug внутри маленькой коробки "parent"')
    def drug_container_parent(self):
        time.sleep(1)
        drug_div = self.element_is_visible(self.locators.DRUG_CONTAINER_PARENT)
        time.sleep(0.7)
        before = drug_div.get_attribute('style')
        time.sleep(0.5)
        self.action_drug_and_drop_by_offset(drug_div, random.randint(-1, 100), random.randint(-1, 200))
        time.sleep(0.7)
        after = drug_div.get_attribute('style')
        time.sleep(0.6)
        return before, after



































