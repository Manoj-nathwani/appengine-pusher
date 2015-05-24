import os
import jinja2
import webapp2
import pusher
from settings import *


# jinja2
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


# pusher
client = pusher.Pusher(
    app_id=pusher_app_id,
    key=pusher_key,
    secret=pusher_secret)


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())


class Push(webapp2.RequestHandler):
    def get(self):
        client.trigger(u'test_channel', 'my_event', {u'message': 'helooooooooo'})
        self.response.write("Message sent")


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/push', Push)
], debug=True)
