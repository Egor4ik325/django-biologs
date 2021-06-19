# Creating user abilities

1. Create and link app
2. Add (default/custom) and link urls
3. Create custom views
4. Create templates

'app_name:url_name' - url link.
'template_sub_dir/file.html' - file link.

Custom registration view should:
1. make a form for registering users (Django default)
2. CUSTOM USER LOGIC
3. login user for Django infrastructure (django.contrib.auth(authentication module).models.User)
