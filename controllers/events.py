
from google.appengine.api import users
from controllers import base
from models import event

class EventsHandler(base.BaseHandler):
    def get(self):
        user = users.get_current_user()
        events = event.Event.all()
        e_list = ""

        #list events
        for e in events:
            ebutton = """
                <div class="btn-group"><a href="/admin/initevent?elaunch=%s" 
                class="btn btn-default">Launch</a></div>
            """ %e.eid

            e_list += """
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
            </tr>
            """ %(e.name, e.location, e.description, e.date, ebutton)
        self.render("events.html", events = e_list, logged_user = user.nickname())

    def post(self):
        #create and add event to datastore
        name = self.request.get('ename')
        date = self.request.get('edate')
        location = self.request.get('elocation')
        description = self.request.get('edescription')
        if(name and date and location and description):
            e = event.Event.create(name, date, location, description)
            e.put()
            self.redirect("/admin/events")
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
