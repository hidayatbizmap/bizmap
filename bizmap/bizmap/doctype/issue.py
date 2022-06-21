import frappe

@frappe.whitelist()
def set_user_project_and_customer(doc,method):
	for usr in frappe.get_all("Project User",{"email":frappe.session.user},['parent']):
		project=frappe.get_doc("Project",usr.parent)
		doc.project=project.name
		doc.customer=project.customer
