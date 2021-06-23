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
    conditions = " AND 1=1 "
    if(filters.get('name')):conditions += f" AND name LIKE '%{filters.get('name')}'"
    if(filters.get('book_name')):conditions += f" AND book_name = '{filters.get('book_name')}'"
    if(filters.get('status')):conditions += f" AND status ='{filters.get('status')}'"
    
    
    data = frappe.db.sql("""SELECT name,book_name,author,publisher,book_rent,status, COUNT(book_rent) OVER (PARTITION BY book_name) AS total_book  FROM `tabBooks`  ;""")
    return data
   
def get_columns():
    return[
		"ISBN:Link/Books:150",
		"Book Name:Data:250",
		"Book Author:Data:150",
		"Book Publisher:Data:150",
		"Book Rent:Data:150",
		"Book Status:Selection:150",
		"Total Book:150"
	]
