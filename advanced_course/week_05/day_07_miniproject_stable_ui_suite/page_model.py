class DashboardPage:
    def __init__(self) -> None:
        self.user_menu = "get_by_test_id('user-menu')"
        self.save_button = "get_by_role('button', name='Save')"

    def open(self) -> str:
        return "dashboard-opened"
