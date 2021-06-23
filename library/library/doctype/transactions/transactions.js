// Copyright (c) 2021, Bala Murugan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Transactions', 'member', function (frm) {
	frappe.call({
		"method": "frappe.client.get",
		args: {
			doctype: "Members",
			name: frm.doc.member
		},
		callback: function (data) {
			
			frappe.model.set_value(frm.doctype, frm.docname, "member_name", 
			data.message.first_name 
			+ (data.message.last_name ? (" " + data.message.last_name) : ""))
		}
	})
	

	// refresh: function(frm) {

	// }
});
//Adding filter in Books doctype books field based on Books doctype status field value
frappe.ui.form.on("Transactions", "onload", function(frm){
	
	//frm.set_df_property("bar_code", "reqd", true);
    frm.set_query("books", function(){
		return {
            "filters": [
                ["Books", "status", "=", "Available"]    
            ]
		
		}
    });
});


