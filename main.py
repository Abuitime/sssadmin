from controllers import *
import webapp2

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}

app = webapp2.WSGIApplication([('/', login.LoginHandler),
								('/registration', registration.RegistrationHandler),
								('/admin', admin.AdminHandler),
								('/admin/events', events.EventsHandler),
								('/admin/initevent' , events.InitEventHandler),
								('/admin/delevent', events.DeleteEventHandler),
								('/admin/editevent', events.EditEventHandler),
								('/admin/members', members.MembersHandler),
								('/admin/dash', dash.DashHandler),
								('/admin/swipe', swipe.SwipeHandler)
								], config=config, debug=True)
