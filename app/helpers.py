#
# AUTHOR : LAWRENCE GANDHAR
# Project For Mohini - (India)
# Project Date : 14th Sept 2021
#

import datetime
import os
import random
import string
import re
import json
import secrets

from django.conf import settings
from app.models import *

from django.utils import timezone
from django.core.mail import EmailMessage
from django.core.serializers.json import DjangoJSONEncoder


# *************************************************************************************
# YEAR RANGE
# *************************************************************************************
def year_ranger():
    return [x for x in range(2011, (datetime.datetime.now().year + 5))]


# *************************************************************************************
# AUTO CODE GENERATOR
# *************************************************************************************

def generate_code(prefix="A", id=1):
    id = str(id)
    series = "0" * 10
    main_series = prefix + series[:(len(series) - len(id))] + id

    return main_series


# *************************************************************************************
# HANDLE UPLOADED FILE
# *************************************************************************************

def handle_uploaded_file(f, path="", insert_path=None):
    _, ext = os.path.splitext(f.name)

    file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=14)) + ext

    filepath = os.path.join(path, file_name)

    with open(filepath, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    if os.path.exists(filepath):
        if insert_path is not None:
            return [True, os.path.join(insert_path, file_name)]
        return [True, filepath]
    return [False, None]


# *************************************************************************************
# Create Directory
# *************************************************************************************

def create_directory(path):
    if not os.path.exists(path):
        try:
            os.makedirs(path)
            return True
        except:
            return False
    return True


# *************************************************************************************
# Remove Html Tags
# *************************************************************************************

def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)



# ******************************************************************************
# User Creation Form Errors Mapping
# ******************************************************************************
def user_creation_form_errors(err_msg):
    errors = json.loads(err_msg.as_json())
    err_keys = errors.keys()

    errors["password"] = []

    if "password2" in err_keys:
        for msg in errors["password2"]:
            errors["password"].append({"message":msg["message"], "code":msg["code"]})

        del(errors["password2"])

    if "password1" in err_keys:
        for msg in errors["password1"]:
            if msg["code"] == "required":
                errors["password"].append({"message":"Both password fields are required.", "code":msg["code"]})
            else:
                errors["password"].append({"message":msg["message"], "code":msg["code"]})

        del(errors["password1"])

    return errors


# ******************************************************************************
# Errors : Formatting
# ******************************************************************************
def format_errors(err_msg):

    if not isinstance(err_msg, dict) and isinstance(err_msg, str):
        err_msg = err_msg.as_json()

    html = ["<table style='color:#FFFFFF; border:1px solid #eee; width:100%'>"]
    html.append("<tr><td class='text-center' style='padding:10px; font-weight:700;'>Label</td>")
    html.append("<td class='text-center' style='padding:10px; font-weight:700;'>Errors</td></tr>")
    for i in err_msg:
        html.append("<tr><td style='vertical-align:top; padding:10px; border:1px solid #eee;'>{}</td>".format(i.title()))
        html.append("<td style='vertical-align:top; padding:10px; border:1px solid #eee;'><ul style='margin:0px;'>")
        for v in err_msg[i]:
            html.append("<li>{}</li>".format(v["message"]))
    html.append("</ul></td></tr></table>")

    html = ''.join(html)
    return html


# ******************************************************************************
# Queryset to {Row id:{row}} JSON format
# @queryset = Queryset Object
# ******************************************************************************
def queryset_row_to_json(queryset):
    items_list_json = {}
    for row in queryset:
        
        try:
            xx = row.__dict__  # get all attributes of the object
            items_list_json[row.id] = {x:y for (x,y) in xx.items() if x not in ["_state", "id"]}  # discard _state, id (key:value) pair
        except AttributeError:
            pass

        if "account_no_id" in items_list_json[row.id].keys():
            if items_list_json[row.id]["account_no_id"] is not None:
                items_list_json[row.id]["account_no_id_related"] = row.account_no.account_no
            else:
                items_list_json[row.id]["account_no_id_related"] = None

    return json.dumps(items_list_json, cls=DjangoJSONEncoder)


# ******************************************************************************
#
# ******************************************************************************
def clean_data(val=None):
    if val is None:
        return None
    else:
        if val.strip()!="":
            return val.strip()
        else:
            return None


#
#
#

def sendmymail(subject=None, email_html_template=None,send_to=[]):
    email_msg = EmailMessage(subject,
                             email_html_template,
                             settings.APPLICATION_EMAIL,
                             send_to,
                             reply_to=[settings.APPLICATION_EMAIL]
                             )
    # this is the crucial part that sends email as html content but not as a plain text
    email_msg.content_subtype = 'html'
    email_msg.send(fail_silently=False)

# ******************************************************************************
# Send Forgot Password Email
# ******************************************************************************

def send_email_forgot_password(user=None):
    email_html_template = '''
        <html>
        <body>
        <p>
        Dear {} {},
        </br>
        </p>
        <p>
        </br>
            Please click on the link given below to reset your password.
        </p>
        <p>
        <br/><br/>
        Best Regards,<br/>
        Administrator<br/>
        FinECL<br/>
        </body></html>
    '''.format(user.first_name.title(), user.last_name.title())

    subject = 'FinECL - Forgot Password'.format(user)

    sendmymail(subject, email_html_template,send_to=[user.email])

# ******************************************************************************
# Send Accept Email
# ******************************************************************************

def send_email_accept_user(user=None, passwd=None):
    email_html_template = '''
        <html>
        <body>
        <p>
        Dear {} {},
        </br>
        </p>
        <p>
        </br>
            Congratulations! Your application for the registeration in FinECL has been approved. The credentials are given below.
            <br/><br/>
            Please reset your password once you login with the one time password which is valid for a week.
            <br/><br/>
            Username: <b>{}</b>
            <br/>
            Password: <b>{}</b>
        </p>
        <p>
        <br/><br/>
        Best Regards,<br/>
        Administrator<br/>
        FinECL<br/>
        </body></html>
    '''.format(user.first_name.title(), user.last_name.title(), user.email, passwd)

    subject = 'FinECL - registeration Successful'.format(user)

    sendmymail(subject, email_html_template,send_to=[user.email])


# ******************************************************************************
# Send Reject Email
# ******************************************************************************

def send_email_reject_user(user=None):
    email_html_template = '''
        <html>
        <body>
        <p>
        Dear {} {},
        </br>
        </p>
        <p>
        </br>
            Your application for the registeration in FinECL has been rejected due to administrative reasons.
            <br/>
            Please try again or contact the Administrator.
        </p>
        <p>
        <br/><br/>
        Best Regards,<br/>
        Administrator<br/>
        FinECL<br/>
        </body></html>
    '''.format(user.first_name.title(), user.last_name.title())

    subject = 'FinECL - Forgot Password'.format(user)

    sendmymail(subject, email_html_template,send_to=[user.email])


# ******************************************************************************
# Audit trail function
# ******************************************************************************

def audit_trail(request, data={}):

    """
    Example : {
        "parent" : tab_status,
        "edited_data" : True,
        "params":{"handler_table": "initial", "selected_ids":[obj.id]}
    }
    """


    ins = Audit_Trail.objects.create(user = request.user, date = timezone.now())

    dict_keys = data.keys()

    if "parent" in dict_keys:
        ins.parent = data["parent"]

    #
    # Edit Mode
    if "edited_data" in dict_keys:
        ins.edited_data = data["edited_data"]

        if "params" in dict_keys:
            ins.edited_data_params = json.dumps(data["params"])

    #
    # Moded Data Mode
    if "moved_data" in dict_keys:
        ins.moved_data = data["moved_data"]

        if "params" in dict_keys:
            ins.moved_data_params = json.dumps(data["params"])

    #
    # Deleted Data Mode
    if "deleted_data" in dict_keys:
        ins.deleted_data = data["deleted_data"]

        if "params" in dict_keys:
            ins.deleted_data_params = json.dumps(data["params"])

    #
    # Report Download Mode
    if "report_download" in dict_keys:
        ins.report_download = data["report_download"]

        if "params" in dict_keys:
            ins.report_download_params = json.dumps(data["params"])

    #
    # Report Run Mode
    if "report_run" in dict_keys:
        ins.report_run = data["report_run"]

        if "params" in dict_keys:
            ins.report_run_params = json.dumps(data["params"])

    ins.save()


# ******************************************************************************
# BACKGROUND COLOR CODINGS
# ******************************************************************************

def bg_color_codes():
    return "#"+secrets.token_hex(3)+"32"
