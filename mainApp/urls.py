from django.urls import path

from mainApp.views import (create_product, show_json, show_json_by_id,
                           show_main, show_xml, show_xml_by_id)

app_name = 'mainApp'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]