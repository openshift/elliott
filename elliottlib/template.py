from __future__ import absolute_import, print_function, unicode_literals
from mako.template import Template


def render_topic(template, impact="Important"):
    t = Template(template)
    return t.render(impact=impact)
