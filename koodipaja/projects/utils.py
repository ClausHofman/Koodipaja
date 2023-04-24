from pprint import pprint
from .models import Project, ProjectTag, ProjectArticle, ProjectArticleTag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateProjects(request, projects, results):
    # Pagination
    page = request.GET.get('page')
    # results = 3 # results per page (hardcoded)
    paginator = Paginator(projects, results)  # projects = queryset
    pprint(paginator)

    # PageNotAnInteger error set page to 1
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    # EmptyPage error
    except EmptyPage:
        page = paginator.num_pages  # the last page
        projects = paginator.page(page)

    # for the situation that there would be an excessive amount of buttons due to a large amount of pages:
    # you can test it in projects.html: replace "for page in paginator.page_range" with "for page in custom_range"
    # custom_range = range(1, 1000) # custom range test code

    # let's create a "range window"
    # experiment with the number for different results
    leftIndex = (int(page) - 3)

    if leftIndex < 1:
        leftIndex = 1

    # experiment with the number for different results
    rightIndex = (int(page) + 4)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    print(projects)
    return custom_range, projects


def searchProjects(request):

    search_query = ''

    # "search_query" is in projects.html in this case
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        print('SEARCH:', search_query)

    tags = ProjectTag.objects.filter(name__icontains=search_query)

    projects = Project.objects.distinct().filter(  # distinct() to avoid duplicate search results!
        Q(title__icontains=search_query) |
        # Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        # does the Project tags queryset contain the tags that are input in the search_query (the filter)
        Q(tags__in=tags)
        # we could add another value that says a user has to exist
    )

    return projects, search_query


def searchArticles(request):

    search_query = ''

    # "search_query" is in projects.html in this case
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        print('SEARCH:', search_query)

    tags = ProjectArticleTag.objects.filter(name__icontains=search_query)

    articles = ProjectArticle.objects.distinct().filter(  # distinct() to avoid duplicate search results!
        Q(title__icontains=search_query) |
        # Q(description__icontains=search_query) |
        Q(body__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        # does the Project tags queryset contain the tags that are input in the search_query (the filter)
        Q(tags__in=tags)
        # we could add another value that says a user has to exist
    )

    return articles, search_query
