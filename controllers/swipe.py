from controllers import base
from models import user
from models import event
from types import NoneType

def valid_pid(pid):
    if len(pid) != 8:
        return False
    return True 

class SwipeHandler(base.BaseHandler):
	def get(self):
		e = self.session.get('event')
		if not e or event.Event.by_eid(e):
			self.redirect("/admin")

		if self.request.get('user'):
			user = self.request.get('user')
			msg = ("Welcome " + user + "!")
			self.render("index.html", message = msg)
		else:
			self.render("index.html", message = "")

	def post(self):
		e = self.session.get('event')
		if not e:
			self.redirect("/admin")
		pid = self.request.get('pid')
		if(len(pid) == 10):
			pid = pid[2:10]

		if not valid_pid(pid):
			msg = 'Invalid PID'
			self.render('index.html', message = msg)   
		else:
			#User.login should take care of checking in user to event so modify method in user.py to fit need
			u = user.User.login(self, pid)
			if u:
				self.redirect('/admin/swipe?user=%s' %u.name)
			else:
				self.redirect('/registration?pid=%s' %pid)