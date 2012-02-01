from django_pancake.flatten import flatten

# template_name: (template_source, pancake_source),
TESTS = {
    # No inheritance.
    'test1': ('Some text here', 'Some text here'),
    'test2': ('{% unknown_block_tag %}Text here', '{% unknown_block_tag %}Text here'),

    # Basic inheritance.
    'base1': ('<html><title>{% block title %}{% endblock %}</title></html>', '<html><title></title></html>'),
    'child1': ('{% extends "base1" %} {% block title %}It worked{% endblock %}', '<html><title>It worked</title></html>'),

    # Junk in child templates.
    'junk1': ('{% extends "base1" %} Junk goes here', '<html><title></title></html>'),
    'junk2': ('{% extends "base1" %} Junk goes here {% some_tag %}', '<html><title></title></html>'),
    'junk3': ('{% extends "base1" %} Junk goes here {% some_tag %}  {% block title %}Worked{% endblock %}', '<html><title>Worked</title></html>'),

    # Inheritance with default values in blocks.
    'defaultbase1': ('<title>{% block title %}Default{% endblock %}</title>', '<title>Default</title>'),
    'default1': ('{% extends "defaultbase1" %}', '<title>Default</title>'),
    'default2': ('{% extends "defaultbase1" %}{% block title %}No default{% endblock %}', '<title>No default</title>'),

    # Blocks within blocks.
    'withinbase1': ('<title>{% block fulltitle %}{% block title %}Welcome{% endblock %} | Example.com{% endblock %}</title>', '<title>Welcome | Example.com</title>'),
    'within1': ('{% extends "withinbase1" %}  {% block fulltitle %}Yay{% endblock %}', '<title>Yay</title>'),
    'within2': ('{% extends "withinbase1" %}  {% block title %}Some page{% endblock %}', '<title>Some page | Example.com</title>'),

    # Three-level inheritance structure.
    '3levelbase1': ('{% block content %}Welcome!<br>{% block header %}{% endblock %}{% endblock %}', 'Welcome!<br>'),
    '3levelbase2': ('{% extends "3levelbase1" %}{% block header %}<h1>{% block h1 %}{% endblock %}</h1>{% endblock %}', 'Welcome!<br><h1></h1>'),
    '3level1': ('{% extends "3levelbase2" %}{% block h1 %}Title goes here{% endblock %}', 'Welcome!<br><h1>Title goes here</h1>'),

    # {% load %} statements get bubbled up and combined.
    'loadbase1': ('{% load webdesign %}<html><title>{% block title %}{% endblock %}</title></html>', '{% load webdesign %}<html><title></title></html>'),
    'load1': ('{% extends "base1" %}{% load humanize %}{% block title %}Load 1{% endblock %}', '{% load humanize %}<html><title>Load 1</title></html>'),
    'load2': ('{% extends "loadbase1" %}{% load humanize %}{% block title %}Load 2{% endblock %}', '{% load humanize webdesign %}<html><title>Load 2</title></html>'),
}
TEMPLATES = dict((k, v[0]) for k, v in TESTS.items())

def test_flatten():
    for template_name, (template_source, pancake_source) in TESTS.items():
        yield check_flatten, template_name, pancake_source

def check_flatten(template_name, expected):
    result = flatten(template_name, TEMPLATES)
    assert result == expected, 'expected %r, got %r' % (expected, result)
