#!/usr/bin/env python
import re

class CodeBuilder:
	def __init__(self, indent=0):
		self.code = []
		self.indent_level = indent

	def __str__(self):
		return ''.join(str(c) for c in self.code)

	def add_line(self, line):
		self.code.append(' ' * self.indent_level + line + '\n')

	def add_section(self):
		section = CodeBuilder(self.indent_level)
		self.code.append(section)
		return section

	INDENT_STEP = 4

	def indent(self):
		self.indent_level += self.INDENT_STEP

	def dedent(self):
		self.indent_level -= self.INDENT_STEP

	def get_globals(self):
		assert self.indent_level == 0
		global_namespace = {}
		exec(str(self), global_namespace)
		return global_namespace


class Templite():
	def __init__(self, text):
		code = CodeBuilder()
		code.add_line('def render_function(context):')
		code.indent()
		vars_all = set()
		vars_code = code.add_section()
		code.add_line('result = []')
		code.add_line('append_result = result.append')
		code.add_line('extend_result = result.extend')

		tokens = re.split(r"(?s)({{.*?}}|{%.*?%}|{#.*?#})", text)
		for token in tokens:
			if token.startswith('{{'):
				code.add_line('append_result({})'.format('c_' + token[2:-2]))
				vars_all.add(token[2:-2])
			else:
				code.add_line('append_result({})'.format(repr(token)))

		for var in vars_all:
			vars_code.add_line('c_{} = context["{}"]'.format(var, var))

		code.add_line('return "".join(result)')
		code.dedent()
		self._render_function = code.get_globals()['render_function']

	def render(self, context):
		return self._render_function(context)

print Templite('Hello, {{name}}. Today is {{date}}.').render({'name': 'Jair', 'date': 'Thursday'})
