import os


settings = {
"static_path": os.path.join(os.path.dirname(__file__), "static"),
"cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
"template_path":os.path.join(os.path.dirname(__file__), "templates"),
"login_url": "/login",
"xsrf_cookies": True,
}
