// Copyright (c) 2016, Bala Murugan and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Paying Customers"] = {
	"filters": [
		{
			"fieldname": "first_name",
			"label":__("Member Name"),
			"fieldtype": "Data",
			"width": 100,
			"reqd": 0,
		},
		{
			"fieldname": "outstanding_debt",
			"label":__("Outstanding Debt"),
			"default":"",
			"width": 100,
			"reqd": 0,
		}

	]
};
