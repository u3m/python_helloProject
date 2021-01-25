# https://blog.csdn.net/qq_19707521/article/details/105072362 高并发部署方案
# https://blog.csdn.net/qq_35622837/article/details/105652766?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control

from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'hello world'

# if __name__ == '__main__':
app.run(threaded=True, host='127.0.0.1', port=5000)