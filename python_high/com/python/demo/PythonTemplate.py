# -*- coding：utf-8 -*-
from string import Template
# 支持简单的字符串模板替换

def start_response(resp="text/html"):
    """
    请求文件的类型, 选填参数（默认"text/html"）
    用它来创建一个CGI（Common Gateway Interface）
    :param resp:    传入参数
    :return:
    """
    return 'Content-type: ' + resp + '\n\n'

def include_header(the_title):
    """
    将模板页面的标题部分进行替换
    :param the_title:   替换标题的文字
    :return:
    """
    with open('templates/header.html') as headf:
        head_text = headf.read()
    headers = Template(head_text)
    # substitute()函数需要一个参数, 指定要替换的参数即可完成替换
    return headers.substitute(title=the_title)

def include_footer(the_links):
    """
    替换页面的底部数据
    :param the_links:   页面底部的数据
    :return:
    """
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href"' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    # 将页面底部的数据替换成为字典数据
    return footer.substitute(links=link_string)

def start_form(the_url, form_type="POST"):
    """
    请求页面
    :param the_url:     请求页面的URL
    :param form_type:   请求页面的方式
    :return:
    """
    return '<form action="' + the_url + '"method="' + form_type + '">'

def end_form(submit_msg="Submit"):
    """
    # 增加页面交互, 拼接提交的数据
    :param submit_msg:  页面提交的数据
    :return:
    """
    return '<p><p><input type=submit value="' + submit_msg + '">'

def u_list(items):
    """
    为页面新增一个无序列表
    :param items:   列表项
    :return:
    """
    u_string = '<url>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</url>'
    return u_string

def header(header_text, header_level=2):
    """
    标题参数字体控制
    :param header_text:     标题文字
    :param header_level:    标题字体
    :return:
    """
    return '<h' + str(header_level) + '>' + header_text + '</h' +str(header_level) + '>'

def para(para_text):
    """
    用HTML标记一段文字
    :param para_text:   标记文字的内容
    :return:
    """
    return '<p>' + para_text + '</p>'