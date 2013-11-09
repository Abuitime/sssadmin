from controllers import *
#from controllers import registration
import webapp2


app = webapp2.WSGIApplication([('/', home.HomeHandler),
								('/registration', registration.RegistrationHandler),
								('/admin', admin.AdminHandler),
								('/admin/events', events.EventsHandler),
								('/admin/members', members.MembersHandler)
								], debug=True)
