from controllers import base
class DashHandler(base.BaseHandler):
	def get(self): 
		#self.response.write("Dash")
		self.render("dash.html",title="Dashboard")
	def post(self):
		self.response.write("Dash")

