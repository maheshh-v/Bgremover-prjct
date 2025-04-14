from flask import Flask, render_template, request, send_from_directory
from rembg import remove
import os
from flask import send_from_directory

app = Flask(__name__)
app.config['toUPLOAD'] = 'uploads'
app.config['getSTATIC'] = 'static'


@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('static', filename)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        
        if 'image' not in request.files:
            return render_template('index.html', error='No image file selected.')

        file = request.files['image']
        if file.filename == '':
            return render_template('index.html', error='No image file selected.')

        try:
            image_path = os.path.join(app.config['toUPLOAD'], file.filename)
            file.save(image_path)

            
            output = remove(open(image_path, 'rb').read())

            
            result_path = os.path.join(app.config['getSTATIC'], 'result.png')
            with open(result_path, 'wb') as output_file:
                output_file.write(output)

            # Pass the  image path to the template
            return render_template('index.html', result_path=result_path)

        except Exception as e:
            return render_template('index.html', error='An error occurred: {}'.format(str(e)))

    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['toUPLOAD'], filename)

@app.route('/static/<filename>')
def static_file(filename):
    return send_from_directory(app.config['getSTATIC'], filename)

@app.route('/download/<filename>')
def download_result(filename):
    return send_from_directory(app.config['getSTATIC'], filename, as_attachment=True)


if __name__ == '__main__':
  app.run(debug=True)
