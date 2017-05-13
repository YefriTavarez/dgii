frappe.ui.form.on("Reporte 606", {
    onload: function(frm) {
       frm.doc.from_date = frappe.datetime.month_start();
       frm.doc.to_date = frappe.datetime.month_end();
	   cur_frm.disable_save();
    },

	run_report: function(frm){
		var url = "/api/method/dgii.dgii.doctype.reporte_606.reporte_606.get_file_address?from_date=" 
			+ frm.doc.from_date + "&to_date=" + frm.doc.to_date;

		window.open(url);
	}
});

