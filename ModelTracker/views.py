from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.template import Context, RequestContext
from django.core.context_processors import csrf
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

        return render_to_response("main.html",res,context_instance = RequestContext(request))
    if request.method=="POST":
        id = request.POST["id"]
        table = request.POST["table"]
        models = request.session.get("models", None)
        res=fetchChanges(id,table)
        res["models"]=models
        return render_to_response("main.html",res,context_instance = RequestContext(request))

def findChanges(old_state,new_state):
    res="<ul>"
    if type(old_state)==type({}):
        for key in old_state:
            if old_state[key]!=new_state.get(key,None):
                if type(old_state[key]) in [type({}),type([])]:
                    res+= "<li>"+findChanges(old_state[key],new_state[key])+"</li>"
                else:
                    res+="<li>%s:: %s ----> %s</li>"%(key,old_state[key],new_state[key])
    elif type(old_state)==type([]):
        for key in range(len(old_state)):
            if old_state[key] != new_state[key]:
                if type(old_state[key]) in [type({}), type([])]:
                    res += findChanges(old_state[key], new_state[key])
                else:
                    res += "<li>%s:: %s ----> %s</li>" % (key, old_state[key], new_state[key])
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
