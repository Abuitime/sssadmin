import base_handler
from models import event

class EventsHandler(base_handler.BaseHandler):
    def get(self):
        events = event.Event.all().order('-date')
        e_list = ""

        for e in events:
            e_list += """
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
            </tr>
            """ %(e.title, e.location, e.description, e.date)
        self.render("events.html", events = e_list)

    def post(self):
        name = self.request.get('name')
        date = self.request.get('date')
        location = self.request.get('location')
        description = self.request.get('description')
        if(name and date and location and description):
            e = event.Event.create(name, date, location, description)
            e.put()
            self.redirect("/admin/events")
        else:
            self.render("events.html", name = name, date = date, 
                        location = location, description = description,
                        error = "invalid information")
