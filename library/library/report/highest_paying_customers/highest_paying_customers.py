# Copyright (c) 2013, Bala Murugan and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe import _
import frappe

def execute(filters=None):
	#columns, data = [], []
	return get_columns(), get_data(filters)

def get_data(filters):
    print(f"\n\n\n\{filters}\n\n\n\n")
    data = frappe.db.sql("""SELECT name,first_name,outstanding_debt,phone_number,email_address,total_payment FROM `tabMembers` ORDER BY total_payment DESC;""")
    return data
   
def get_columns():
    return[
		"Member ID:Link/Books:150",
		"Member Name:Data:200",
		"Outstanding Debit:Data:150",
		"Phone Number:Data:200",
		"Email Address:Data:200",
		"Highest Paying Customer:Data:200"
	]
