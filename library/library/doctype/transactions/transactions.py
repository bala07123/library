# -*- coding: utf-8 -*-
# Copyright (c) 2021, Bala Murugan and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils.data import flt


class Transactions(Document):
    def on_update(self):

        users = frappe.db.get_values("Members", filters={"name": self.member}, fieldname=[
                                     "name", "first_name", "outstanding_debt"], as_dict=True)
        amount = flt(users[0].outstanding_debt)
        print(amount)
        if(self.transaction_type == "Issue"):
            b = f"select sum(rent) from `tabTransactions` where member_name = '{self.member_name}' and docstatus<=1"
            d = frappe.db.sql(b)
            total_pay = d[0]
            total_payment = f"update `tabMembers` set total_payment = '{total_pay[0]}' where name='{self.member}'"
            frappe.db.sql(total_payment)
            if(flt(amount) < 500):
                s = f"select sum(rent) from `tabTransactions` where member_name = '{self.member_name}' and docstatus=0"
                qty = frappe.db.sql(s)
                a = qty[0]

                z = f"update `tabMembers` set outstanding_debt = '{a[0]}' where name='{self.member}'"
                frappe.db.sql(z)
                y = f"update `tabBooks` set status = 'Issued' where book_name='{self.books_name}'"
                frappe.db.sql(y)
            else:
                frappe.throw(
                    _("Cannot Issue a books when outstanding debit is above 500 "))

    def on_submit(self):
        if self.transaction_type == "Return":
            if self.paid == True:
                users = frappe.db.get_values("Members", filters={"name": self.member}, fieldname=[
                                             "name", "first_name", "outstanding_debt"], as_dict=True)
                print(users[0].outstanding_debt)
                outstanding_rent = flt(
                    users[0].outstanding_debt) - int(self.rent)
                rent_outstanding = f"update `tabMembers` set outstanding_debt = '{outstanding_rent}' where name='{self.member}'"
                frappe.db.sql(rent_outstanding)
                z = f"update `tabBooks` set status = 'Available' where book_name='{self.books_name}'"
                frappe.db.sql(z)
        else:
            frappe.throw(
                    _("Already the book is Issued please confirm the book rent is paid and return the book  "))
