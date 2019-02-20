from django.shortcuts import render
from django.http import HttpResponse
from django.utils.safestring import mark_safe
try:
    from django.core.context_processors import csrf
except:
    from django.template.context_processors import csrf
import datetime
from .models import *
import simplejson
def main(request):
    if request.method=="GET":
        models=request.session.get("models",None)
        if not models:
            models = [s['table'] for s in History.objects.values("table").distinct()]
            request.session["models"]=models
        res={"models": models}
        res.update(csrf(request))

        return render(request,"main.html",res)
    if request.method=="POST":
        id = request.POST["id"]
        table = request.POST["table"]
        models = request.session.get("models", None)
        res=fetchChanges(id,table)
        res["models"]=models
        return render(request,"main.html",res)
def get(lst,index,default):
    if index<len(lst): return lst[index]
    return default
def findChanges(old_state,new_state):
    res="<ul>"
    if type(old_state)==type({}):
        for key in old_state:
            if old_state[key]!=new_state.get(key,None):
                if type(old_state[key]) in [type({}),type([])]:
                    res+= "<li>"+findChanges(old_state.get(key,{}),new_state.get(key,{}))+"</li>"
                else:
                    res+="<li>%s:: %s ----> %s</li>"%(key,old_state.get(key,None),new_state.get(key,None))
    elif type(old_state)==type([]):
        for key in range(len(old_state)):
            if old_state[key] != get(new_state,key,None):
                if type(old_state[key]) in [type({}), type([])]:
                    res += findChanges(old_state[key], new_state[key])
                else:
                    res += "<li>%s:: %s ----> %s</li>" % (key, old_state[key], get(new_state,key,None))
    return res+"</ul>"
def fetchChanges(id,table):
    changes = History.objects.filter(primary_key=id, table=table).order_by("-id")
    rows = []
    for change in changes:
        row = {}
        row["event_time"] = change.done_on
        row["by"] = change.done_by
        row["changes"] = []
        row["name"]=change.name
        row["id"]=change.id
        for key in change.new_state.keys():
            if type(change.new_state[key]) ==type({}) and change.new_state[key].get("_type",None)!=None:

                if change.new_state[key]["_type"]=="datetime":
                    try:
                        change.new_state[key]=datetime.datetime.strptime(change.new_state[key]["value"],"%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%dT%H:%M:%SZ")
                    except ValueError as exp:
                        change.new_state[key]=datetime.datetime.strptime(change.new_state[key]["value"],"%Y-%m-%d").strftime("%Y-%m-%d")
                elif change.new_state[key]["_type"]=="date":
                    change.new_state[key]=datetime.datetime.strptime(change.new_state[key]["value"],"%Y-%m-%d").date().strftime("%Y-%m-%d")
            if change.old_state.get(key, None) != change.new_state.get(key, None):
                if type(change.old_state.get(key, None)) in [type({}), type([])]:
                    text = "%s: <br/>" % key
                    keyChanges = findChanges(change.old_state[key], change.new_state[key])
                    text += keyChanges
                    row["changes"].append(mark_safe(text))
                else:
                    row["changes"].append(
                        "%s: %s ----> %s" % (key, change.old_state.get(key, None), change.new_state[key]))
        rows.append(row)
    count = len(rows)
    res = {"count": count, "changes": rows, "id": id, "selected_model": table}
    return res

def getChanges(request):
    id = request.GET["id"]
    table = request.GET["table"]
    res=fetchChanges(id,table)
    return HttpResponse(simplejson.dumps(res))
