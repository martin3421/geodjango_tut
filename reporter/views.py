import os
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import WorldBorder, Incidence
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.gis.geos import Point, LineString, MultiLineString
from agricom.settings import MEDIA_ROOT

from .forms import UploadGpxForm
from .models import GPXPoint, GPXTrack, gpxFile

from django.conf import settings

import gpxpy
import gpxpy.gpx

class HomepageView(TemplateView):
    template_name = 'index.html'

def world_dataset(request):
    world = serialize('geojson', WorldBorder.objects.all())
    return HttpResponse(world, content_type='json')

def incidences_dataset(request):
    incidences = serialize('geojson', Incidence.objects.all())
    return HttpResponse(incidences, content_type='json')

def upload_gpx(request):
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        form = UploadGpxForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = gpxFile(gpx_file=request.FILES['gpx_file'])
            new_file.save()
            SaveGPXtoPostGIS(request.FILES['gpx_file'], new_file)

            # Redirect to the document list after POST
            return redirect('reporter:upload-gpx')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = UploadGpxForm()  # An empty, unbound form

    # Load documents for the list page
    gpx_files = gpxFile.objects.all()

    # Render list page with the documents and the form
    context = {'gpx_files': gpx_files, 'form': form, 'message': message}
    return render(request, 'list.html', context)

def SaveGPXtoPostGIS(file_data, file_instance):
    file_path = os.path.join(MEDIA_ROOT,'gpx_files', file_data.name)
    with open(file_path) as gpxfile:
        gpx = gpxpy.parse(gpxfile)
        if gpx.waypoints:        
            for waypoint in gpx.waypoints: 
                print(waypoint.name)
        if gpx.tracks:
            for track in gpx.tracks:
                for extension in track.extensions:
                    print(extension.name)
                # #print(track)
                # for segment in track.segments:
                # #    print(segment)
                #     for point in segment.points:
                #         print(point)
    #gpx_file = open(settings.MEDIA_ROOT+ '/uploaded_gpx_files'+'/' + f.name)
    #gpx = gpxpy.parse(gpx_file)