FROM python:3.7.9

COPY . /ocr

WORKDIR /ocr

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN apt-get update
RUN apt-get install -y tesseract-ocr
RUN apt-get install -y libtesseract-dev
RUN apt-get install 'ffmpeg' 'libsm6' 'libxext6'  -y
COPY /trainnedpytesseract /usr/share/tesseract-ocr/4.00/tessdata
#RUN pip install torch==0.4.1.post2
RUN apt-get install libmagickwand-dev -y
RUN apt-get install cmake -y
RUN rm -rf imgtxtenh/
RUN git clone https://github.com/mauvilsa/imgtxtenh

WORKDIR /ocr/imgtxtenh

RUN dpkg --configure -a 
RUN cmake CMakeLists.txt -DCMAKE_BUILD_TYPE=Release && make 
RUN chmod +x ./imgtxtenh 

WORKDIR /ocr
ENTRYPOINT ["python3"]

CMD ["app_heroku.py"]


