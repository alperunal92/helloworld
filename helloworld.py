# ------------------------------------------------
# Maintainer by Alper Unal
#
#
# Version      Date       
# 1.0          23.01.2019
#
# ----------------------------------------------
from flask import Flask
import os

helloworld = Flask(__name__)

@helloworld.route("/")
def hello():
    return "Hello World !!"

#--------Main------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    helloworld.run(debug=True,host='0.0.0.0',port=port)
#------------------------------
