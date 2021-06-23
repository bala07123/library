# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "library"
app_title = "Library"
app_publisher = "Bala Murugan"
app_description = "Library Management"
app_icon = "icon-linux"
app_color = "#6DAFC9"
app_email = "murugan.mu@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
fixtures = ["Books","Members"]
# include js, css files in header of desk.html
# app_include_css = "/assets/library/css/library.css"
# app_include_js = "/assets/library/js/library.js"

# include js, css files in header of web template
# web_include_css = "/assets/library/css/library.css"
# web_include_js = "/assets/library/js/library.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "library.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "library.install.before_install"
# after_install = "library.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "library.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"library.tasks.all"
# 	],
# 	"daily": [
# 		"library.tasks.daily"
# 	],
# 	"hourly": [
# 		"library.tasks.hourly"
# 	],
# 	"weekly": [
# 		"library.tasks.weekly"
# 	]
# 	"monthly": [
# 		"library.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "library.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "library.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "library.task.get_dashboard_data"
# }

