# You can use the following variables:
#  - self: ORM model of the record on which the action is triggered
#  - object: browse_record of the record on which the action is triggered if there is one, otherwise None
#  - pool: ORM model pool (i.e. self.pool)
#  - time: Python time module
#  - cr: database cursor
#  - uid: current user id
#  - context: current context
# If you plan to return an action, assign: action = {...}

def parse_description(description):
  '''
name: [your-name]
phone: [phone]
city: [city]
zip: [zip]
email: [email]
notes: [notes]

--
This  mail was sent through contact form from the website XXXXXXXXXX using Wordpress Contact Form Plugin
  '''
  fields=['name','phone','city','zip','email','notes']
  _dict={}
  for line in description.split('\n'):
    for field in fields:
        if field in line:
            split_line=line.split(':')
            if len(split_line)>1:
                _dict[field]=split_line[1]
  return _dict

lead=self.browse(cr,uid,context['active_id'],context=context)
description=lead['description']
_dict=parse_description(description)
self.write(cr,uid,context['active_id'],{
                        'contact_name':_dict.get(u'name'),
                        'phone':_dict.get(u'phone'),
                        'description':_dict.get(u'notes'),
                        'city':_dict.get(u'city'),
                        'email_from':_dict.get(u'email'),
                        'zip':_dict.get(u'zip')})
