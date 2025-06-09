import allure
import pytest

from pages.droppable_page import DroppablePage


@allure.epic("UI")
@allure.feature("Страница перетаскивания элементов")
@pytest.mark.smoke
class TestDroppablePage:
    @allure.title("Перетаскивание элемента")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_drag_and_drop_element(self, droppable_page: DroppablePage):
        droppable_page.switch_to_frame()
        droppable_page.drag_and_drop_element()
        droppable_element_text = droppable_page.find_droppable_element().text
        assert droppable_element_text == "Dropped!", \
            f"Некорректный текст принимающего элемента \
                {droppable_element_text}"
