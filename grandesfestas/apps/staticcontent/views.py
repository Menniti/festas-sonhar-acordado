from os.path import exists, join
from django.conf import settings
from django.views import static


def serve(request, path, document_root=None, show_indexes=False, fallback=None):
    if path.startswith('/'):
        path = path[1:]

    if path == '':
        path = './'

    if path.endswith('/') and exists(join(document_root, path, 'index.html')):
        path = 'index.html'

    if not exists(join(document_root, path)) and fallback:
        path = fallback

    return static.serve(request, path, document_root=document_root, show_indexes=show_indexes)
