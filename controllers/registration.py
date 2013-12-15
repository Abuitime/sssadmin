from controllers import base
from models import user

import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')

def valid_username(username):
    return username and USER_RE.match(username)

def valid_password(password):
    return password and PASS_RE.match(password)

def valid_email(email):
    return not email or EMAIL_RE.match(email)

def valid_pid(pid):
    if len(pid) != 8:
        return False
    return True 

def valid_number(number):
    if len(number) != 10:
        return False
    return True

class RegistrationHandler(base.BaseHandler):
    def get(self):
        if self.request.get('pid'):
            self.render("signup.html", pid = self.request.get('pid'))
        else:
            self.redirect("/admin/swipe?msg=nopid")

    def post(self):
        have_error = False
        self.name = self.request.get('name')
        self.last_name = self.request.get('last_name')
        self.pid = self.request.get('pid')
        self.email = self.request.get('email')
        self.major = self.request.get('major')
        self.year = self.request.get('year')
        self.number = self.request.get('number')

        params = dict(name = self.name,
                      last_name = self.last_name,
                      pid = self.pid,
                      email = self.email,
                      major = self.major,
                      year = self.year,
                      number = self.number,
                      )

        if not self.name or not self.last_name:
            params['error_name'] = "That's not a complete name."
            have_error = True
        if not self.major:
            params['error_major'] = "Please select a major."
            have_error = True
        if not self.year:
            params['error_year'] = "Please select your year."
            have_error = True
        if not valid_email(self.email):
            params['error_email'] = "That's not a valid email."
            have_error = True
        if not valid_pid(self.pid):
            params['error_pid'] = "That's not a valid PID."
            have_error = True
        if not valid_number(self.number):
            params['error_number'] = "That's not a valid phone number."
            have_error = True
        if have_error:
            self.render('signup.html', **params)
        else:
            self.done()

    def done(self):
        #make sure the user doesn't already exist
        u = user.User.by_pid(self.pid)
        if u:
            msg = 'That user already exists.'
            self.render('signup.html', error_exists = msg)
        else:
            u = user.User.register(self.pid, self.name, self.last_name, self.major, self.email, self.number, self.year)
            u.put()

            user.User.login(self, self.pid)
            self.redirect('/?user=%s' %(u.name))

