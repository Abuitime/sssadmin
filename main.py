from controllers import *
import webapp2


app = webapp2.WSGIApplication([('/', home.HomeHandler),
								('/registration', registration.RegistrationHandler),
								('/admin', admin.AdminHandler),
								('/admin/events', events.EventsHandler),
								('/admin/members', members.MembersHandler),
								('/admin/dash', dash.DashHandler)
								], debug=True)
