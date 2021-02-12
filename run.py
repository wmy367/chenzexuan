# -*- coding: utf-8 -*-

import json
import time
import os 
import sys 
import flask
import matplotlib.pyplot as plt


path    = os.path.split(os.path.realpath(__file__))[0]
app_root_path = path

image_path = os.path.join(app_root_path,'./tmp')

def create_app(test_config=None):
    # create and configure the app
    # app = flask.Flask(__name__, instance_relative_config=True)
    app = flask.Flask(__name__,static_folder="./dist",template_folder="./dist",static_url_path='')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # os.makedirs(app.instance_path)

    # a simple page that says hello
    @app.route('/')
    def hello():
        global IN_FLOW
        # return 'DATA SERVER:: IN_FLOW[[%s]]'%IN_FLOW
        return flask.render_template("index.html")

    ## 静态文件
    filedirpath = os.path.join(app.root_path,'tmp')

    @app.route("/file/<path:filename>")
    def downloader(filename):
        return flask.send_from_directory(filedirpath,filename,as_attachment=True)

    

    return app


if __name__ == '__main__':
    # t0 = udp_status.UDPSTatusThread(callback=get_all_data_from_fpga)
    # t0.start()
    create_app().run(host='0.0.0.0',port=1314,debug=True)
    # t0.join(timeout=1)

    # get_all_data_from_fpga_verb_core("Bti")
