from flask import Flask , render_template,request
import database
app=Flask(__name__)

# datas=[]
database.create_expenses_table()
@app.route("/" , methods=["GET" ,"POST"])
def Home():
    if request.method=="POST":
       Title_entry=request.form.get("title")

    #    print(Title_entry)

       Amount_entry=int(request.form.get("amount")or "0")
    #    print(Amount_entry)

       Category_entry=request.form.get("category")
    #    print(Category_entry)  

       database.store_expenses(Title_entry, Amount_entry ,Category_entry) 

       #   datas.append((Title_entry,Amount_entry,Category_entry))
       #   print(datas)

    expenses=database.extract_expenses_data()      

    kwargs={
          "datas":expenses
       } 


    return render_template("index.html", **kwargs)