# project_management/user_events.py
import frappe


@frappe.whitelist()
def after_insert_user(doc, method):
# doc is a User object
try:
if getattr(doc, 'company', None):
# ensure Worker role
if 'Worker' not in frappe.get_roles(doc.name):
doc.add_roles('Worker')
except Exception as e:
frappe.log_error(f'Error in after_insert_user: {e}')
