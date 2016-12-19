cur_frm.cscript.onload_post_render = function(doc, cdt, cdn) {
	cur_frm.disable_save();
	cur_frm.toolbar.print_icon.addClass("hide");
}

cur_frm.cscript.run_report = function(doc){
	document.location = "/api/method/dgii.dgii.doctype.reporte_607.reporte_607.get_file_address?from_date=" 
		+ doc.from_date + "&to_date=" + doc.to_date;	
}
