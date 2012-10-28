from urllib2 import urlparse

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.simplejson import dumps
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from ahrefws.settings import SITE_ID

from shorturl.models import ShortUrl
from shorturl.forms import AddUrlForm

global_domain = Site.objects.get(pk=SITE_ID).domain

def main_page(request):
    host_parts = request.get_host().split('.')
    global_domain_parts = global_domain.split('.')
    if len(host_parts) - len(global_domain_parts) == 1:
        return follow_url(request, host_parts[0])
    return render_to_response('templates/index.html', {'form': AddUrlForm})


def add_url(request):
    if request.method == 'POST':
        form = AddUrlForm(request.POST)
        if form.is_valid():
            src_url = form.cleaned_data['url']
            if src_url.find('http://') != -1 and src_url.find('https://') != -1:
                src_url = 'http://%s' % src_url
            parsed_url = urlparse.urlparse(src_url)
            if parsed_url.netloc.find(global_domain) != -1:
                ret = {'status': 'fail', 'error': 'recursive url'}
            else:
                try:
                    url_obj = ShortUrl.objects.get(source_url = src_url)
                except ShortUrl.DoesNotExist:
                    url_obj = ShortUrl(source_url = src_url)
                    url_obj.save()
                short_link = "http://%s.%s" % (url_obj.short_url, global_domain)
                alt_short_link = 'http://%s%s' % (global_domain, reverse('shorturl.views.follow_url', args=(url_obj.short_url,)))
                ret = {'status': 'ok', 'short_url': short_link, 'alt_short_url': alt_short_link}
        else:
            ret = {'status': 'fail', 'error': 'not valid url'}
        return HttpResponse(dumps(ret))


def follow_url(request, url):
    try:
        url_obj = ShortUrl.objects.get(short_url = url)
    except ShortUrl.DoesNotExist:
        return HttpResponseRedirect('http://%s' % global_domain)
    else:
        return HttpResponseRedirect(url_obj.source_url)