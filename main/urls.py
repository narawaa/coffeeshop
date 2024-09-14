from django.urls import path
from main.views import frontpage, create_product_entry, show_xml, show_xml_by_id, show_json, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]