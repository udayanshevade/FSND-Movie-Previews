from jinja2 import Template, Environment, PackageLoader, select_autoescape


env = Environment(
    loader=PackageLoader('env', 'static/templates')
)