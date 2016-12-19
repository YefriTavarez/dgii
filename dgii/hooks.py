# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "dgii"
app_title = "DGII"
app_publisher = "Soldeva, SRL"
app_description = "Una aplicacion para la generacion de los reportes que son enviados a la Direccion General de Impuestos Internos en la Republica Dominicana."
app_icon = "octicon octicon-flame"
app_color = "#7CBA00"
app_email = "servicios@soldeva.com"
app_version = "0.0.1"
app_license = "GNU General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/dgii/css/dgii.css"
# app_include_js = "/assets/dgii/js/dgii.js"

# include js, css files in header of web template
# web_include_css = "/assets/dgii/css/dgii.css"
# web_include_js = "/assets/dgii/js/dgii.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "dgii.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "dgii.install.before_install"
# after_install = "dgii.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "dgii.notifications.get_notification_config"

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
# 		"dgii.tasks.all"
# 	],
# 	"daily": [
# 		"dgii.tasks.daily"
# 	],
# 	"hourly": [
# 		"dgii.tasks.hourly"
# 	],
# 	"weekly": [
# 		"dgii.tasks.weekly"
# 	]
# 	"monthly": [
# 		"dgii.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "dgii.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "dgii.event.get_events"
# }
