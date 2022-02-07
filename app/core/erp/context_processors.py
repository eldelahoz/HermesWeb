from django.conf import settings


def nom_web(request):
    return {'NOM_WEB_SITE': settings.NOM_WEB_SITE}
