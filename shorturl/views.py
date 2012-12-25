from urllib2 import urlparse

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.simplejson import dumps
from django.core.urlresolvers import reverse
from ahrefws.settings import DOMAIN_NAME

from shorturl.models import ShortUrl


def main_page(request):
    host_parts = request.get_host().split('.')
    if len(host_parts) == 3:
        return follow_url(host_parts[0])
    return render_to_response('templates/index.html', {})


def get_short_link(long_url):
    parsed_url = urlparse.urlparse(long_url)

    if parsed_url.scheme == '':
        long_url = 'http://%s' % long_url
    elif parsed_url.scheme not in ('http', 'https'):
        return {'status': 'fail', 'error': 'bad scheme url'}

    parsed_clean_url = urlparse.urlparse(long_url)
    if parsed_clean_url.netloc.find(DOMAIN_NAME) != -1:
        return {'status': 'fail', 'error': 'recursive url'}

    if long_url[-1] == '/':
        long_url = long_url[:-1]

    url_obj, created = ShortUrl.objects.get_or_create(source_url = long_url)
    short_link = "http://%s.%s" % (url_obj.short_url, DOMAIN_NAME)
    alt_short_link = 'http://%s%s' % (DOMAIN_NAME, reverse('shorturl.views.follow_url', args=(url_obj.short_url,)))
    ret = {'status': 'ok', 'short_url': short_link, 'alt_short_url': alt_short_link}
    if not created:
        ret.update({'created': url_obj.created.isoformat(), 'clicks': url_obj.clicks})
    return ret


def add_url(request):
    if request.method == 'POST':
        src_url = request.POST.get('url', '')
        if src_url != '':
            ret = get_short_link(src_url)
        else:
            ret = {'status': 'fail', 'error': 'empty url'}
        return HttpResponse(dumps(ret), mimetype='application/json')
    else:
        return HttpResponse('use POST for this url', mimetype='text/plain')

def follow_url(url):
    try:
        url_obj = ShortUrl.objects.get(short_url = url)
    except ShortUrl.DoesNotExist:
        return HttpResponseRedirect('http://%s' % DOMAIN_NAME)
    else:
        url_obj.clicks += 1
        url_obj.save()
        return HttpResponseRedirect(url_obj.source_url)


def api_help_page(request):
    return render_to_response('templates/api_help.html', {})