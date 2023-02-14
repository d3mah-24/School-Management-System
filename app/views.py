from django.shortcuts import render
from platform import system
from .models import std as form, mark_ict
from django.db.models import F
from random import randint


# Create your views here.
def index(req):
    if req.method == "POST":
        if req.user.is_authenticated:
            q = form.objects.all().get(pass1=req.POST["password"], std_phone_num=req.POST["email"])
            q.view_counter = F('view_counter') + 1
            q.save()
            data = form.objects.all()

            return render(req, "teacher/index.html", {"data": data})
        if form.objects.filter(std_phone_num=req.POST["email"], pass1=req.POST["password"]).exists():
            q = form.objects.all().get(pass1=req.POST["password"], std_phone_num=req.POST["email"])
            q.view_counter = F('view_counter') + 1
            q.save()
            data = form.objects.all()

            return render(req, "teacher/index.html", {"data": data})

        else:
            return render(req, "index.html", {"p": 1, "msg": "Not valid password"})
    else:
        return render(req, "index.html", {"p": 0})
  
 
def mark(req):
    if req.method == "POST":
        for d in req.data.get('all', {}):

            id = d['id']
            ten1 = d['ten1']
            ten2 = d['ten2']
            ten3 = d['ten3']
            twenty = d['twenty']
            fifty = d['fifty']
            hundred = d['hundred']
            mark_ict.objects.all().fillter(std_data=id).update(ten1=ten1, ten2=ten2,
                                                                                          ten3=ten3, twenty=twenty,
                                                                                          fifty=fifty, hundred=hundred
                                                                                          )
            sa =  mark_ict.objects.all()
            return render(req,"mark.html",{"data":sa})
    else:
        sa = mark_ict.objects.all()
        return render(req, "teacher/mark.html", {"data": sa})

def login(req):
    return render(req, "index.html")


def forget(req):
    if req.method == "POST":

        if form.objects.filter(std_phone_num=req.POST["std_phone_num"],
                               parent_password=req.POST["parent_password"]).exists():
            form.objects.filter(parent_password=req.POST["parent_password"]).update(pass1=req.POST["new_pass"])
            q = form.objects.all().get(parent_password=req.POST["parent_password"])
            q.no_forget = F('no_forget') + 1
            q.save()
            return render(req, "index.html", {"p": 1, "msg": "changed"})
        else:
            return render(req, "index.html", {"p": 1, "msg": "Not valid password"})
    else:
        return render(req, "forget.html", {})


def create(req):
    if req.method == "POST":

        unique_id = req.POST["name"][0] + req.POST["fname"][1] + req.POST["name"][1] + req.POST["fname"][0] + str(
            randint(0, 9)) + str(
            req.POST["age"])
        os = system()

        l = "qa2zwhgmsxedcrfvtgb4ghhg6yhnujm7mgeriklop0"
        sk = [l[randint(0, 41)] for t in range(0, 5)]
        sk = "".join(sk)
        unique_id = str(sk[2:5][::-1]) + unique_id + "en" + sk[2:] + "en"

        form.objects.create(name=req.POST["name"], fname=req.POST["fname"], lname=req.POST["lname"],
                            kebele=req.POST["kebele"], gender=req.POST["gender"], grade=req.POST["grade"],
                            age=req.POST["age"], std_phone_num=req.POST["std_phone_num"],
                            parent_phone_num=req.POST["parent_phone_num"], parent_name=req.POST["parent_name"],
                            parent_password=req.POST["parent_password"], pass1=req.POST["pass"], unique_id=unique_id,
                            os=os, code=sk
                            )
        return render(req, "index.html", {"p": 1, "msg": "Account Is Succesfully Created"})
    else:
        return render(req, "index.html")

# Create your views here.
