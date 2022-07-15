from views import *

urlpatterns = [
        ('listing/', cars_listing),
        ('create/', cars_create),
        ('retrieve/id', cars_retrieve),
        ('update/id', cars_update),
        ('delete/id', cars_delete),
]