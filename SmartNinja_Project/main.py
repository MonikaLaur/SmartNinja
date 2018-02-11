#!/usr/bin/env python
import os
import jinja2
import webapp2
import random
import datetime
import model
from google.appengine.api import users
import helper


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}

        user = users.get_current_user()
        params["logged_in"] = bool(user)
        params["user"] = user
        params["login_url"] = users.create_login_url("/")
        params["logout_url"] = users.create_logout_url("/")

        #
        # if user:
        #     visitor = model.User.query(model.User.email == user.nickname()).fetch()
        #     if not visitor:
        #         visitor = model.User(email=user.nickname(),
        #                              admin=False,
        #                              updated=datetime.datetime.utcnow(),
        #                              ip_address=self.request.remote_addr)
        #     else:
        #         visitor = visitor[0]
        #         visitor.updated = datetime.datetime.utcnow()
        #         visitor.ip_address = self.request.remote_addr
        #
        #     address = helper.get_address_from_ip(visitor.ip_address)
        #
        #     visitor.city = str(address["city"])
        #     visitor.country = str(address["country_name"])
        #     visitor.zip_code = str(address["zip_code"])
        #     visitor.latitude = str(address["latitude"])
        #     visitor.longitude = str(address["longitude"])
        #
        #
        #     visitor.put()

        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))



class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

My_messages=[]
My_History=[]


class BlogHandler(BaseHandler):
    def get(self):
        messages = model.Message.query(
            model.Message.deleted != True).fetch()  # model.Message.deleted != True needed with fake delete
        messages = sorted(messages, key=lambda x: x.created)[::-1]
        return self.render_template("blog.html", params={"messages": messages})

    def post(self):
        name = self.request.get("name")
        message_text = self.request.get("message_text")
        message = model.Message(message_text=message_text, name=name)
        message.put()
        return self.redirect_to("blog")


class EditMessageHandler(BaseHandler):
    def get(self, message_id):
        message = model.Message.get_by_id(int(message_id))
        return self.render_template("edit_message.html", params={"message": message})

    def post(self, message_id):
        message = model.Message.get_by_id(int(message_id))
        message.message_text = self.request.get("message_text")
        message.name = self.request.get("name")
        message.put()  # saves data in databank
        return self.redirect_to("blog")


class DeleteMessageHandler(BaseHandler):
    def get(self, message_id):
        message = model.Message.get_by_id(int(message_id))
        return self.render_template("delete_message.html", params={"message": message})

    def post(self, message_id):
        message = model.Message.get_by_id(int(message_id))
        message.key.delete()  # real delete (doesn't save in datastore)
        # message.deleted = True   # saves message in database  # have to add a query field in RealBlogHandler get
        # message.put() # needed with message.deleted = True
        return self.redirect_to("blog")


class LuckyNumberHandler(BaseHandler):
    def get(self):
        global My_History
        current_datetime = datetime.datetime.now()
        current_datetime += datetime.timedelta(hours=1) #can also write = "" (hours=+1)
        readable_date = current_datetime.strftime("%Y-%m-%d  %H:%M:%S")
        #readable_date = current_datetime.isoformat()
        my_number = random.randint(0,9)

        # add date and number to history
        My_History.append( (readable_date,my_number) )

        return self.render_template("luckyNumber.html", params={"site_my_number": my_number, "time":readable_date, "site_history":My_History})

class sngHandler(BaseHandler):
    def get(self):
        return self.render_template("sng.html")


    def post(self):
        has_guessed = True
        userguess = self.request.get("Numberguess")
        secret = 7
        userguess = int(userguess or 0)
        is_guessed = secret == userguess

        answer = self.request.get("answer")
        return self.render_template("sng.html", params={"is_guessed": is_guessed, "has_guessed": has_guessed, "answer": answer})


class LotteryHandler(BaseHandler):
    def get(self):
        global My_History
        current_datetime = datetime.datetime.now()
        readable_date = current_datetime.strftime("%Y-%m-%d  %H:%M:%S")
        lotto_numbers = random.sample(range(1,50),6)

        My_History.append(( lotto_numbers, readable_date))

        return self.render_template("Lottery.html", params={"give_me_lotto": lotto_numbers, "time":readable_date, "site_history":My_History})


class LoginHandler (BaseHandler):

    def get(self):
        user = users.get_current_user()

        if user:
            logged_in = True
            logout_url = users.create_logout_url('/logintest')
            params = {"logged_in": logged_in, "logout_url": logout_url, "user": user}
        else:
            logged_in = False
            login_url = users.create_login_url('/logintest')
            params = {"logged_in": logged_in, "login_url": login_url, "user": user}

        return self.render_template("logintest.html", params=params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler), # hello.html
    webapp2.Route('/blog', BlogHandler, name="blog"), # instructor realblog?
    webapp2.Route('/luckynumber', LuckyNumberHandler),
    webapp2.Route('/lottery', LotteryHandler),
    webapp2.Route('/sng', sngHandler),
    webapp2.Route('/logintest', LoginHandler, name="logintest"),
    webapp2.Route('/message/<message_id:\d+>/edit', EditMessageHandler),
    webapp2.Route('/message/<message_id:\d+>/delete', DeleteMessageHandler)
], debug=True)

# missing /shoppinglist , /options_game ( is in secret no game ), message edit , message delete. 
