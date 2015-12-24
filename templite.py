#!/usr/bin/env python

python_source = '''
def render_function(context):
	result = []
	c_name = context['name']
	c_date = context['date']
	append_result = result.append
	extend_result = result.extend
	append_result('Hello, ')
	append_result(c_name)
	append_result('. Today is ')
	append_result(c_date)

	return ''.join(result)
'''

global_namespace = {}
exec(python_source, global_namespace)

print global_namespace['render_function']({'name': 'Jair', 'date': 'Thursday'})
