import csv
import json
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from covid.models import SideEffect, User, Vaccination, VaccinationSideEffect
from django.db.models import Count, Q

from django.core import serializers

all = Vaccination.objects.filter(~Q(vaccine_name='')).count()

count_1 = Vaccination.objects.filter(vaccine_times=1).filter(~Q(vaccine_name ='')).count()
count_2 = Vaccination.objects.filter(vaccine_times=2).filter(~Q(vaccine_name ='')).count()

count_f = User.objects.filter(gender='F').count()
count_m = User.objects.filter(gender='M').count()

count_10 = User.objects.filter(age='10~20').count()
count_30 = User.objects.filter(age='30~40').count()
count_50 = User.objects.filter(age='50~60').count()
count_70 = User.objects.filter(age='70').count()

count_underlying_true = User.objects.filter(underlying=True).count()
count_underlying_false = User.objects.filter(underlying=False).count()

count_pfizer = Vaccination.objects.filter(vaccine_name='화이자').count()
count_moderna = Vaccination.objects.filter(vaccine_name='모더나').count()
count_janssen = Vaccination.objects.filter(vaccine_name='얀센').count()
count_astrazeneca = Vaccination.objects.filter(vaccine_name='아스트라제네카').count()
count_etc = all-(count_pfizer+count_moderna+count_janssen+count_astrazeneca)

# def add_percentage(vaccine_list):
#     for vaccine in vaccine_list:
#         vaccine['percentage'] = round((vaccine['count']/all) *100,2)

def main(request):
    # initiate()

    context = {
        'vaccine_list' : json.dumps([
            {'label': '기타', 'value': count_etc, 'color': '#D1B2FF', 'isShow': True, 'percentage': round((count_etc/all)*100, 2)},
            {'label': '얀센', 'value': count_janssen, 'color': '#B2CCFF', 'isShow': True, 'percentage': round((count_janssen/all)*100, 2)},
            {'label': '아스트라제네카', 'value': count_astrazeneca, 'color': '#B2EBF4', 'isShow': True, 'percentage': round((count_astrazeneca/all)*100, 2)},
            {'label': '모더나', 'value': count_moderna, 'color': '#D1B2FF', 'CEF279': True, 'percentage': round((count_moderna/all)*100, 2)},
            {'label': '화이자', 'value': count_pfizer, 'color': '#FFE08C', 'isShow': True, 'percentage': round((count_pfizer/all)*100, 2)},
        ])
    }

    
    return render(request, "main.html", context)

    # vaccine_list = Vaccination.objects.values('vaccine_name').annotate(count=Count('vaccine_name')).order_by('count')
    # add_percentage(vaccine_list)
    # return render(request, "main.html", {"vaccine_list": json.dumps(list(vaccine_list))})

def create(request):
    
    if request.POST.get('vaccine_name_1_etc'):
        vaccine_name_1 = request.POST.get('vaccine_name_1_etc')
    else:
        vaccine_name_1 = request.POST.get('vaccine_name_1')

    if request.POST.get('vaccine_name_2_etc'):
        vaccine_name_2 = request.POST.get('vaccine_name_2_etc')
    else:
        vaccine_name_2 = request.POST.get('vaccine_name_2')
    
    #user 
    user = User(
        gender=request.POST.get('gender'), 
        age=request.POST.get('age'), 
        underlying=request.POST.get('underlying')
    )
    user.save()

    #first vaccination
    first_vaccination = Vaccination(
        user = user,
        vaccine_times = 1,
        vaccine_name = vaccine_name_1
    )
    first_vaccination.save()

    #first vaccination side effect
    if request.POST.getlist('side_effect_1[]'):
        for se in request.POST.getlist('side_effect_1[]'):
            if se != 'etc':
                side_effect = SideEffect.objects.get(id=se)
                side_effect_etc = None
            else:
                side_effect = None
                side_effect_etc = request.POST.get('side_effect_1_etc')
            vaccine_side_effect_1 = VaccinationSideEffect(
                vaccination = first_vaccination,
                side_effect = side_effect,
                side_effect_etc = side_effect_etc
            )
            vaccine_side_effect_1.save()

    #second vaccination
    second_vaccination = Vaccination(
        user = user,
        vaccine_times = 2,
        vaccine_name = vaccine_name_2
    )
    second_vaccination.save()

    #second vaccination side effect
    if request.POST.getlist('side_effect_2[]'):
        for se in request.POST.getlist('side_effect_2[]'):
            if se != 'etc':
                side_effect = SideEffect.objects.get(id=se)
                side_effect_etc = None
            else:
                side_effect = None
                side_effect_etc = request.POST.get('side_effect_1_etc')
            vaccine_side_effect_2 = VaccinationSideEffect(
                vaccination = second_vaccination,
                side_effect = side_effect,
                side_effect_etc = side_effect_etc
            )
            vaccine_side_effect_2.save()
    
    #return result
    return redirect('covid:survey')




def vaccination(request):
    context = {
        'vaccine_list_times' : json.dumps([
            {'label': '1차', 'value': count_1, 'color': '#D1B2FF', 'isShow': True, 'percentage': round((count_1/all)*100,2)},
            {'label': '2차', 'value': count_2, 'color': '#B2CCFF', 'isShow': True, 'percentage': round((count_2/all)*100,2)} 
        ]),
        'vaccine_list_gender' : json.dumps([
            {'label': '남성', 'value': count_m, 'color': '#D1B2FF', 'isShow': True, 'percentage': round((count_m/all)*100,2)},
            {'label': '여성', 'value': count_f, 'color': '#B2CCFF', 'isShow': True, 'percentage': round((count_f/all)*100,2)} 
        ]),
        'vaccine_list_age' : json.dumps([
            {'label': '10~20대', 'value': count_10, 'color': '#D1B2FF', 'isShow': True, 'percentage': round((count_10/all)*100,2)},
            {'label': '30~40대', 'value': count_30, 'color': '#B2CCFF', 'isShow': True, 'percentage': round((count_30/all)*100,2)},
            {'label': '50~60대', 'value': count_50, 'color': '#D1B2FF', 'B2EBF4': True, 'percentage': round((count_50/all)*100,2)},   
            {'label': '70대 이상', 'value': count_70, 'color': '#D1B2FF', 'isShow': True, 'percentage': round((count_70/all)*100,2)},
        ]),
        'vaccine_list_underlying' : json.dumps([
            {'label': '기저질환 있음', 'value': count_underlying_true, 'color': '#D1B2FF', 'isShow': True, 'percentage': round((count_underlying_true/all)*100, 2)},
            {'label': '기저질환 없음', 'value': count_underlying_false, 'color': '#B2CCFF', 'isShow': True, 'percentage': round((count_underlying_false/all)*100, 2)},
        ]),
        'vaccine_list_type' : json.dumps([
            {'label': '기타', 'value': count_etc, 'color': '#D1B2FF', 'isShow': True, 'percentage': round((count_etc/all)*100, 2)},
            {'label': '얀센', 'value': count_janssen, 'color': '#B2CCFF', 'isShow': True, 'percentage': round((count_janssen/all)*100, 2)},
            {'label': '아스트라제네카', 'value': count_astrazeneca, 'color': '#B2EBF4', 'isShow': True, 'percentage': round((count_astrazeneca/all)*100, 2)},
            {'label': '모더나', 'value': count_moderna, 'color': '#D1B2FF', 'isShow': True, 'percentage': round((count_moderna/all)*100, 2)},
            {'label': '화이자', 'value': count_pfizer, 'color': '#FFE08C', 'isShow': True, 'percentage': round((count_pfizer/all)*100, 2)},
        ])
    }

    return render(request, "vaccination.html", context)
    


def make_condition(column, list):
    if(list):
        list[:] = [("( {} = '{}' )".format(column, item)) for item in list]
        sql = " AND ({}) ".format(' or '.join( list ))
        return sql        
    else:
        return ''

def effect(request):

    condition = dict()
    condition['vaccine_name'] = ''
    condition['age']  = ''
    condition['gender']    = ''
    condition['underlying']   = ''

    if request.method == 'GET':
        print(request.GET)
        condition['vaccine_name'] = make_condition(column='vaccination.vaccine_name', list=request.GET.getlist('vaccine_name[]'))
        condition['age'] = make_condition(column='user.age', list=request.GET.getlist('age[]'))
        condition['gender'] = make_condition(column='user.gender', list=request.GET.getlist('gender[]'))
        condition['underlying'] = make_condition(column='user.underlying', list=request.GET.getlist('underlying[]'))

    # create sql query
    sql = """ 
                SELECT
                    user.gender, user.age, user.underlying,
                    side_effect.id, side_effect.side_effect_name, count(side_effect.side_effect_name) as count,
                    vaccination.vaccine_name
                FROM side_effect
                JOIN vaccination_side_effect ON side_effect.id = vaccination_side_effect.side_effect
                JOIN vaccination ON vaccination.id = vaccination_side_effect.vaccination
                {}
                JOIN user ON user.id = vaccination.user
                {}{}{}
                GROUP BY side_effect.side_effect_name
                ORDER BY count
        """.format(condition['vaccine_name'], condition['gender'],condition['age'], condition['underlying'])

    print(sql)

    # return result
    se_status_list = list()
    se_status_query = SideEffect.objects.raw(sql)
    all= sum(se_status.count for se_status in se_status_query)
    for se_status in se_status_query:
        se_status_dict = dict()
        se_status_dict['label'] = se_status.side_effect_name
        se_status_dict['value'] = se_status.count
        se_status_dict['color'] = 'D1B2FF'
        se_status_dict['isShow'] = True
        se_status_dict['percentage'] = round((se_status.count/all)*100, 2)
        se_status_list.append(se_status_dict)
        print(se_status_dict)

    
    def get_checked(name, value):
        if value in request.GET.getlist(name):
            return 'checked'

    checked = { 
        'gender': {
            'M': get_checked('gender[]', 'M'),
            'F': get_checked('gender[]', 'F')
        },
        'age': {
            '10': get_checked('age[]', '10~20'),
            '30': get_checked('age[]', '30~40'),
            '50': get_checked('age[]', '50~60'),
            '70': get_checked('age[]', '70~')
        },
        'underlying':{
            't':get_checked('underlying[]', 'true'),
            'f':get_checked('underlying[]', 'false')
        },
        'vaccine':{
            '모더나':get_checked('vaccine_name[]', '모더나'),
            '화이자':get_checked('vaccine_name[]', '화이자'),
            '아스트라제네카':get_checked('vaccine_name[]', '아스트라제네카'),
            '얀센':get_checked('vaccine_name[]', '얀센'),
        }
    }
    
    context = {
        'side_effect_status' : json.dumps(se_status_list),
        'checked' : checked
    }
    return render(request, "effect.html", context)

def survey(request):
    side_effect_list = SideEffect.objects.all()
    return render(request, "survey.html", {'side_effect_list':side_effect_list})

def search(request):
    gender = request.GET.getlist('gender')
    age = request.GET.getlist('gender')
    underlying = request.GET.getlist('underlying')
    vaccine_name = request.GET.getlist('vaccine_name')

    se_list = VaccinationSideEffect.objects.select_related('vaccination')
    return 

def create(request):

    if request.POST.get('vaccine_name_1_etc'):
        vaccine_name_1 = request.POST.get('vaccine_name_1_etc')
    else:
        vaccine_name_1 = request.POST.get('vaccine_name_1')

    if request.POST.get('vaccine_name_2_etc'):
        vaccine_name_2 = request.POST.get('vaccine_name_2_etc')
    else:
        vaccine_name_2 = request.POST.get('vaccine_name_2')
    
    #user 
    user = User(
        gender=request.POST.get('gender'), 
        age=request.POST.get('age'), 
        underlying=request.POST.get('underlying')
    )
    user.save()

    #first vaccination
    first_vaccination = Vaccination(
        user = user,
        vaccine_times = 1,
        vaccine_name = vaccine_name_1
    )
    first_vaccination.save()

    #first vaccination side effect
    if request.POST.getlist('side_effect_1[]'):
        for se in request.POST.getlist('side_effect_1[]'):
            if se != 'etc':
                side_effect = SideEffect.objects.get(id=se)
                side_effect_etc = None
            else:
                side_effect = None
                side_effect_etc = request.POST.get('side_effect_1_etc')
            vaccine_side_effect_1 = VaccinationSideEffect(
                vaccination = first_vaccination,
                side_effect = side_effect,
                side_effect_etc = side_effect_etc
            )
            vaccine_side_effect_1.save()

    #second vaccination
    second_vaccination = Vaccination(
        user = user,
        vaccine_times = 2,
        vaccine_name = vaccine_name_2
    )
    second_vaccination.save()

    #second vaccination side effect
    if request.POST.getlist('side_effect_2[]'):
        for se in request.POST.getlist('side_effect_2[]'):
            if se != 'etc':
                side_effect = SideEffect.objects.get(id=se)
                side_effect_etc = None
            else:
                side_effect = None
                side_effect_etc = request.POST.get('side_effect_1_etc')
            vaccine_side_effect_2 = VaccinationSideEffect(
                vaccination = second_vaccination,
                side_effect = side_effect,
                side_effect_etc = side_effect_etc
            )
            vaccine_side_effect_2.save()
    
    #return result
    return JsonResponse({'good':'good'})
    return redirect('covid:survey')
    

def initiate():
    
    side_effect_list = SideEffect.objects.values_list('side_effect_name', flat=True)
    csv_file = csv.reader(open('covid_final.csv', mode='r', encoding='utf-8'))

    my_list = list()
    for rows in csv_file:
        my_dict = dict()
        my_dict['gender'] = rows[0]
        my_dict['age'] = rows[1]
        my_dict['underlying'] = rows[2]
        my_dict['vaccine_name_1'] = rows[3]
        my_dict['side_effect_1'] = rows[4].split("\t")
        my_dict['vaccine_name_2'] = rows[5]
        my_dict['side_effect_2'] = rows[6].split("\t")
        my_list.append(my_dict)

    for my_dict in my_list:

        # user
        user = User(
            gender = my_dict['gender'],
            age = my_dict['age'],
            underlying = my_dict['underlying']
        )
        user.save()

        #first vaccination
        first_vaccination = Vaccination(
            user = user,
            vaccine_times = 1,
            vaccine_name = my_dict['vaccine_name_1']
        )
        first_vaccination.save()

        #first vaccination side effect
        if my_dict['side_effect_1']:
            for se in my_dict['side_effect_1']:
                if se:
                    if se in side_effect_list:
                        side_effect = SideEffect.objects.get(side_effect_name=se)
                        side_effect_etc = None
                    else:
                        side_effect = None
                        side_effect_etc = se

                    vaccine_side_effect_1 = VaccinationSideEffect(
                        vaccination = first_vaccination,
                        side_effect = side_effect,
                        side_effect_etc = side_effect_etc
                    )
                    vaccine_side_effect_1.save()

        #first vaccination
        second_vaccination = Vaccination(
            user = user,
            vaccine_times = 2,
            vaccine_name = my_dict['vaccine_name_2']
        )
        second_vaccination.save()

        #first vaccination side effect
        if my_dict['side_effect_2']:
            for se in my_dict['side_effect_2']:
                if se:
                    if se in side_effect_list:
                        side_effect_2 = SideEffect.objects.get(side_effect_name=se)
                        side_effect_etc_2 = None
                    else:
                        side_effect_2 = None
                        side_effect_etc_2 = se

                    vaccine_side_effect_2 = VaccinationSideEffect(
                        vaccination = second_vaccination,
                        side_effect = side_effect_2,
                        side_effect_etc = side_effect_etc_2
                    )
                    vaccine_side_effect_2.save()