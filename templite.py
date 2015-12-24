#!/usr/bin/env python

context = {'name': 'Jair', 'date': 'Thursday'}

result = []
c_name = context['name']
c_date = context['date']
append_result = result.append
extend_result = result.extend
append_result('Hello, ')
append_result(c_name)
append_result('. Today is ')
append_result(c_date)

print ''.join(result)
