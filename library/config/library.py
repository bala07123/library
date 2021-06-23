from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Library"),
            "icon": "octicon octicon-briefcase",
            "items": [
                {
                    "type": "doctype",
                    "name": "Books",
                    "label": "Book",
                    "description": _("Books which members issue and return."),
                },
                {
                    "type": "doctype",
                    "name": "Members",
                    "label": "Members",
                    "description": _("People who have enrolled membership in the library."),
                },
                {
                    "type": "doctype",
                    "name": "Membership",
                    "label": "Membership",
                    "description": _("Books which members issue and return."),
                },
                {
                    "type": "doctype",
                    "name": "Transactions",
                    "label": "Transaction",
                    "description": _("People who have enrolled membership in the library."),
                }
            ]

        },
        {
            "label": _("Reports"),
            "icon": "fa fa-list",
            "items": [
                {
                    "type": "report",
                    "is_query_report": True,
                    "name": "Books Details",
                    "doctype": "Books"
                },
                {
                    "type": "report",
                    "is_query_report": True,
                    "name": "Highest Paying Customers",
                    "doctype": "Members"
                },
            ]
        },
    ]
