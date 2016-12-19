# -*- coding: utf-8 -*-
# Copyright (c) 2015, Soldeva, SRL and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cstr, cint, flt, formatdate, format_datetime
from frappe.model.document import Document
from frappe.utils.csvutils import UnicodeWriter
import time

class Reporte606(Document):
	pass

@frappe.whitelist()
def get_file_address(from_date,to_date):
	result = frappe.db.sql("""SELECT p.rnc, s.tipo_rnc, p.tipo_bienes_y_servicios_comprados, 
		p.bill_no, p.bill_date, p.posting_date, p.base_taxes_and_charges_added, p.base_total 
		FROM `tabPurchase Invoice` p 
		JOIN tabSupplier s on s.rnc = p.rnc 
		WHERE p.bill_no LIKE '%s' AND p.docstatus = 1 AND p.posting_date 
		BETWEEN '%s' AND '%s' """ % ("%A%",from_date,to_date), as_dict=True)

	w = UnicodeWriter()
	w.writerow([
		'RNC',
		'Tipo de RNC',
		'Tipo de Bienes y Servicios Comprados',
		'NCF',
		'NCF modificado',
		'FC AAAAMM',
		'FC DD',
		'FP AAAAMM',
		'FP DD',
		'ITBIS Facturado',
		'ITBIS Retenido',
		'Monto Facturado',
		'Retencion Renta'
	])
		
	for row in result:
		bill_no = row.bill_no.split("-")[1] if(len(row.bill_no.split("-")) > 1) else row.bill_no # NCF-A1##% || A1##%
		w.writerow([
			row.rnc,
			row.tipo_rnc,
			row.tipo_bienes_y_servicios_comprados,
			bill_no,
			'',
			row.bill_date.strftime("%Y%m"),
			row.bill_date.strftime("%d"),
			row.posting_date.strftime("%Y%m"),
			row.posting_date.strftime("%d"),
			row.base_taxes_and_charges_added,
			'0', # ?
			row.base_total,
			'0' # ?
		])

	frappe.response['result'] = cstr(w.getvalue())
	frappe.response['type'] = 'csv'
	frappe.response['doctype'] = "Reporte_606_" + str(int(time.time()))
