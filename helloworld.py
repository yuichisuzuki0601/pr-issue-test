# coding: utf-8
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


class MainPage(webapp.RequestHandler):


    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(u'Hello, webapp World! My name is 鈴木 裕一!!')


application = webapp.WSGIApplication([('/', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
