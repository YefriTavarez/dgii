# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "dgii"
app_title = "DGII"
app_publisher = "Soldeva, SRL"
app_description = "Una aplicacion para la generacion de los reportes que son enviados a la Direccion General de Impuestos Internos en la Republica Dominicana"
app_icon = "octicon octicon-flame"
app_color = "#469"
app_email = "servicios@soldeva.com"
app_license = "MIT"


# Fixtures
# --------

fixtures = [
	{
		"doctype": "Custom Field",
		"filters": {
			"name": (
				"in", (
					"Purchase Invoice-total_itbis",
					"Purchase Invoice Item-item_type",
					"Purchase Invoice-legal_tip",
					"Purchase Invoice-other_taxes",
					"Purchase Invoice-excise_tax",
					"Purchase Invoice-include_isr",
					"Purchase Invoice-isr_amount",
					"Purchase Invoice-isr_rate",
					"Purchase Invoice-include_retention",
					"Purchase Invoice-retention_amount",
					"Purchase Invoice-retention_rate",
					"Purchase Invoice-monto_facturado_servicios",
					"Purchase Invoice-monto_facturado_bienes",
					"Sales Taxes and Charges-tax_type",
					"Item-item_type",
					"Purchase Invoice-tipo_bienes_y_servicios_comprados",
					"Supplier-tipo_rnc",
					"Customer-tipo_rnc",
					"Purchase Invoice-tax_id",
				)
			)
		}
	}	
]

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

# Doctype JS
# ----------
doctype_js = {
	"Purchase Invoice": "public/js/purchase_invoice.js",
	"Customer": "public/js/customer.js",
}

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

doc_events = {
	"Purchase Invoice": {
		"validate": "dgii.hook.purchase_invoice.validate",
	}
}

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

