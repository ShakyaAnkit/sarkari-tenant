from django import template
from django.urls import reverse

from home.lang.utils import translate, get_locale

register = template.Library()

class LanguageNode(template.Node):
	def __init__(self, nodelist):
		self.nodelist = nodelist

	def render(self, context):
		output = self.nodelist.render(context)
		return translate(output)

@register.tag('trans')
def do_trans(parser, _):
	"""
	Localize words `{% trans %}` and `{% endtrans %}`
	"""
	nodelist = parser.parse(('endtrans',))
	parser.delete_first_token()
	return LanguageNode(nodelist)

@register.simple_tag
def url_localized(name, *args, **kwargs):
	print(name, args, kwargs)
	if get_locale() == 'en':
		name = name.replace('home:', 'home_en:')
	return reverse(name, args=args, kwargs=kwargs)
