# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Library",
			"category": "Modules",
			"color": "#6DAFC9",
			"icon": "icon-linux",
			"type": "module",
			"label": _("Library"),	
			"onboard_present": 1
		}
	]
