from django.core.urlresolvers import reverse
from django import template
register = template.Library()

@register.filter
def floatcutzeroes(value):
    return float(value)

def _scale_image(file_id, **kwargs):
    # Not really scale image but use css to pretend for the time being
    img_url = reverse('download_file', args=(file_id,))
    width = kwargs['width'] if 'width' in kwargs else '200'
    height = kwargs['height'] if 'height' in kwargs else '200'
    padleft = kwargs['padleft'] if 'padleft' in kwargs else '5'
    return '<img src="%s" class="img-thumbnail" width="%s" height="%s" style="margin-right:%spx">' % (img_url, width, height, padleft)

@register.simple_tag
def filetype_icon(file_name, file_id, **kwargs):
    icon_name = 'fa-file-o'
    size = kwargs['size'] if 'size' in kwargs else '2em'
    import os
    _, ext = os.path.splitext(file_name)
    ext = ext.lower()
    if len(ext) > 2:
        ext = ext[1:]
        icons = {'pdf': 'pdf',
                 'txt': 'text',
                 'docx': 'word',
                 'xlsx': 'excel',
                 'zip': 'archive',
                 'gz': 'archive',
                }
        if ext in ['jpg', 'jpeg', 'png']:
            return _scale_image(file_id, **kwargs)
        elif ext in icons.keys():
            icon_name = 'fa-file-%s-o' % icons[ext]

    return '<i class="fa %s" style="margin-right:10px;font-size:%s;"></i>' % (icon_name, size)