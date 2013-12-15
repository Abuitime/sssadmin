
from google.appengine.api import users
from controllers import base
from models import event

class EventsHandler(base.BaseHandler):
    def get(self):
        user = users.get_current_user()
        e = event.Event.all()

        self.render("events.html", events = e, logged_user = user.nickname())

    def post(self):
        #create and add event to datastore
        name = self.request.get('ename')
        date = self.request.get('edate')
        location = self.request.get('elocation')
        description = self.request.get('edescription')
        if(name and date and location and description):
            e = event.Event.create(name, date, location, description)
            e.put()
            self.redirect("/admin/events?new=1")
        else:
            self.render("events.html", name = name, date = date, 
                        location = location, description = description,
                        error = "invalid information")

class InitEventHandler(base.BaseHandler):
    def get(self):
        #add event to session variable
        eid = self.request.get("elaunch")
        if not event.Event.by_eid(eid):
            self.redirect("/admin/events")
        self.session['event'] = eid
        self.redirect("/admin/swipe")

    def post(self):
        self.redirect("/admin/events")

class EditEventHandler(base.BaseHandler):
    def get(self):
        self.redirect("/admin/events")

    def post(self):
        eid = self.request.get("meid")
        event = event.Event.by_eid(eid)
        if not event:
            self.redirect("/admin/events")
        else:
            #update event data and put in datastore
            name = self.request.get('mename')
            date = self.request.get('medate')
            location = self.request.get('melocation')
            description = self.request.get('medescription')
            if(name and date and location and description):
                event.name = name
                event.date = date
                event.location = location
                event.description = description
                event.put()
                self.redirect("/admin/events?edit=1")
            else:
                self.redirect("/admin/events?edit=0")

class DeleteEventHandler(base.BaseHandler):
    def get(self):
        self.redirect("/admin/events")

    def post(self):
        event = event.Event.by_eid(self.request.get("eid"))
        if not event:
            self.redirect("/admin/events?delete=0")
        event.delete()
        self.redirect("/admin/events?delete=1")
