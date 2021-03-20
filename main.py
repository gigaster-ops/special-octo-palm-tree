from flask import Flask, render_template, url_for, redirect, request, make_response, jsonify, json
import secrets
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/')
def hello_world():
    return render_template('main.html')


@app.route('/nst')
def style_transfer():
    return render_template('nst.html')


@app.route('/nst2')
def style_transfer2():
    return render_template('nst2.html')


@app.route('/gen')
def gen_img():
    return render_template('gen.html')


def get_names(n):
    a = []
    for i in range(n):
        a.append(secrets.token_hex(10))
    return a


@app.route('/ajax_parameters', methods=['POST'])
def ajax_():
    print(request.form)
    print(request.files)
    weight_style2 = 0
    file3 = 0
    weight_style = request.form['weight_style']
    if 'weight_style2' in request.form:
        weight_style2 = request.form['weight_style2']
    weight_content = request.form['weight_content']
    num_epoch = request.form['num_epoch']

    name1, name2, name3 = get_names(3)

    file1 = request.files['file1']
    file2 = request.files['file2']
    if 'file3' in request.files:
        file3 = request.files['file3']

    two = weight_style2 != 0 and file3 != 0
    file1.save(f'{name1}.jpg')
    file2.save(f'{name2}.jpg')
    if two:
        file3.save(f'{name3}.jpg')

    return json.dumps({'src': url_for('static', filename=f'{name1}.jpg')})


@app.route('/generate', methods=['POST'])
def generate():
    print('generate!')
    return json.dumps({'src1': url_for('static', filename=f'images/im1.jpg'),
                       'src2': url_for('static', filename=f'images/im1.jpg'),
                       'src3': url_for('static', filename=f'images/im1.jpg'),
                       'src4': url_for('static', filename=f'images/im1.jpg'),
                       'src5': url_for('static', filename=f'images/im1.jpg'),
                       'src6': url_for('static', filename=f'images/im1.jpg'),
                       'src7': url_for('static', filename=f'images/im1.jpg'),
                       'src8': url_for('static', filename=f'images/im1.jpg'),
                       'src9': url_for('static', filename=f'images/im1.jpg'),
                       'src10': url_for('static', filename=f'images/im1.jpg'),
                       'src11': url_for('static', filename=f'images/im1.jpg'),
                       'src12': url_for('static', filename=f'images/im1.jpg'),
                       'src13': url_for('static', filename=f'images/im1.jpg'),
                       'src14': url_for('static', filename=f'images/im1.jpg'),
                       'src15': url_for('static', filename=f'images/im1.jpg'),
                       'src16': url_for('static', filename=f'images/im1.jpg'),})


if __name__ == '__main__':
    app.run(debug=True)
