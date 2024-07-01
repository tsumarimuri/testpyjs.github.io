from flask import Flask,send_file,render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/clicked',methods=["GET"])
def clicked():
    return send_file("./testfile.docx", 
                 mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                 as_attachment=False, 
                 download_name="test.docx")

     

if __name__ == '__main__':
    app.run(debug=True,port=5001)

