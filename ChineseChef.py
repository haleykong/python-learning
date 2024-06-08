from Chef import Chef


class ChineseChef(Chef):  # Use Inheritance, can do everything the Chef can do

    def make_special_dish(self):
        print("The chef makes orange chicken")  # Override from Chef

    def make_fried_rice(self):
        print("The chef makes fried rice")
