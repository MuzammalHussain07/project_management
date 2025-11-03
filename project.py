# project_management/project.py
import frappe


def validate(doc, method):
# Ensure project manager belongs to same company
if doc.project_manager:
pm_company = frappe.get_value('User', doc.project_manager, 'company')
if pm_company and pm_company != doc.company:
frappe.throw('Project Manager must belong to the same company as the project')


# Ensure each project member belongs to same company
for row in getattr(doc, 'project_members', []) or []:
member_company = frappe.get_value('User', row.user, 'company')
if member_company and member_company != doc.company:
frappe.throw(f'Project member {row.user} belongs to a different company')
