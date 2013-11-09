from controllers import *
#from controllers import registration
import webapp2


app = webapp2.WSGIApplication([('/', home.HomeHandler),
								('/registration', registration.RegistrationHandler)]
                                , debug=True)
