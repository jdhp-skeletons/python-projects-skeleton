#!/usr/bin/env python3

from jinja2 import Template
import os
import yaml

with open("vars.yml") as stream:
    vars_dict = yaml.safe_load(stream)

print(vars_dict)
print(" --- ")

TEMPLATE_FILE_LIST = ['README.rst.j2']   # TODO: recursively explore the "templates" directory instead of manually declaring files here...

for template_filename in TEMPLATE_FILE_LIST:
    with open(os.path.join("templates", template_filename), 'r') as fd_template:   # TODO...
        template = Template(fd_template.read())

        output_filename = os.path.join("..", template_filename.rstrip(".j2"))   # TODO...
        with open(output_filename, 'w') as fd_out:
            print(f"{ template_filename } -> { output_filename }")
            fd_out.write(template.render(vars_dict))
