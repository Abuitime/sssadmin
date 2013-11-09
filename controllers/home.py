from controllers import base
from models import user

def valid_pid(pid):
    if len(pid) != 8:
        return False
    return True 

class HomeHandler(base.BaseHandler):
	def get(self):
		if self.request.get('user'):
			user = self.request.get('user')
			msg = ("Welcome " + user + "!")
			self.render("index.html", message = msg)
		else:
			#self.response.write("hello world")
			self.render("index.html", message = "")
			#self.response.write(base.template_dir)

	def post(self):
		pid = self.request.get('pid')
		if(len(pid) == 10):
			pid = pid[2:10]

		if not valid_pid(pid):
			msg = 'Invalid PID'
			self.render('index.html', message = msg)   
		else:
			#User.login should take care of checking in user to event so modify method in user.py to fit need
			u = user.User.login(pid)
			if u:
				msg = ("Welcome " + u.name + "!")
				self.render('index.html', message = msg)
			else:
				self.redirect('/registration?pid=%s' %(pid))