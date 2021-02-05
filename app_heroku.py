# import os
# from flask import Flask, jsonify, request
# from flask_restful import reqparse, abort, Api, Resource
# from flask_cors import CORS, cross_origin
# import urllib.request
from ocr_pipeline import process
from firebase import Firebase
from google.cloud import storage
import os
import subprocess
from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS, cross_origin
import urllib.request
import requests
import asyncio
import file_utils
app = Flask(__name__)
api = Api(app)
CORS(app)
# test
# test
# test
# test
# test
# test
config = {
  "apiKey": "AIzaSyA1DQpPRfs9XxFc1RAOrRXY2Dn7o_iTiIQ",
  "authDomain": "fir-ocr-ec83a.firebaseapp.com",
  "databaseURL": "https://fir-ocr-ec83a.firebaseio.com",
  "storageBucket": "fir-ocr-ec83a.appspot.com"
}
firebase = Firebase(config)
def uploadFB(path):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./fir-ocr-ec83a-587caeefbbec.json"
    
    imagePath = "./ocrproc_pre_newimage.jpg"
    obj = firebase.storage().child(path).put(imagePath)
    return obj['name']
def urlprocess(url):
    name = url
    # print(name.find("%2F"));
    path = name[name.find("%2F")+3:]
    path =path[:path.find("%2F")]
    # print(path)
    tokens = name[name.find("token=")+6:]

    # auth = firebase.auth()
    # tokens = auth.sign_in_with_email_and_password("lebathanh1812@gmail.com","Teo361812")
    # tokens = auth.refresh(tokens['refreshToken'])

    # print(tokens)
    # print (name)
    firebasepath = "images/" + "{}".format(path)+"/{}.jpg".format(path)
    # print(firebasepath)
    storage = firebase.storage()
    # print(storage.child(firebasepath).get_url(tokens))
    storage.child(firebasepath).download("newimage.jpg")
    # hardcode xd
    # img_path = "./newimage.jpg"
    # pre_img_path = 'pre_' + os.path.basename(img_path) # pre_0.jpg
    # command = './imgtxtenh/imgtxtenh ' + ' -p ' + os.path.basename(img_path) + " " + os.path.basename(pre_img_path)# ../../imgtxtenh/imgtxtenh 0.jpg -p pre_0.jpg
    # p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    uploadpath = "images/"+ "{}".format(path) + "/ocr.jpg"
    global ocrpath
    ocrpath = uploadpath



class rnImg(Resource):
    @cross_origin()
    def post(self):
        # url =  request.form.get('url')
        url =  request.get_json()
        if(url):
            urlprocess(url['url'])
        return jsonify({'message': 'ok'})

    @cross_origin()
    def options(self):
        pass   
        

# test
# test
# test
# test
# test
# test
def createImg(imgUrl):
    urllib.request.urlretrieve(imgUrl, "newimage.jpg")
    # print(imgUrl)
    # pushLatLng()

def bufferProcess():
    point = process('./newimage.jpg',1)

    return point
class HelloWorld(Resource):
    @cross_origin()
    def get(self):
        lat, lng = bufferProcess()
        path = uploadFB(ocrpath)
        path = path[:path.find("/ocr.jpg")]
        # path = "abcasd.asd./asdas/dasd"

        # lat = 11.193712907467816 
        # lng = 106.5878921136777
        point = {}
        point['lat'] = lat
        point['lng'] = lng
        point['ocr'] = path
        # print(lat, lng)
        return jsonify(point)

    @cross_origin()
    def post(self):
        res = request.data.decode('utf-8')
        # print(res)
        createImg(res)
        return jsonify({'message': 'ok'})

    @cross_origin()
    def options(self):
        pass

api.add_resource(HelloWorld, '/api', endpoint='api')
api.add_resource(rnImg,'/img',endpoint='img')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5111))
    app.run(host = '0.0.0.0', port = port)
    # app.run(host = '192.168.1.112', port = port)
