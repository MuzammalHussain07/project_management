# project_management/permissions.py
return None


user_company = frappe.get_value('User', user, 'company')
if not user_company:
return "1=0" # no rows


return "`tabProject`.company = '{0}'".format(frappe.db.escape(user_company))


# For Task doctype: join via project table to ensure company isolation
def get_permission_query_conditions_task(user=None):
if not user:
user = frappe.session.user
if SYSTEM_ADMIN_ROLE in frappe.get_roles(user):
return None


user_company = frappe.get_value('User', user, 'company')
if not user_company:
return "1=0"


# ensure tasks are returned only if their linked project's company matches user's company
return "EXISTS (SELECT 1 FROM `tabProject` p WHERE p.name = `tabTask`.project AND p.company = '{0}')".format(frappe.db.escape(user_company))




def has_permission(doc, ptype, user=None):
if not user:
user = frappe.session.user


if SYSTEM_ADMIN_ROLE in frappe.get_roles(user):
return True


user_company = frappe.get_value('User', user, 'company')
# If doc has company directly
if hasattr(doc, 'company') and doc.company:
return str(doc.company) == str(user_company)


# If Task: check via linked Project
if doc.doctype == 'Task' and doc.project:
proj_company = frappe.get_value('Project', doc.project, 'company')
return str(proj_company) == str(user_company)


# Default: allow read for other system docs
return True
