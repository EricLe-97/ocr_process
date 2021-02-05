# AI-Repos/Backend OCR
Mọi người clone về và xóa folder imgtxtenh đi

Sau đó clone từ https://github.com/mauvilsa/imgtxtenh về

*if use mac*

```
brew install imagemagick@6
brew link imagemagick@6 --force
```

Khởi động **redis**, sau đó chạy các lệnh:

1. `cd imgtxtenh`
2. `cmake -DCMAKE_BUILD_TYPE=Release`
3. `make`
4. `cd ..`
5. `sudo docker-compose up -d`

API sẽ được tạo ra ở `localhost:5000/api`

*localhost:5000/api(GET)*

1. nhận request và thực hiện: improve ảnh, xử lý ảnh sang text và trả toạ độ kèm link trên Firebase cho Frontend

*localhost:5000/img(POST)*

`Param: uri của hình ảnh trên firebase`

1. nhận request và thực hiện lưu hình ảnh từ firebase về local.


*Chạy lệnh copy toàn bộ file trainned data vào TESSDATA_PREFIX để chạy được code mới*



`(MACOS) cp ./trainnedpytesseract/*.traineddata /usr/local/Cellar/tesseract/4.1.1/share/tessdata`
`(LINUX)cp ./trainnedpytesseract/*.traineddata /usr/share/tesseract-ocr/4.00/tessdata`
Lưu ý: đổi `4.1.1` thành version Pytesseract tương ứng với máy của mình. Check version bằng lệnh `tesseract --version`