from flask import Flask , render_template,request

app=Flask(__name__)

datas=[]
@app.route("/" , methods=["GET" ,"POST"])
def Home():
    if request.method=="POST":
       Title_entry=request.form.get("title")
       print(Title_entry)
       Amount_entry=int(request.form.get("amount")or "0")
       print(Amount_entry)
       Category_entry=request.form.get("category")
       print(Category_entry)  
       datas.append((Title_entry,Amount_entry,Category_entry))
       print(datas)

    kwargs={
          "datas":datas
       } 


    return render_template("index.html", **kwargs)