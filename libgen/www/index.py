import frappe
from libgen.constant import is_no_cache
from libgen.utils import redirect_to_login


def get_context(context):
    # 需要用户登录
    context.no_cache = is_no_cache
    user = frappe.session.user
    if user == "Guest":
        redirect_to_login()
    return context
