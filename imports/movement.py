class Movement:
    breadcrumb = ""
    message = "You aren't anywhere... yet."

    def __init__(self):
        pass

    def where_am_i(self):
        return "home"

    def get_formatted_breadcrumb(self):
        return self.breadcrumb

    def set_breadcrumb(self, value):
        self.breadcrumb = value

    def get_breadcrumb(self):
        return self.breadcrumb

    def set_next_message(self, value):
        self.next_message = value

    def get_message(self):
        return self.next_message
