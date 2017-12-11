from app import app
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import os

def selected_server():
    selected = request.get_json()
    selected = selected.get('selected')
    selected = selected.get('server')
    print(selected)
    f = open('infrastructure', 'w')
    f.write('[controller-comments]' + '\n')
    for select in selected:
        f.write(select + '\n')
    f.write('[controller-comments:vars]' + '\n')
    f.write('ansible_become_pass=ltytuytlfv24')
    f.close()

def selected_service():
    services = request.get_json()
    services = services.get('services')
    services = services.get('service')
    print(services)
    f = open('/home/rizhikov_v/test_flask/ansible_server_task/roles/service_manager/vars/main.yml', 'w')
    f.write('services:' + '\n')
    for select in services:
        f.write("  - '" + select + "'" +'\n')
    f.close()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/startRedis', methods=['GET','POST'])
def startRedis():
    selected_server()
    os.system('ansible-playbook /home/rizhikov_v/test_flask/ansible_server_task/main.yml -i /home/rizhikov_v/test_flask/infrastructure --tags=start_redis')
    return render_template('index.html')

@app.route('/stopRedis', methods=['GET','POST'])
def stopRedis():
    selected_server()
    os.system('ansible-playbook /home/rizhikov_v/test_flask/ansible_server_task/main.yml -i /home/rizhikov_v/test_flask/infrastructure --tags=stop_redis')
    return render_template('index.html')

@app.route('/restartRedis', methods=['GET','POST'])
def restartRedis():
    selected_server()
    os.system('ansible-playbook /home/rizhikov_v/test_flask/ansible_server_task/main.yml -i /home/rizhikov_v/test_flask/infrastructure --tags=restart_redis')
    return render_template('index.html')


@app.route('/startRMQ', methods=['GET','POST'])
def startRMQ():
    selected_server()
    os.system('ansible-playbook /home/rizhikov_v/test_flask/ansible_server_task/main.yml -i /home/rizhikov_v/test_flask/infrastructure --tags=start_rabbit')
    return render_template('index.html')

@app.route('/stopRMQ', methods=['GET','POST'])
def stopRMQ():
    selected_server()
    os.system('ansible-playbook /home/rizhikov_v/test_flask/ansible_server_task/main.yml -i /home/rizhikov_v/test_flask/infrastructure --tags=stop_rabbit')
    return render_template('index.html')

@app.route('/restartRMQ', methods=['GET','POST'])
def restartRMQ():
    selected_server()
    os.system('ansible-playbook /home/rizhikov_v/test_flask/ansible_server_task/main.yml -i /home/rizhikov_v/test_flask/infrastructure --tags=restart_rabbit')
    return render_template('index.html')


@app.route('/startSVS', methods=['GET','POST'])
def startSVS():
    selected_server()
    selected_service()
    os.system('ansible-playbook /home/rizhikov_v/test_flask/ansible_server_task/main.yml -i /home/rizhikov_v/test_flask/infrastructure --tags=start_service')
    return render_template('index.html')

@app.route('/stopSVS', methods=['GET','POST'])
def stopSVS():
    selected_server()
    selected_service()
    os.system('ansible-playbook /home/rizhikov_v/test_flask/ansible_server_task/main.yml -i /home/rizhikov_v/test_flask/infrastructure --tags=stop_service')
    return render_template('index.html')

@app.route('/restartSVS', methods=['GET','POST'])
def restartSVS():
    selected_server()
    selected_service()
    os.system('ansible-playbook /home/rizhikov_v/test_flask/ansible_server_task/main.yml -i /home/rizhikov_v/test_flask/infrastructure --tags=restart_service')
    return render_template('index.html')

