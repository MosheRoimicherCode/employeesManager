from models.department import Department
from presenters.main_window_presenter import MainWindowPresenter
from models.department_da import DepartmentDA

class DepartmentPresenter:
    def __init__(self, model: DepartmentDA, list_view, add_view, edit_view, main_window_presenter: MainWindowPresenter):
        self.model = model
        self.list_view = list_view
        self.add_view = add_view
        self.edit_view = edit_view
        self.main_window_presenter = main_window_presenter

        # Set presenter for views
        self.list_view.set_presenter(self)
        self.add_view.set_presenter(self)
        self.edit_view.set_presenter(self)

        # Load initial data
        self.load_data()

    def load_data(self):
        """Load data into the list view."""
        self.main_window_presenter.set_status_bar_text("Loading departments...")
        self.list_view.clear()
        for department in self.model.get_all():
            self.list_view.add_item(department)
        self.main_window_presenter.set_status_bar_text("Departments loaded successfully.")

    def open_add_view(self):
        """Prepare and display the Add View."""
        self.add_view.dept_name_input.clear()
        self.main_window_presenter.load_panel(self.add_view)

    def open_edit_view(self, department: Department):
        """Prepare and display the Edit View with the selected department's data."""
        self.edit_view.edited_department = department.id
        self.edit_view.dept_name_input.setText(department.deptName)
        self.main_window_presenter.load_panel(self.edit_view)

    def add_department(self, dept_id, dept_name):
        """Add a new department."""
        try:
            department = Department(id=int(dept_id), deptName=dept_name)
            self.model.add(department)
        except ValueError as e:
            print(f"Error converting ID to integer: {e}")
            return
        except Exception as e:
            self.main_window_presenter.set_status_bar_text(f"An error occurred while adding: {e}")
            print(f"An error occurred: {e}")
            return
        self.load_data()
        self.main_window_presenter.set_status_bar_text(f"Department {dept_name} added successfully.")
        self.main_window_presenter.load_panel(self.list_view)

    def update_department(self, dept_id, dept_name):
        """Update an existing department."""
        try:
            department = Department(id=self.edit_view.edited_department, deptName=dept_name)
            self.model.update(department)
        except ValueError as e:
            print(f"Error converting ID to integer: {e}")
            return
        except Exception as e:
            self.main_window_presenter.set_status_bar_text(f"An error occurred while updating: {e}")
            print(f"An error occurred: {e}")
            return
        self.load_data()
        self.main_window_presenter.set_status_bar_text(f"Department {dept_name} updated successfully.")
        self.main_window_presenter.load_panel(self.list_view)

    def delete_department(self, department):
        """Delete the selected department."""
        if self.model.delete(department):
            self.load_data()
            self.main_window_presenter.set_status_bar_text(f"Department {department.deptName} deleted successfully.")
        else:
            self.main_window_presenter.set_status_bar_text(f"Department {department.deptName} is in use and cannot be deleted.")

    def open_list_view(self):
        """Display the list view."""
        self.main_window_presenter.load_panel(self.list_view)

    def filter_table(self):
        """Filter the table rows based on the search bar text and selected column."""
        search_text = self.list_view.search_bar.text().lower()
        selected_column = self.list_view.filter_dropdown.currentIndex()  # Get selected column index

        for row in range(self.list_view.table.rowCount()):
            item = self.list_view.table.item(row, selected_column)
            if item and search_text in item.text().lower():
                self.list_view.table.showRow(row)
            else:
                self.list_view.table.hideRow(row)

