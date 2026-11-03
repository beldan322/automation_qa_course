from pages.Interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage


class TestInteractions:


    class TestSortablePage:

        def test_sortable_list(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            before, after = sortable_page.change_list_order()
            assert before != after, 'они равны, либо перезапусти функцию либо перепроверь селекторы'

        def test_sortable_grid(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            before, after = sortable_page.change_grid_order()
            assert before != after, 'они равны, либо перезапусти функцию либо перепроверь селекторы'


    class TestSelectablePage:


        def test_selectable_list(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            active = selectable_page.select_list_item()
            assert len(active) > 0

        def test_selectable_grid(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            active = selectable_page.select_grid_item()
            assert len(active) > 0

    class TestResizablePage:


        def test_resizable_box(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_size, min_size = resizable_page.change_size_resizable_box()
            assert ('500px', '300px') == max_size,'размеры не сходятся'
            assert ('150px', '150px') == min_size, 'размеры не сходятся'


        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_size, min_size = resizable_page.change_size_resizable()
            assert min_size != max_size, 'размеры равны, либо нехватает размера экрана, чтобы изменить размер'


    class TestDroppablePage:

        def test_simple_drug(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == 'Dropped!', 'не переместилось, либо поменялся текст'


        def test_accept_drug(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_accept_drop = droppable_page.not_acceptable_drop()
            accept_drop = droppable_page.acceptable_drop()
            assert not_accept_drop == 'Drop here', 'изменился текст, либо переместилось после accept'
            assert accept_drop == 'Dropped!', 'изменился текст, либо не переместилось'


        def test_prevent_propogation_drug(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            one, two, three, foure = droppable_page.drop_prevent_propogation()
            assert one == 'Dropped!', 'упав тест, либо не переместилось либо поменялось значение'
            assert two == 'Dropped!', 'упав тест, либо не переместилось либо поменялось значение'
            assert three == 'Dropped!', 'упав тест, либо не переместилось либо поменялось значение'
            assert foure == 'Dropped!', 'упав тест, либо не переместилось либо поменялось значение'


        def test_revent_draggable_drug(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            will_before, will_after = droppable_page.will_revert()
            before, after = droppable_page.not_revert()
            assert will_before != will_after, 'равны, чот не так'
            assert before == after, "неравны, чот не так"