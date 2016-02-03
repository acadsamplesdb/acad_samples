from django import template
register = template.Library()

@register.filter
def floatcutzeroes(value):
    return float(value)

@register.simple_tag
def filetype_icon(file_name, **kwargs):
    icon_name = 'fa-file-o'
    size = kwargs['size'] if 'size' in kwargs else '2em'
    import os
    _, ext = os.path.splitext(file_name)
    if len(ext) > 2:
        ext = ext[1:]
        icons = {'pdf': 'pdf',
                 'jpg': 'picture',
                 'png': 'picture',
                 'txt': 'text',
                 'docx': 'word',
                 'xlsx': 'excel',
                 'zip': 'archive',
                 'gz': 'archive',
                }
        if ext in icons.keys():
            icon_name = 'fa-file-%s-o' % icons[ext]

    return '<i class="fa %s" style="margin-right:10px;font-size:%s;"></i>' % (icon_name, size)