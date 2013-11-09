from controllers import base
from google.appengine.api import users

class AdminHandler(base.BaseHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            self.render('dash.html')
        else:
            self.redirect(users.create_login_url(self.request.uri))
