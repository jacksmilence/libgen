import frappe


def redirect_to_login():
    frappe.local.flags.redirect_location = "/login"
    raise frappe.Redirect


def redirect_to_404():
    frappe.local.flags.redirect_location = "/404"
    raise frappe.Redirect

def redirect_to_index():
    frappe.local.flags.redirect_location = "/"
    raise frappe.Redirect

def format_number(number):
    return round(number / 1000 / 1000, 2)
