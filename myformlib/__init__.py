"""myformlib is formlib for `attrs`.
"""
import attr
from webhelpers2.html import tags

__version__ = "0.1"


class Form:
    def __init__(self, cls):
        self.cls = cls
        self.fields = attr.fields(cls)

    @property
    def field_renderers(self):
        return [tags.text(name=f.name) for f in self.fields]

    def iter_render(self, action):
        yield tags.form(url=action)
        yield from self.field_renderers
        yield tags.end_form()

    def render(self, action):
        return "".join(self.iter_render(action))
