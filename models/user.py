from google.appengine.ext import db

class User(db.Model):
    pid = db.StringProperty(required = True)
    name = db.StringProperty(required = True)
    last_name = db.StringProperty(required = True)
    major = db.StringProperty(required = True)
    email = db.StringProperty(required = True)
    number = db.StringProperty(required = True)
    year = db.StringProperty(required = True)

    @classmethod
    def by_name(cls, name):
        u = User.all().filter('name =', name).get()
        return u

    @classmethod
    def by_pid(cls, pid):
        u = User.all().filter('pid =', pid).get()
        return u
        
    @classmethod
    def register(cls, pid, name, last_name, major, email, number, year):
        return User(pid = pid,
                    name = name,
                    last_name = last_name,
                    major = major,
                    email = email,
                    number = number,
                    year = year)

    @classmethod
    def login(cls, pid):
        u = cls.by_pid(pid)
        return u