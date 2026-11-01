from pages.Interactions_page import SortablePage, SelectablePage


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