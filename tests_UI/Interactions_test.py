import allure

from pages.Interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DragabblePage

@allure.suite('Группа "Interactions"')
class TestInteractions:

    @allure.feature('Подгруппа "Sortable"')
    class TestSortablePage:

        @allure.title('Тест "Check sortable list"')
        def test_sortable_list(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            before, after = sortable_page.change_list_order()
            assert before != after, 'они равны, либо перезапусти функцию либо перепроверь селекторы'

        @allure.title('Тест "Check sortable grid"')
        def test_sortable_grid(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            before, after = sortable_page.change_grid_order()
            assert before != after, 'они равны, либо перезапусти функцию либо перепроверь селекторы'


    @allure.feature('Подгруппа "Selectable"')
    class TestSelectablePage:

        @allure.title('Тест "Check selectable list"')
        def test_selectable_list(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            active = selectable_page.select_list_item()
            assert len(active) > 0

        @allure.title('Тест "Check selectable grid"')
        def test_selectable_grid(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            active = selectable_page.select_grid_item()
            assert len(active) > 0


    @allure.feature('Подгруппа "Resizable"')
    class TestResizablePage:

        @allure.title('Тест "Check resizable box"')
        def test_resizable_box(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_size, min_size = resizable_page.change_size_resizable_box()
            assert ('500px', '300px') == max_size,'размеры не сходятся'
            assert ('150px', '150px') == min_size, 'размеры не сходятся'

        @allure.title('Тест "Check resizable"')
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_size, min_size = resizable_page.change_size_resizable()
            assert min_size != max_size, 'размеры равны, либо нехватает размера экрана, чтобы изменить размер'


    @allure.feature('Подгруппа "Droppable"')
    class TestDroppablePage:

        @allure.title('Тест "Check simple drug"')
        def test_simple_drug(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == 'Dropped!', 'не переместилось, либо поменялся текст'

        @allure.title('Тест "Check accept drug"')
        def test_accept_drug(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_accept_drop = droppable_page.not_acceptable_drop()
            accept_drop = droppable_page.acceptable_drop()
            assert not_accept_drop == 'Drop here', 'изменился текст, либо переместилось после accept'
            assert accept_drop == 'Dropped!', 'изменился текст, либо не переместилось'

        @allure.title('Тест "Check prevent propogation"')
        def test_prevent_propogation_drug(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            one, two, three, foure = droppable_page.drop_prevent_propogation()
            assert one == 'Dropped!', 'упав тест, либо не переместилось либо поменялось значение'
            assert two == 'Dropped!', 'упав тест, либо не переместилось либо поменялось значение'
            assert three == 'Dropped!', 'упав тест, либо не переместилось либо поменялось значение'
            assert foure == 'Dropped!', 'упав тест, либо не переместилось либо поменялось значение'

        @allure.title('Тест "Check revent druggable"')
        def test_revent_draggable_drug(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            will_before, will_after = droppable_page.will_revert()
            before, after = droppable_page.not_revert()
            assert will_before != will_after, 'равны, чот не так'
            assert before == after, "неравны, чот не так"


    @allure.feature('Подгруппа "Dragabble"')
    class TestDragabblePage:

        @allure.title('Тест "Check simple dragabble"')
        def test_simple_dragabble(self, driver):
            dragabble_page = DragabblePage(driver, 'https://demoqa.com/dragabble')
            dragabble_page.open()
            before, after = dragabble_page.drug_simple()
            assert before != after , 'они равны или тест упал из-за скорости драйвера'

        @allure.title('Тест "Check axis restricted dragabble"')
        def test_axis_restricted_dragabble(self, driver):
            dragabble_page = DragabblePage(driver, 'https://demoqa.com/dragabble')
            dragabble_page.open()
            before_x, after_x = dragabble_page.drug_axis_x()
            before_y, after_y = dragabble_page.drug_axis_y()
            assert before_x != after_x , 'они равны или тест упал из-за скорости драйвера'
            assert before_y != after_y , 'они равны или тест упал из-за скорости драйвера'

        @allure.title('Тест "Check container restricted dragabble"')
        def test_container_restricted_dragabble(self, driver):
            dragabble_page = DragabblePage(driver, 'https://demoqa.com/dragabble')
            dragabble_page.open()
            before_box, after_box = dragabble_page.drug_container_box()
            before_parent, after_parent = dragabble_page.drug_container_parent()
            assert before_box != after_box , 'они равны или тест упал из-за скорости драйвера'
            assert before_parent != after_parent , 'они равны или тест упал из-за скорости драйвера'

















