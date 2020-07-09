from django.shortcuts import render, redirect
from . forms import Add_Player_Form,Job_Name_Form, Postion_Form
from . models import Player_Name, Jobs, Postion
import random

def start(request):
    return render(request, 'wolf/start.html')

    
def now_player(request):
    data = Player_Name.objects.all()
    params = {
            'title':'NOW PLAYER',
            'data':data,
            }
    return render(request,'wolf/now_player.html',params)


def create(request):
    if request.method == 'POST':
        obj = Player_Name()
        player = Add_Player_Form(request.POST, instance=obj)
        player.save()
        return redirect(to='/wolf/player')
    params = {
            'title':'ADD PLAYER',
            'form':Add_Player_Form(),
            }
    return render(request,'wolf/create.html',params)


def edit(request, num):
    obj = Player_Name.objects.get(id=num)
    if request.method == 'POST':
        friend = Add_Player_Form(request.POST, instance=obj)
        friend.save()
        return redirect(to='/wolf/player')
    params = {
            'id':num,
            'title':'PLAYER CHANGE',
            'form':Add_Player_Form(instance=obj),
            }
    return render(request, 'wolf/edit.html', params)


def delete(request, num):
    make = Player_Name.objects.get(id=num)
    if request.method == 'POST':
        make.delete()
        return redirect(to='/wolf/player')
    params = {
            'id':num,
            'title':'DELETE PLAYER',
            }
    return render(request, 'wolf/delete.html', params)


def job_create(request):
    if request.method == "POST" :
        obj = Jobs()
        job_name = Job_Name_Form(request.POST, instance=obj)
        job_name.save()
        return redirect(to="/wolf/job_create")
    params = {
            'title':'ADD JOB',
            'form':Job_Name_Form(),
            }
    return render(request,'wolf/job_create.html',params)


def job_how(request):
    data = Jobs.objects.all()
    if request.method =="POST" :
        return render(request, '/wolf/sub_start')
    params = {
            "data":data,
            "title":"TITLE",
            }
    return render(request, 'wolf/job_how.html',params)

def sub_start(request):
        
    params = {
            "title":"title",
            }
    return render(request, 'wolf/sub_start.html', params)

def how_many(request):
    data = Player_Name.objects.all().first()
    params = {
            'msg':'',
            'title':'HOW MANY?',
            'form':Postion_Form(),
            'sums':'',
            'msg2':'',
            }
    if request.method == 'POST' :
        obj = Postion()
        how_many = Postion_Form(request.POST, instance=obj)
        how_many.save()
        sums = int(obj.wolf) + int(obj.citizen) + int(obj.hunter) + int(obj.diviner) + int(obj.traitor) + int(obj.psychic)
        if sums != Player_Name.objects.all().count():
            params['msg'] = '参加人数と役職数が異なります'
            params['sums'] = sums
            params['msg2'] = '現在参加人数は' + str(Player_Name.objects.all().count()) + '人です'
            return render(request, 'wolf/how_many.html', params)
        if int(obj.wolf == 0):
            params['msg'] = '少なくともwolfは１必要です'
            return render(request, 'wolf/how_many.html', params)
        if int(obj.wolf) >= int(obj.citizen) + int(obj.hunter) + int(obj.diviner) + int(obj.traitor) + int(obj.psychic):
            params['msg'] = '人狼陣営が多すぎます'
            return render(request, 'wolf/how_many.html', params)
        return redirect(to='../check_job/'+str(data.id))
    return render(request, 'wolf/how_many.html/', params)


def check_job(request, num):
    data = Player_Name.objects.get(id=num)
    params = {
            'data':data,
            'title':'What is '+str(data)+ "'s job?",
            }
    return render(request, 'wolf/check_job.html', params)


how = Player_Name.objects.all().count()

i = 0

def look_job(request, num):
    obj = Postion.objects.all()
    human = Player_Name.objects.all()
    how_human = human.count()
    human_list = human.values_list('name',flat=True)
    new_human_list = list(human_list)
    for item in obj:
        obj_id = item.id
    
    now_obj = Postion.objects.get(id=obj_id)
    ok_list = []
    count = 0
    kazu = 0
    num = num + 1
    global i
    how = i
    while how != 0:
        del new_human_list[0]
        how -= 1
    i = i + 1
    
    while len(new_human_list) != len(ok_list):
        if count == 0:
            kazu = int(now_obj.wolf)
            while kazu != 0:
                ok_list.append('wolf')
                kazu = kazu - 1
            count = count + 1
        elif count == 1:
            kazu = now_obj.hunter
            while kazu != 0:
                ok_list.append('hunter')
                kazu = kazu - 1
            count += 1
        elif count == 2:
            kazu = now_obj.citizen
            while kazu != 0:
                ok_list.append('citizen')
                kazu -= 1
            count += 1
        elif count == 3:
            kazu = now_obj.diviner
            while kazu != 0:
                ok_list.append('diviner')
                kazu -= 1
            count += 1
        elif count == 4:
            kazu = now_obj.traitor
            while kazu != 0:
                ok_list.append('traitor')
                kazu -= 1
            count += 1
        elif count == 5:
            kazu = now_obj.psychic
            while kazu != 0:
                ok_list.append('psychic')
                kazu -= 1
            count += 1
            
    params = {
            'how_human':how_human,
            'i':i,
            'title':'YOUR JOB',
            'position':'',
            'num':num,
           }
    
    k = random.randint(0,now_obj.wolf+now_obj.hunter+now_obj.citizen+now_obj.traitor+now_obj.diviner+now_obj.psychic-1)
    decided_job = ok_list[k]
    if decided_job == 'wolf':
        now_obj.wolf = now_obj.wolf - 1
        now_obj.save()
        params['position'] = str(ok_list.pop(k))
    
    if decided_job == 'hunter':
        now_obj.hunter = now_obj.hunter - 1
        now_obj.save()
        params['position'] = str(ok_list.pop(k))
            
    if decided_job == 'citizen':
        now_obj.citizen = now_obj.citizen - 1
        now_obj.save()
        params['position'] = str(ok_list.pop(k))
            
    if decided_job == 'diviner':
        now_obj.diviner = now_obj.diviner - 1
        now_obj.save()
        params['position'] = str(ok_list.pop(k))
            
    if decided_job == 'traitor':
        now_obj.traitor = now_obj.traitor - 1
        now_obj.save()
        params['position'] = str(ok_list.pop(k))
            
    if decided_job == 'psychic':
        now_obj.psychic = now_obj.psychic - 1
        now_obj.save()
        params['position'] = str(ok_list.pop(k))
    return render(request, 'wolf/look_job.html', params)        


def finish(request):
    params = { 
            'msg':"LET'S START!!"
            }
    return render(request, 'wolf/finish.html', params)

    
    