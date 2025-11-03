# project_management/hooks.py
app_name = "project_management"
app_title = "Project Management"
app_publisher = "Muzammal Hussain"
app_description = "Multi-tenant Project Management app for Frappe"
app_icon = "octicon octicon-briefcase"
app_version = "0.0.1"


# JS files to include
doctype_js = {
"Project": "public/js/project.js",
"Task": "public/js/task.js"
}


# permission hooks (use our custom module)
permission_query_conditions = {
"Project": "project_management.permissions.get_permission_query_conditions_project",
"Task": "project_management.permissions.get_permission_query_conditions_task"
}


has_permission = {
"Project": "project_management.permissions.has_permission",
"Task": "project_management.permissions.has_permission"
}


# Document events
doc_events = {
"Project": {
"validate": "project_management.project.validate"
},
"Task": {
"validate": "project_management.task.validate"
},
"User": {
"after_insert": "project_management.user_events.after_insert_user"
}
}


# Fixtures to export roles if you want to include them in install
fixtures = [
{"dt": "Role", "filters": [["Role", "name", "in", ["System Admin", "Company Admin", "Project Manager", "Worker"]]]}
]
