from pages.drag_and_drop_list_page import DragAndDropListPage

def test_drag_and_drop(page):
    drag_and_drop = DragAndDropListPage(page)

    drag_and_drop.drag_and_drop()
    drag_and_drop.check_drag_and_drop_list()