# -*- coding: utf-8 -*-
# Copyright (c) 2015, Soldeva, SRL and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cstr, cint, flt, formatdate, format_datetime
from frappe.model.document import Document
from frappe.utils.csvutils import UnicodeWriter
import time

class Reporte607(Document):
	def set_right_ids(self):
		invoice_list = frappe.db.sql("SELECT name, parent from `tabSales Invoice` ORDER BY posting_date",as_dict=True)
		
		index = 4276
		for invoice in invoice_list:			
			frappe.db.sql("UPDATE `tabSales Invoice` set serie ='SI-{0}' WHERE name= '{1}'".format(index,invoice.name))
			index = index + 1


@frappe.whitelist()
def get_file_address(from_date,to_date):
	result = frappe.db.sql("""SELECT c.rnc, s.name, s.posting_date, s.total_taxes_and_charges, s.base_total 
		FROM `tabSales Invoice` s 
		JOIN tabCustomer c on s.customer = c.name 
		WHERE s.name NOT LIKE '%s' AND c.rnc > 0 AND s.docstatus = 1 AND s.posting_date 
		BETWEEN '%s' AND '%s' """ % ("SINV-%",from_date,to_date), as_dict=True)

	w = UnicodeWriter()
	w.writerow(['RNC','Tipo de RNC','NCF','NCF modificado','Fecha de impresion','ITBIS facturado','Monto Total'])
		
	for row in result:
		name = row.name.split("-")[1] if(len(row.name.split("-")) > 1) else row.name # NCF-A1##% || A1##%
		w.writerow([row.rnc,"1",name,"",row.posting_date.strftime("%Y%m%d"),row.total_taxes_and_charges,row.base_total])

	frappe.response['result'] = cstr(w.getvalue())
	frappe.response['type'] = 'csv'
	frappe.response['doctype'] = "Reporte_607_" + str(int(time.time()))






 	




