import os
from flask import Flask,request,jsonify, render_template
from search import search_assessments,get_assessements_details

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")



@app.route("/results",methods = ["POST"])
def show_results():
    query = request.form.get("query")
    top_ids = search_assessments(query)
    results = get_assessements_details(top_ids)

    return render_template("results.html",query=query,results=results)


@app.route("/api/search",methods=["POST"])
def api_search():
    data = request.get_json()
    query = data.get("query")


    if not query:
        return jsonify({"Error":"Query required"})
    
    top_ids = search_assessments(query)
    results = get_assessements_details(top_ids)


    response = [
        {
            "name":r[1],
            "url":r[2],
            "remote_testing_support":"Yes" if r[3] else "No",
            "duration":r[4],
            "test_type":r[5],
            "adaptive_support":"Yes" if [6] else "No",
        }
        for r in results
    ]

    return  jsonify(response)


if __name__ == "__main__":
    #app.run(debug= True,port = 5001)  local port.
    port = int(os.environ.get('PORT',10000))
    app.run(host = '0.0.0.0',port = port)