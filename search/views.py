from __future__ import absolute_import, unicode_literals

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from itertools import chain
from wagtail.wagtailsearch.backends import get_search_backend

from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch.models import Query
from home.models import Post

def search(request):
    search_query = request.GET.get('query', None)
    # post = request.GET.get('post', 1)

    # Search
    if search_query:
        s = get_search_backend()

        search_results = s.search(search_query, Post)
        query = Query.get(search_query)
        #search_results = list(chain(profile_results)
        # Record hit
        query.add_hit()
    else:
        search_results = Post.objects.none()

    # Pagination
    paginator = Paginator(search_results, 20)
    try:
        search_results = paginator.page(search_query)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return render(request, 'search/search.html', {
        'search_query': search_query,
        'search_results': search_results,
    })
