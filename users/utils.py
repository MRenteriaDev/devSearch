from .models import Profile, Skills
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateProfiles(request, profiles, results):
    page = request.GET.get('page')
    
    paginator= Paginator(profiles, results)


    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)
    
    leftIndex = (int(page) -4)

    if leftIndex < 1:
        leftIndex = 1

    righIndex = (int(page) +5)

    if righIndex > paginator.num_pages:
        righIndex = paginator.num_pages +1

    custom_range = range(leftIndex, righIndex)

    return custom_range, profiles

def searchFunction(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        print("Search : ", search_query)

    skills = Skills.objects.filter(name__iexact=search_query)

    profiles = Profile.objects.distinct().filter(Q(name__icontains=search_query) 
                            | Q(short_intro__icontains=search_query)
                            | Q(skills__in=skills))

    return profiles, search_query