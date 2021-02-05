from django.urls import path
from .views import HomepageView, world_dataset, incidences_dataset, upload_gpx
app_name = 'reporter'

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('world_data', world_dataset, name='world_data'),
    path('incidence_data', incidences_dataset, name='incidence_data'),
    path('upload_gpx', upload_gpx, name='upload-gpx'),
]