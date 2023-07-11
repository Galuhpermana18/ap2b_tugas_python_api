from ast import Param
from inspect import Parameter
from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)
book_data = {"data": [{"nama": "Galuh Permana", "Kelas": "1IA15"},
                      {"nama": "Anya Geraldine", "Kelas": "1IA22"}]}


@app.route('/hello/', methods=['GET'])
def welcome():
    return "Hello World"


@app.route('/mahasiswa', methods=["GET"])
def GET_mahasiswa():

    return jsonify(book_data)


@app.route('/mahasiswa', methods=['PUT'])
def PUT_mahasiswa():
    record = request.json
    index = None

    for i, data in enumerate(book_data['data']):
        if data['Kelas'] == record['Kelas']:
            index = i
            break

    if index is not None:
        book_data['data'][index] = record
        return_message = {"error": False, "Message": "Data berhasil diupdate"}
    else:
        return_message = {"error": True, "Message": "Data tidak ditemukan"}

    return jsonify(return_message)


@app.route('/mahasiswa', methods=["post"])
def POST_mahasiswa():
    record = json.loads(request.data)

    book_data["data"].append(record)

    print(record)

    return_message = {"error": False, "Message": "Data Berhasil Di Tambah"}

    return jsonify(return_message)


@app.route('/mahasiswa', methods=["DELETE"])
def DEL_mahasiswa():
    record = request.json
    if record in book_data["data"]:
        book_data["data"].remove(record)
        return_message = {"error": False, "Message": "Data berhasil dihapus"}
    else:
        return_message = {"error": True, "Message": "Data tidak ditemukan"}
    return jsonify(return_message)


@app.route('/kampus', methods=["GET"])
def GET_kampus():
    response = requests.get(
        "http://universities.hipolabs.com/search?country=indonesia")

    return response.json()


@app.route("/mahasiswa-param", methods=["GET"])
def GET_mahasiswa_with_param():
    get_param = request.args
    name = get_param.get('name')

    return jsonify({"value": name})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
