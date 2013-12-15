from google.appengine.api import users
from controllers import base

import jinja2
import os
import urllib
import hmac

class LoginHandler(base.BaseHandler):

	def get(self):
		user = users.get_current_user()

		if user:
			self.render("dash.html", title = "SSS Administration",
									 logged_user = user.nickname(),
									 logout_url = users.create_logout_url('/'))
		else:
			self.redirect(users.create_login_url('/'))
		

