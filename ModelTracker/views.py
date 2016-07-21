from django.shortcuts import render_to_response, render
from django.template import Context, RequestContext
from django.core.context_processors import csrf
from models import *
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
        models = request.session.get("models", None)
        id=request.POST["id"]
        table=request.POST["table"]
        print id,table
        changes=History.objects.filter(primary_key=id,table=table).order_by("-id")
        print changes.count()
        rows=[]
        for change in changes:
            row={}
            row["datetime"]=change.done_on
            row["by"]=change.done_by
            row["changes"]=[]
            for key in change.old_state.keys():
                if change.old_state[key]!=change.new_state.get(key,None):
                    row["changes"].append("%s: %s ----> %s"%(key,change.old_state[key],change.new_state[key]))
            rows.append(row)
        count=len(rows)
        res={"count":count,"changes":rows,"models":models,"id":id,"selected_model":table}
        return render_to_response("main.html",res,context_instance = RequestContext(request))
