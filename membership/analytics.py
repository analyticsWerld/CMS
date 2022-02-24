from pty import CHILD
from .models import Member
from django.db.models import Q,Count
import json


def class_summary():
    dataset = Member.objects.values('church_class').annotate(
        counts = Count('church_class')
    ).order_by('church_class')
    
    classes = []
    counts = []     
    for entry in dataset:
        classes.append("%s Class"%entry.get("church_class"))
        counts.append(entry.get("counts"))

    # chart = {
    #     'chart': {'type': 'pie'},
    #     'title': {'text': 'Titanic Survivors by Ticket Class'},
    #     'series': [{
    #         'name': 'Embarkation Port',
    #         'data': list(map(lambda row: {'name': port_display_name[row['embarked']], 'y': row['total']}, dataset))
    #     }]
    # }

    return {
        'categories': json.dumps(classes),
        'counts': json.dumps(counts)
    }

    return dataset
def gender_summary():
    dataset = Member.objects.values('church_class').annotate(
        male_count = Count('church_class',filter=Q(gender = "MALE")),
        female_count = Count('church_class',filter=Q(gender = "FEMALE"))
    ).order_by('church_class')
    
    classes = []
    males = []
    females = []

    for entry in dataset:
        classes.append("%s Class"%entry.get("church_class"))
        males.append(entry.get("male_count"))
        females.append(entry.get("female_count"))
    
    male_series = {
        'name' : 'Males',
        'data' : males,
        'color' : 'green'
    }

    female_series = {
        'name' : 'Females',
        'data' : females,
        'color' : 'red'
    }

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Gender Distribution Per Classes'},
        'xAxis': {'categories': classes},
        'series': [male_series, female_series]
    }

    return json.dumps(chart)


def baptised_summary():
    dataset = Member.objects.values('church_class').exclude(church_class='CHILDREN').annotate(
        baptised_count = Count('gender',filter=Q(baptised = "YES")),
        not_baptised_count = Count('gender',filter=Q(baptised = "NO"))
    ).order_by('church_class')
    gender = []
    baptised = []
    not_baptised = []
    for entry in dataset:
        gender.append("%s"%entry.get("church_class"))
        baptised.append(entry.get("baptised_count"))
        not_baptised.append(entry.get("not_baptised_count"))
    
    baptised_series = {
        'name' : 'Baptised',
        'data' : baptised,
        'color' : 'green'
    }

    not_baptised_series = {
        'name' : 'Not Baptised',
        'data' : not_baptised,
        'color' : 'red'
    }

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Baptismal Status Distribution'},
        'xAxis': {'categories': gender},
        'series': [baptised_series, not_baptised_series]
    }

    dump = json.dumps(chart)
    return dump

member_summary_context = {'baptised':baptised_summary(),'gender':gender_summary(),'summaries':class_summary()}
