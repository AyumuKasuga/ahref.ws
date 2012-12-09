from urllib2 import urlparse

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.simplejson import dumps
from django.core.urlresolvers import reverse

from shorturl.models import ShortUrl
from shorturl.forms import AddUrlForm


def main_page(request):
    host_parts = request.get_host().split('.')
    if len(host_parts) == 3:
        return follow_url(request, host_parts[0])
    return render_to_response('templates/index.html', {'form': AddUrlForm})


def get_short_link(long_url):
    if long_url.find('http://') != -1 and long_url.find('https://') != -1:
        long_url = 'http://%s' % long_url
    parsed_url = urlparse.urlparse(long_url)
    if parsed_url.netloc.find(request.get_host()) != -1:
        ret = {'status': 'fail', 'error': 'recursive url'}


def get_long_link(url):
    pass


def add_url(request):
    if request.method == 'POST':
        form = AddUrlForm(request.POST)
        if form.is_valid():
            src_url = form.cleaned_data['url']
            if src_url.find('http://') != -1 and src_url.find('https://') != -1:
                src_url = 'http://%s' % src_url
            parsed_url = urlparse.urlparse(src_url)
            if parsed_url.netloc.find(request.get_host()) != -1:
                ret = {'status': 'fail', 'error': 'recursive url'}
            else:
                try:
                    url_obj = ShortUrl.objects.get(source_url = src_url)
                except ShortUrl.DoesNotExist:
                    url_obj = ShortUrl(source_url = src_url)
                    url_obj.save()
                short_link = "http://%s.%s" % (url_obj.short_url, request.get_host())
                alt_short_link = 'http://%s%s' % (request.get_host(), reverse('shorturl.views.follow_url', args=(url_obj.short_url,)))
                ret = {'status': 'ok', 'short_url': short_link, 'alt_short_url': alt_short_link}
        else:
            ret = {'status': 'fail', 'error': 'not valid url'}
        return HttpResponse(dumps(ret))


def follow_url(request, url):
    try:
        url_obj = ShortUrl.objects.get(short_url = url)
    except ShortUrl.DoesNotExist:
        main_host = '.'.join(request.get_host().split('.')[1:])
        return HttpResponseRedirect('http://%s' % main_host)
    else:
        url_obj.clicks += 1
        url_obj.save()
        return HttpResponseRedirect(url_obj.source_url)