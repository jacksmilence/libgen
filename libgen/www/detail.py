import frappe
from libgen.constant import is_no_cache
from libgen.utils import redirect_to_index, redirect_to_login


def get_context(context):
    context.no_cache = is_no_cache
    user = frappe.session.user
    if user == "Guest":
        redirect_to_login()
    md5 = frappe.form_dict.get("url_optimization")
    result = frappe.db.sql(f"""
SELECT u.Title, u.Author, u.Series, u.Periodical, u.VolumeInfo, u.Publisher, u.Year, u.MD5, u.Identifier,
CASE 
WHEN `Visible`='ban'
THEN 'ban'
WHEN `Visible`='del'
THEN 'del'
ELSE 
CONCAT(u.`ID` - (u.`ID` % 1000), '/', u.`MD5`) 
END as `Filename`, u.Extension
FROM updated u WHERE u.MD5='{md5}'
    """, as_dict=True)
    try:
        context.result = result[0]
    except IndexError:
        redirect_to_index()
    return context