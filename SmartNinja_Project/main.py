#!/usr/bin/env python
import os
import jinja2
import webapp2
import random
import datetime


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
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

class BlogHandler(BaseHandler):
    def get(self):
        global My_History
        current_datetime = datetime.datetime.now()
        current_datetime += datetime.timedelta(hours=1) #can also write = "" (hours=+1)
        readable_date = current_datetime.strftime("%Y-%m-%d  %H:%M:%S")
        #readable_date = current_datetime.isoformat()
        my_number = random.randint(0,9)

        # add date and number to history
        My_History.append( (readable_date,my_number))

        return self.render_template("blog.html", params={"site_my_number": my_number, "time":readable_date, "site_history":My_History})

My_History=[]

class LotteryHandler(BaseHandler):
    def get(self):

        current_datetime = datetime.datetime.now()
        readable_date = current_datetime.strftime("%Y-%m-%d  %H:%M:%S")

        My_History.append(("The Lucky Numbers: ", lotto_numbers, "on " readable_date))

        lotto_numbers = random.sample(range(1,50),6)

        return self.render_template("Lottery.html", params={"give_me_lotto": lotto_numbers, "time":readable_date, "site_history":My_History})

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/blog', BlogHandler),
    webapp2.Route('/lottery', LotteryHandler),
], debug=True)

