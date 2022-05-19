import json
from django.shortcuts import render ,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .forms import UploadFileFormUser
from .models import UserFileUpload
from pdf2docx import parse
import aspose.words as aw
from htmldocx import HtmlToDocx
import pdfkit
import os 
from .task import document_converter_celery_task_function
from django.shortcuts import render
from .task import go_to_sleep
from celery.result import AsyncResult
from celery_progress.backend import Progress
from django.views.decorators.cache import never_cache


@never_cache
def get_progress(request, task_id):
    progress = Progress(AsyncResult(str(task_id)))
    return HttpResponse(json.dumps(progress.get_info()), content_type='application/json')

def docx2pdf_converter(request):
    if request.method == 'POST':
        form = UploadFileFormUser(request.POST, request.FILES)
        if form.is_valid():
            form_current_choices = form.cleaned_data['current_choices']
            form_file_data = form.cleaned_data['file']
            form_convert_choices= form.cleaned_data['convert_choices']
            form_file_data = str(form_file_data)
            form_convert_choices = str(form_convert_choices)
            form_current_choices = str(form_current_choices)
            document_converter_celery_task_function.delay(form_current_choices,form_file_data,form_convert_choices)
    else:
        form = UploadFileFormUser()
    tasks1 = go_to_sleep.delay(20)
    return render(request, 'docversion.html', {'form': form ,'task_id': tasks1.task_id})

# End Document Conversion Code