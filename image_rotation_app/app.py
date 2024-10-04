from flask import Flask,render_template,request
from PIL import Image
import os

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/route",methods=["POST"])
def rotation():

    angle=int(request.form["angle"])
    
    file=request.files["image"]
    img=Image.open(file)
    rotated_img=img.rotate(angle)

    file_name=f"rotated_image_{angle}.png"
    file_path=os.path.join(r"C:\Users\meteh\OneDrive\Masaüstü\deusAI3\output",file_name)
    rotated_img.save(file_path,format="PNG")


    return render_template("succes.html")


if __name__=="__main__":
    app.run(debug=True)

