from google.appengine.ext import db

class Event(db.Model):
    eid = db.StringProperty(required = True)
    name = db.StringProperty(required = True)
    date = db.StringProperty(required = True)
    location = db.StringProperty(required = True)
    description = db.TextProperty(required = True)
    participants = db.TextProperty()

    @classmethod
    def create(cls, name, date, location, description):
        return Event(name = name,
                    date = date,
                    location = location,
                    description = description)

    def by_date(cls, date):
        e = Event.all().filter('date =', date).get()
        return e

    def by_name(cls, name):
        e = Event.all().filter('name =', name).get()
        return e

    def by_eid(cls, eid):
        e = Event.all().filter('eid =', eid).get()
        return e
