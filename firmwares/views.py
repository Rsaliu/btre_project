from django.shortcuts import render
from django.http import HttpResponse,Http404, response
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json

def get_version():
    pass

def download(request):
    file_path = os.path.join(settings.BASE_DIR,"firmwares/https_ota_variant_real.ino.esp32.bin")
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def data(request):
    device_id=request.POST['deviceId']
    longitude=request.POST['longitude']
    latitude=request.POST['latitude']
    print(f'payload: received is: device_is: {device_id} longitude: {longitude} latitude: {latitude}')
    return HttpResponse(status=201)

@csrf_exempt
def iotpayload(request):
    json_request=json.loads(request.body)
    print(f'payload: received is: {json_request}')
    return HttpResponse(status=201)
