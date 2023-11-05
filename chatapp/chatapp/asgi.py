import os
#  async server gateway interface for websocket
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from .routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp.settings')


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    )
})
"""
 ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(rooms.routing.websocket_urlpatterns),
})
"""
