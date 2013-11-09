from controllers import base_handler
class DashHandler(base_handler.BaseHandler):
	def get(self): 
		#self.response.write("Dash")
		self.render("dash.html",title="SSS Admin")
	def post(self):
		self.response.write("Dash")

