openerp_web-leads-capture
=========================

Capture leads from your website or other form and insert them as new leads into your OpenERP v7 server. Do not lose an opportunity!

In this example I have set up Wordpress Contact Form Plugin to generate incoming email.

You should create a server action and include the text contained in the python file. Select "Leads/Oportunities" as Object and "Python code" as Action Type. Rename it as you like, for example, "Create lead from email" and set "True" as Condition and assign "5" as Priority.

This way every time a form is filled you will receive an email containing info that OpenERP will parse to create a new lead.
