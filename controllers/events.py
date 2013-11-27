
from google.appengine.api import users
from controllers import base
from models import event

class EventsHandler(base.BaseHandler):
    def get(self):
        user = users.get_current_user()
        events = event.Event.all()
        e_list = ""

        for e in events:
            e_list += """
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
            </tr>
            """ %(e.name, e.location, e.description, e.date)
        self.render("events.html", events = e_list, logged_user = user.nickname())

    def post(self):
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
