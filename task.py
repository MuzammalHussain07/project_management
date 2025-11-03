# project_management/task.py
import frappe


def validate(doc, method):
# Ensure project's company exists
proj_company = frappe.get_value('Project', doc.project, 'company')
if not proj_company:
frappe.throw('Linked project must have a company')


# Assigned worker must belong to the same company
if doc.assigned_worker:
worker_company = frappe.get_value('User', doc.assigned_worker, 'company')
if worker_company != proj_company:
frappe.throw('Assigned worker must belong to the same company as the project')
