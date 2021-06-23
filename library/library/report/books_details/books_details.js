// Copyright (c) 2016, Bala Murugan and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Books Details"] = {
	"filters": [
		{
			"fieldname": "book_name",
			"label":__("Book Name"),
			"fieldtype": "Data",
			"width": 100,
			"reqd": 0,
		},
		{
			"fieldname": "status",
			"label":__("Book Status"),
			"fieldtype": "Select",
			"options":['Issued','Available'],
			"default":"",
			"width": 100,
			"reqd": 0,
		}

	]
};
