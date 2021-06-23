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
            # Find the total rent of the Members in Transactions Doctype
            b = f"select sum(rent) from `tabTransactions` where member_name = '{self.member_name}' and docstatus<=1"
            d = frappe.db.sql(b)
            total_pay = d[0]
            # Set total payment of members in Members Doctype
            total_payment = f"update `tabMembers` set total_payment = '{total_pay[0]}' where name='{self.member}'"
            frappe.db.sql(total_payment)
            if(flt(amount) < 500):
                # Find the total rent based on Member in Transactions Doctype
                s = f"select sum(rent) from `tabTransactions` where member_name = '{self.member_name}' and docstatus=0"
                qty = frappe.db.sql(s)
                a = qty[0]
                # Set the outstanding debit amount in Members Doctype
                z = f"update `tabMembers` set outstanding_debt = '{a[0]}' where name='{self.member}'"
                frappe.db.sql(z)
                # Once the book is issued to member ,then Books doctype status updated to Issued
                y = f"update `tabBooks` set status = 'Issued' where book_name='{self.books_name}'"
                frappe.db.sql(y)
            else:
                frappe.throw(
                    _("Cannot Issue a books when outstanding debit is above 500 "))

    def on_submit(self):
        if self.transaction_type == "Return":
            if self.paid == True:
                # Find the outstanding debit based on Members book returned
                debt = frappe.db.get_values("Members", filters={"name": self.member}, fieldname=[
                    "name", "first_name", "outstanding_debt"], as_dict=True)
                outstanding_rent = flt(
                    debt[0].outstanding_debt) - int(self.rent)
                #set the outstanding debit value in Members Doctype
                rent_outstanding = f"update `tabMembers` set outstanding_debt = '{outstanding_rent}' where name='{self.member}'"
                frappe.db.sql(rent_outstanding)
                #Update the status value is Available in Books Doctype ,once the book is return
                z = f"update `tabBooks` set status = 'Available' where book_name='{self.books_name}'"
                frappe.db.sql(z)
        else:
            frappe.throw(
                _("Already the book is Issued please confirm the book rent is paid and return the book  "))
