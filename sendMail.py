import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'chudang98hn@gmail.com'
EMAIL_PASSWORD = 'kmujvzkdoblvfxjv'
EMAIL_RECEIVER = 'duckdonald10031998@gmail.com'

def trigger_email(array_cv):
    res = ""
    total_record = len(array_cv)
    # for cv in array_cv:
    for index,cv in enumerate(array_cv):
        name = cv["name"]
        position = cv["position"]
        DOB = cv["dateOfBirth"]
        cares = cv["whoCares"]
        linkCV = cv["linkCV"]
        res += '<tr style="border: 1px solid black;text-align: center;">'
        res += f'<td style="border: 1px solid black;text-align: center;">{index + 1}/{total_record}</td>'
        res += f'<td style="border: 1px solid black;text-align: center;">{name}</td>'
        res += f'<td style="border: 1px solid black;text-align: center;">{position}</td>'
        res += f'<td style="border: 1px solid black;text-align: center;">{DOB}</td>'
        res += f'<td style="border: 1px solid black;text-align: center;">{cares}</td>'
        res += f'<td style="border: 1px solid black;text-align: center;">{linkCV}</td>'
        res += '</tr>'

    return """
        <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
            </head>
            <body>
                <h1 style="text-align: center">Danh sach ung vien</h1>
                <table
                    style="border: 1px solid black;text-align: center;"
                >
                    <tr style="border: 1px solid black;text-align: center;">
                    <th style="border: 1px solid black;min-width: 50px;text-align: center;">STT</th>
                    <th style="border: 1px solid black;min-width: 200px;text-align: center;">Ten ung vien</th>
                    <th style="border: 1px solid black;min-width: 250px;text-align: center;">Vi tri ung tuyen</th>
                    <th style="border: 1px solid black;min-width: 100px;text-align: center;">DOB</th>
                    <th style="border: 1px solid black;min-width: 200px;text-align: center;">Care</th>
                    <th style="border: 1px solid black;min-width: 300px;text-align: center;">CV</th>
                    </tr>
                    {data}
                </table>
            </body>
        </html>""".format(data=res)
    # return template
# data_table = conver_data_to_html_tags(testData)

def sendMail(data):
    html_attach = trigger_email(data)
    msg = EmailMessage()
    msg['Subject'] = '[AutoCV] Danh sach ung vien'
    msg['From' ] = EMAIL_ADDRESS
    msg['To'] = EMAIL_RECEIVER
    msg.set_content('plain text')
    msg.add_alternative(html_attach, subtype="html")

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


    # for index,cv in array_cv:
    #     name = cv["name"]
    #     position = cv["position"]
    #     DOB = cv["dateOfBirth"]
    #     cares = cv["whoCares"]
    #     linkCV = cv["linkCV"]
    #     res += '<tr style="border: 1px solid black;width: 100%;text-align: center;">'
    #     res += f'<td style="border: 1px solid black;width: 100%;text-align: center;">{index+1}/${total_record}</td>'
    #     res += f'<td style="border: 1px solid black;width: 100%;text-align: center;">{name}</td>'
    #     res += f'<td style="border: 1px solid black;width: 100%;text-align: center;">{position}</td>'
    #     res += f'<td style="border: 1px solid black;width: 100%;text-align: center;">{DOB}</td>'
    #     res += f'<td style="border: 1px solid black;width: 100%;text-align: center;">{cares}</td>'
    #     res += f'<td style="border: 1px solid black;width: 100%;text-align: center;">{linkCV}</td>'
    #     res += '</tr>'