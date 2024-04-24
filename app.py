import cv2
from flask import Flask, render_template, Response, request, jsonify
import time
import boto3
import mediapipe as mp
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import matplotlib.pyplot as plt
import numpy as np


from utils.first import calculateAngle, mp_pose, pose, mp_drawing, detectPose


app = Flask(__name__)


from utils.Surya import (classify_Surya_One, classify_Surya_Two, classify_Surya_Three,
                         classify_Surya_Four, classify_Surya_Five, classify_Surya_Six, classify_Surya_Seven)

from utils.module2 import (classifyChildPose, classifySitPose, classifyPlankPose)

from utils.Others import (classifyTPose,classifyTreePose)


global all_poses
all_poses = {"classify_Surya_One":classify_Surya_One,
             "classify_Surya_Two": classify_Surya_Two, 
             "classify_Surya_Three":classify_Surya_Three, 
             "classify_Surya_Five":classify_Surya_Five, 
             "classify_Surya_Six": classify_Surya_Six, 
             "classify_Surya_Seven":classify_Surya_Seven,
             "classify_Surya_Four":classify_Surya_Four,
             "classifyChildPose":classifyChildPose, 
             "classifySitPose":classifySitPose,
             "classifyPlankPose": classifyPlankPose,
             "classifyTPose":classifyTPose,
             "classifyTreePose":classifyTreePose}

global render_image
render_image ='/static/images/Ready.png'
global render_text
render_text='Current pose will be displayed here'
global render_timer 
render_timer = "Pending: 0 seconds"
global render_poses
render_poses=[]


def generate_frames_surya():
    poses = [classify_Surya_One, classify_Surya_Two, classify_Surya_Three,
                         classify_Surya_Four, classify_Surya_Five, classify_Surya_Six, classify_Surya_Seven]
    camera = cv2.VideoCapture(0)
    for curr_pose in poses:
      
        start_time = time.time()
        
        pose_duration = 50 
        while time.time() - start_time < pose_duration:
            success, frame = camera.read()
          
            if not success:
                break
            else:
                results = detectPose(frame, pose)
                if results.pose_landmarks:
                    mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                    landmarks = []
                    for landmark in results.pose_landmarks.landmark:
                        landmarks.append((int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0]), landmark.z))
                    label = curr_pose(landmarks)
                    cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0) if label == 'Wrong pose' else (0, 255, 0), 2)
                    global render_image
                    render_image=f'/static/images/{curr_pose.__name__}.png'
                    global render_text
                    render_text=f'Status: Current Pose is {label}'
                    global render_timer
                    # Calculate remaining seconds and format as "Pending Seconds: X seconds"
                    remaining_seconds = max(0, int(pose_duration - (time.time() - start_time)))
                    render_timer = f'Pending Seconds: {remaining_seconds} seconds'
                   
                      
                        
                        
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                
      
          
      
    render_image='/static/images/Done.png'            


@app.route('/post-exercises', methods=['POST'])
def post_exercises():
    selected_exercises = request.json  
    global all_poses
    res=[]
    for i in selected_exercises:
        
        res.append(all_poses[(i.split('DeleteUpDown')[0])])
        
    global render_poses    
    render_poses= res

def generate_frames_second():
    poses = [classifySitPose,classifyChildPose,classifyPlankPose]
    camera = cv2.VideoCapture(0)
    for curr_pose in poses:
        
        start_time = time.time()
        
        pose_duration = 50 
        while time.time() - start_time < pose_duration:
            success, frame = camera.read()
          
            if not success:
                break
            else:
                results = detectPose(frame, pose)
                if results.pose_landmarks:
                    mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                    landmarks = []
                    for landmark in results.pose_landmarks.landmark:
                        landmarks.append((int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0]), landmark.z))
                    label = curr_pose(landmarks)
                    cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0) if label == 'Wrong pose' else (0, 255, 0), 2)
                    global render_image
                    render_image=f'/static/images/{curr_pose.__name__}.png'
                    global render_text
                    render_text=f'Status: Current Pose is {label}'
                    global render_timer
                    # Calculate remaining seconds and format as "Pending Seconds: X seconds"
                    remaining_seconds = max(0, int(pose_duration - (time.time() - start_time)))
                    render_timer = f'Pending Seconds: {remaining_seconds} seconds'
                        
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
  
    render_image='/static/images/Done.png'            


global email_information
email_information = {
    "module_name":"module_name",
    "set_of_excercises":[],
    "session_duration":0,
    "accuracy":[],
    
}

# Modify the generate_pie_chart function to accept accuracy_data
def generate_pie_chart(accuracy_data):
    exercises = [f'Exercise {i+1}' for i in range(len(accuracy_data))]
    plt.pie(accuracy_data, labels=exercises, autopct='%1.1f%%')
    plt.title('Accuracy of Exercises')
    plt.axis('equal')
    plt.savefig('static/images/pie_chart.png')  # Save the pie chart image
    plt.close()

# Modify the generate_bar_graph function to accept accuracy_data
def generate_bar_graph(accuracy_data):
    exercises = [f'Exercise {i+1}' for i in range(len(accuracy_data))]
    plt.bar(exercises, accuracy_data)
    plt.xlabel('Exercises')
    plt.ylabel('Accuracy (%)')
    plt.title('Accuracy of Exercises')
    plt.savefig('static/images/bar_graph.png')  # Save the bar graph image
    plt.close()

def generate_frames_custom():
   
    camera = cv2.VideoCapture(0)
    global email_information
    email_information["module_name"]="custom module"
    
    for curr_pose in render_poses:
        start_time = time.time()
        email_information["set_of_excercises"].append(curr_pose.__name__)
        email_information["session_duration"]+=50
        total_count=0
        correct_count=0
        pose_duration = 50 
        while time.time() - start_time < pose_duration:
            success, frame = camera.read()

            if not success:
                break
            else:
                total_count+=1
                results = detectPose(frame, pose)
                if results.pose_landmarks:
                    mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                    landmarks = []
                    for landmark in results.pose_landmarks.landmark:
                        landmarks.append((int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0]), landmark.z))
                    label = curr_pose(landmarks)
                    cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0) if label == 'Wrong pose' else (0, 255, 0), 2)
                    if label != 'Wrong pose':
                        correct_count += 1
                    global render_image
                    render_image=f'/static/images/{curr_pose.__name__}.png'
                    global render_text
                    render_text=f'Status: Current Pose is {label}'
                    global render_timer
                    # Calculate remaining seconds and format as "Pending Seconds: X seconds"
                    remaining_seconds = max(0, int(pose_duration - (time.time() - start_time)))
                    render_timer = f'Pending Seconds: {remaining_seconds} seconds'

                        
                ret, buffer = cv2.imencode('.jpg', frame)
                
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
        email_information['accuracy'].append((correct_count/total_count)*100)
    render_image='/static/images/Done.png'            


@app.route('/submit-contact-details', methods=['GET'])
def submit_contact_details():
    email = request.args.get('emailOrPhone')
    
    # Setup email details
    sender_email = 'proconnect522@gmail.com'  # Your Gmail address
    sender_password = 'swie gaic lzwt ojfc'  # Your Gmail password
    recipient_email = email
    subject = 'Subject of the Email'
    # Construct the HTML content for the email body
    # Generate pie chart and bar graph
    # Generate pie chart and bar graph using accuracy data
    generate_pie_chart(email_information['accuracy'])
    generate_bar_graph(email_information['accuracy'])
    message_body = f"""
    <html>
    <head>
    <style>
        /* Define CSS styles for better presentation */
        body {{
            font-family: Arial, sans-serif;
            color: #333;
        }}
        .highlighted {{
            color: red;
            font-weight: bold;
        }}
    </style>
    </head>
    <body>
    <h2>Session Information:</h2>
    <p><span class="highlighted">Module Name:</span> {email_information['module_name']}</p>
    <p><span class="highlighted">Session Duration:</span> {email_information['session_duration']} seconds</p>
    <p><span class="highlighted">Set of Exercises:</span></p>
    <ul>
        {"".join(f"<li>{exercise}</li>" for exercise in email_information['set_of_excercises'])}
    </ul>
    <p><span class="highlighted">Accuracy:</span></p>
    <ul>
        {"".join(f"<li>{accuracy}%</li>" for accuracy in email_information['accuracy'])}
    </ul>
   <!-- Example in contact.html -->
<img src="{{ url_for('static', filename='images/pie_chart.png') }}" alt="Pie Chart">
<img src="{{ url_for('static', filename='images/bar_graph.png') }}" alt="Bar Graph">


    </body>
    
    </html>
    """
    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message_body, 'html'))

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("Email sent successfully")
        
    except Exception as e:
        print(f"Failed to send email: {e}")

    return "Email sent successfully"


@app.route('/')
def index():
    return render_template('frontpage.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/working_second')
def working_second():
    return render_template('working_second.html')


@app.route('/custom')
def custom():
    return render_template('custom.html')

@app.route('/working')
def working():
    return render_template('practice.html')      

@app.route('/features')
def features():
    return render_template('modules.html')          





@app.route('/default_image')
def default_image():
    return render_image

@app.route('/default_text')
def default_text():
    return render_text


@app.route('/default_timer')
def default_time():
    return render_timer

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames_surya(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_second')
def video_feed_second():
  
    return Response(generate_frames_second(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_custom')
def video_feed_custom():
    return Response(generate_frames_custom(), mimetype='multipart/x-mixed-replace; boundary=frame')






if __name__ == "__main__":
    app.run(debug=True, port=8000)















