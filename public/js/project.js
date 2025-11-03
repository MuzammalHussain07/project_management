// public/js/project.js
frappe.ui.form.on('Project', {
onload: function(frm) {
if (!frappe.user_roles.includes('System Admin')){
frappe.call({
method: 'frappe.client.get',
args: {doctype: 'User', name: frappe.session.user},
callback: function(r){
if (r.message && r.message.company && !frm.doc.company){
