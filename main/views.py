import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    logger.info('index page called')
    return render(request, 'main/index.html')
