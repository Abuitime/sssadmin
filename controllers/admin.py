import base_handler

class AdminHandler(base_handler.BaseHandler):
    def get(self):
        self.render('dash.html')