from controllers import base
from models import user

class MembersHandler(base.BaseHandler):
    def get(self):
        users = user.User.all()
        u_list = ""
        for u in users:
            u_list += """
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
            </tr>
            """ %(u.name + " " + u.last_name, u.pid, u.major, u.number, u.year, u.email)
        self.render("members.html", members = u_list)