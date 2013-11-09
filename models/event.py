from google.appengine.ext import db

class Event(db.Model):
    name = db.StringProperty(required = True)
    date = db.StringProperty(required = True)
    location = db.StringProperty(required = True)
    description = db.Text()
    participants = db.Text()

    @classmethod
    def create(cls, name, date, location, description, participants):
        return User(name = name,
                    date = date,
                    location = location,
                    description = description,
                    participants = participants)

    def by_date(cls, date):
        e = Event.all().filter('date =', date).get()
        return e

    def by_name(cls, name):
        e = Event.all().filter('name =', name).get()
        return e
