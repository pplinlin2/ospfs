#!/usr/bin/env python

class CodeBuilder:
	def __init__(self, indent=0):
		self.code = []
		self.indent_level = indent

	def __str__(self):
		return ''.join(c for c in self.code)

	def add_line(self, line):
		self.code.append(' ' * self.indent_level + line + '\n')

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
	def __init__(self):
		code = CodeBuilder()
		code.add_line('def render_function(context):')
		code.indent()
		code.add_line('result = []')
		code.add_line('c_name = context["name"]')
		code.add_line('c_date = context["date"]')
		code.add_line('append_result = result.append')
		code.add_line('extend_result = result.extend')
		code.add_line('append_result("Hello, ")')
		code.add_line('append_result(c_name)')
		code.add_line('append_result(". Today is ")')
		code.add_line('append_result(c_date)')
		code.add_line('return "".join(result)')
		code.dedent()
		self._render_function = code.get_globals()['render_function']

	def render(self, context):
		return self._render_function(context)

print Templite().render({'name': 'Jair', 'date': 'Thursday'})
