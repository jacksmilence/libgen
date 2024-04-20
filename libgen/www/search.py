import math

import frappe
from libgen.constant import is_no_cache
from libgen.utils import redirect_to_login, redirect_to_404, redirect_to_index


def get_context(context):
    # 需要用户登录
    context.no_cache = is_no_cache
    user = frappe.session.user
    if user == "Guest":
        redirect_to_login()

    # 获取搜索结果
    try:
        req = frappe.form_dict['req']
    except KeyError:
        redirect_to_index()
    res = frappe.form_dict['res']
    column = frappe.form_dict['column']
    try:
        pagination = int(frappe.form_dict['page'])
    except KeyError:
        pagination = 1
    context.req = req
    context.res = int(res)
    context.column = column
    context.pagination = int(pagination)

    # 模糊查询
    values = {'req': '%' + req + '%', 'res': int(res), 'start': (int(pagination) - 1) * int(res)}
    if column == 'title':
        count = frappe.db.sql("select count(Title) as count from updated where Title like %(req)s order by Year desc", values=values, as_dict=True)
        results = frappe.db.sql("""select * from updated where Title like %(req)s order by Year desc limit %(start)s,  %(res)s""",
                                values=values, as_dict=True)
        total_page_number = math.ceil(int(count[0]['count']) / int(res))
    elif column == 'author':
        count = frappe.db.sql("select count(Author) as count from updated where Author like %(req)s order by Year desc",
                              values=values, as_dict=True)
        results = frappe.db.sql(
            """select * from updated where Author like %(req)s order by Year desc limit %(start)s,  %(res)s""",
            values=values, as_dict=True)
        total_page_number = math.ceil(int(count[0]['count']) / int(res))
    elif column == 'series':
        count = frappe.db.sql("select count(Series) as count from updated where Series like %(req)s order by Year desc",
                              values=values, as_dict=True)
        results = frappe.db.sql(
            """select * from updated where Series like %(req)s order by Year desc limit %(start)s,  %(res)s""",
            values=values, as_dict=True)
        total_page_number = math.ceil(int(count[0]['count']) / int(res))
    elif column == 'publisher':
        count = frappe.db.sql("select count(Publisher) as count from updated where Publisher like %(req)s order by Year desc",
                              values=values, as_dict=True)
        results = frappe.db.sql(
            """select * from updated where Publisher like %(req)s order by Year desc limit %(start)s,  %(res)s""",
            values=values, as_dict=True)
        total_page_number = math.ceil(int(count[0]['count']) / int(res))
    elif column == 'identifier':
        count = frappe.db.sql("select count(Identifier) as count from updated where Identifier like %(req)s order by Year desc",
                              values=values, as_dict=True)
        results = frappe.db.sql(
            """select * from updated where Identifier like %(req)s order by Year desc limit %(start)s,  %(res)s""",
            values=values, as_dict=True)
        total_page_number = math.ceil(int(count[0]['count']) / int(res))

    elif column == 'language':
        count = frappe.db.sql("select count(Language) as count from updated where Language like %(req)s order by Year desc",
                              values=values, as_dict=True)
        results = frappe.db.sql(
            """select * from updated where Language like %(req)s order by Year desc limit %(start)s,  %(res)s""",
            values=values, as_dict=True)
        total_page_number = math.ceil(int(count[0]['count']) / int(res))
    elif column == 'md5':
        count = frappe.db.sql("select count(MD5) as count from updated where MD5 like %(req)s order by Year desc",
                              values=values, as_dict=True)
        results = frappe.db.sql(
            """select * from updated where MD5 like %(req)s order by Year desc limit %(start)s,  %(res)s""",
            values=values, as_dict=True)
        total_page_number = math.ceil(int(count[0]['count']) / int(res))
    elif column == 'tags':
        count = frappe.db.sql("select count(Tags) as count from updated where Tags like %(req)s order by Year desc",
                              values=values, as_dict=True)
        results = frappe.db.sql(
            """select * from updated where Tags like %(req)s order by Year desc limit %(start)s,  %(res)s""",
            values=values, as_dict=True)
        total_page_number = math.ceil(int(count[0]['count']) / int(res))
    elif column == "year":
        count = frappe.db.sql("select count(Year) as count from updated where Year like %(req)s order by Year desc",
                              values=values, as_dict=True)
        results = frappe.db.sql(
            """select * from updated where Year like %(req)s order by Year desc limit %(start)s,  %(res)s""",
            values=values, as_dict=True)
        total_page_number = math.ceil(int(count[0]['count']) / int(res))
    else:
        redirect_to_index()
    if pagination < 1:
        redirect_to_404()
    elif pagination > total_page_number > 0:
        redirect_to_404()
    context.total_page_number = total_page_number
    context.count = count[0]
    context.results = results
    return context
