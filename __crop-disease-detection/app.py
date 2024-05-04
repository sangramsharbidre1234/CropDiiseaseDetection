from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import getpass
import os

from pyngrok import ngrok, conf

from utils import  cottonmodel, sugarcanemodel, tomatomodel, get_model_details

app = Flask(__name__)


# Open a ngrok tunnel to the HTTP server
public_url = ngrok.connect(5000).public_url
print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}/\"".format(public_url, 5000))

# Update any base URLs to use the public ngrok URL
app.config["BASE_URL"] = public_url



# Define the upload folder
UPLOAD_FOLDER = 'static/uploaded_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Function to check if a file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the home page
@app.route('/')
def home():
    model_data = get_model_details()
    return render_template('index.html', model_data=model_data)


# /cropmodel/?modelname=tomatomodel
# /cropmodel/?modelname=sugarcanemodel
# /cropmodel/?modelname=cottonmodel

@app.route('/cropmodel/')
def cropmodel():
    # Check if the request is a GET request
    if request.method == 'GET':
        # Get the modelname argument from the request
        modelname = request.args.get('modelname')

        # Print the modelname on the terminal if available
        if modelname:
            # model_LIST = ['cottonmodel', 'sugarcanemodel', 'tomatomodel']

            # print(f"Model Name: {modelname}")
            __model_data = get_model_details()
            model_data = __model_data[modelname]


            # Render the template with the result
            return render_template('modelresult.html', modelname=modelname, model_data=model_data)
        
        else:
            msg = "Model Name not provided in the request."
            return render_template('modelresult.html', msg=msg)

    # Render a template for non-GET requests
    return render_template('nongetresult.html')



# Route to handle file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':

        if 'file' not in request.files:
            return redirect(request.url)
        
        modelname = request.form.get('modelname')

        
        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            # Rename the file to "imageFile.jpeg"
            filename = 'imageFile.jpeg'
            
            # Save the file to the upload folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


            defalut_image_path = 'static/uploaded_images/imageFile.jpeg'

            __model_data = get_model_details()
            model_data = __model_data[str(modelname)]

            if modelname == 'cottonmodel':
                result = cottonmodel(defalut_image_path)

            elif modelname == 'sugarcanemodel':
                result = sugarcanemodel(defalut_image_path)
            
            elif modelname == 'tomatomodel':
                result = tomatomodel(defalut_image_path)
            
            else:
                result = 'None'
                model_data = 'None'
            
            # print("modelname : ", modelname)
            # print("model_data : ", model_data)
            print("--- result : ", result)
            # Render the template with the result
            return render_template('modelresult.html', modelname=modelname, result=result, model_data=model_data)
            
            # return redirect(url_for('view_file', filename=filename))
        else:
            return "Invalid file type. Allowed extensions are: png, jpg, jpeg"
    
    return redirect(url_for('cropmodel'))


        
# Route to view the uploaded file
# @app.route('/view/<filename>')
# def view_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    # Ensure the upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    # app.run(debug=True)

    # for Docker
    # app.run(debug=True, host="0.0.0.0", port=5000)
    app.run(port=5000, use_reloader=False)

