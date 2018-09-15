from datetime import datetime
import attr


@attr.s
class Person:
    name = attr.ib(type=str)
    birthday = attr.ib(type=datetime)


def test_render_class():
    from myformlib import Form

    form = Form(Person)
    result = form.render("http://example.com")
    assert result == (
        '<form action="http://example.com" method="post">'
        '<input id="name" name="name" type="text" />'
        '<input id="birthday" name="birthday" type="text" />'
        "</form>"
    )
