from django.template import Library

register = Library()

@register.simple_tag
def get_icon_name(cause):
  icon_map = {
    'accident': 'fa-car-burst',
    'circulació': 'fa-car',
    'sin_incidencias': 'wrench',
    'other': 'fa-circle-exclamation',
  }
  return icon_map.get(cause, 'fa-circle-exclamation')

@register.simple_tag
def get_color_bg(cause):
  icon_map = {
    'accident': 'bg_accident',
    'circulació': 'bg_circulacio',
    'sin_incidencias': 'bg_sin_incidencias',
    'avaria': 'bg_accident',
    'other': 'bg_obras',
  }
  return icon_map.get(cause, 'bg_obras')




register.simple_tag(get_icon_name)

register.simple_tag(get_color_bg)