import mediapipe as mp
from utils.first import calculateAngle,mp_pose

def classify_Surya_One(landmarks):
    label = 'Wrong pose'
    
    left_leg_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_HIP.value])
    right_leg_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value])
    
    left_torso_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value]) 
    
    right_torso_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                       landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                       landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value]) 
   
    
    left_hand_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]) 
    
    right_hand_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]) 
    
   
    if (left_torso_angle >  160  and left_leg_angle > 160 and left_hand_angle < 50) or \
       (right_torso_angle > 160  and right_leg_angle > 160 and right_hand_angle < 50 ) or \
       (right_torso_angle > 160 and left_torso_angle > 160 and right_leg_angle > 160 and left_leg_angle > 160 and right_hand_angle <50 and left_hand_angle < 50):
        label = 'Pranam Pose'
        
    
    return label

def classify_Surya_Two(landmarks):
    label = 'Wrong pose'
    
    left_leg_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_HIP.value])
    right_leg_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value])
    
    left_torso_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value]) 
    
    right_torso_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                       landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                       landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value]) 
    
    
    
    left_hand_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]) 
    
    right_hand_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]) 
    
   
    if (left_torso_angle >  180 and left_torso_angle < 250   and left_leg_angle > 160 and left_hand_angle > 160) or \
       (right_torso_angle > 180 and right_torso_angle < 250 and right_leg_angle > 160 and right_hand_angle > 160 ) or \
       (left_torso_angle >  180 and left_torso_angle < 250 and right_torso_angle < 250 and left_leg_angle > 160 and left_hand_angle > 160 and right_torso_angle > 180  and right_leg_angle > 160 and right_hand_angle > 160):
        label = 'Hastha Uttanasana Pose'
        
        
    
    return label

def classify_Surya_Three(landmarks):
    label = 'Wrong pose'
    
    left_leg_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_HIP.value])
    right_leg_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value])
    
    left_torso_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value]) 
    
    right_torso_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                       landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                       landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value]) 
    
    
    
    left_hand_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]) 
    
    right_hand_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]) 
    
    
        
    if (left_torso_angle < 95 and left_torso_angle > 20   and left_leg_angle > 180 and left_leg_angle < 190 and left_hand_angle > 160 ) or \
       (right_torso_angle < 95 and right_torso_angle > 20 and right_leg_angle > 180 and right_leg_angle < 190 and right_hand_angle > 160 ) or \
       (left_torso_angle < 95 and left_torso_angle > 20 and right_torso_angle < 95 and right_torso_angle > 20 and left_leg_angle < 190 and left_leg_angle > 180 and left_hand_angle > 160  and right_leg_angle > 180 and right_leg_angle < 190 and right_hand_angle > 160):
        label = 'Paada Hastha Pose'
        
    return label

def classify_Surya_Four(landmarks):
    label = 'Wrong pose'
    
    left_leg_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_HIP.value])
    right_leg_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value])
    
    left_torso_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value]) 
    
    right_torso_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                       landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                       landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value]) 
    
  
    
    left_hand_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]) 
    
    right_hand_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]) 
   
    if (left_torso_angle < 50 and left_torso_angle > 0   and left_leg_angle > 50 and left_leg_angle < 80 and left_hand_angle > 160 ) or \
       (right_torso_angle < 190 and right_torso_angle > 140 and right_leg_angle > 110 and right_leg_angle < 160 and right_hand_angle > 160 ) or \
       (left_torso_angle < 30 and left_torso_angle > 0 and right_torso_angle < 190 and right_torso_angle > 170 and left_leg_angle < 80 and left_leg_angle > 85 and left_hand_angle > 160  and right_leg_angle > 150 and right_leg_angle < 180 and right_hand_angle > 160):
        label = 'Ashwa Sanchalan Asana'
        
    
    return label

def classify_Surya_Five(landmarks):
    label = 'Wrong pose'
    

    
    right_leg_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value])
    
    left_leg_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value])
    
    left_torso_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value]) 
    
    right_torso_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value]) 
    
    left_hand_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]) 
    
    right_hand_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]) 
    
    right_armpit_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]) 
     
    left_armpit_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]) 
    
   
    if (left_torso_angle > 170 and left_leg_angle > 160 and left_hand_angle>160 and left_armpit_angle > 60 ) or ( right_torso_angle>170 and right_leg_angle>160 and right_hand_angle>160 and right_armpit_angle>60):
        label = 'Plank pose'
        
    return label

def classify_Surya_Six(landmarks):
    label = 'Wrong pose'
    
    left_leg_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_HIP.value])
    right_leg_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value])
    
    left_torso_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value]) 
    
    right_torso_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                       landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                       landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value]) 
    
   
    
    left_hand_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]) 
    
    right_hand_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]) 
   
   
     
    if (left_torso_angle < 140 and left_torso_angle > 100   and left_leg_angle > 110 and left_leg_angle < 130 and left_hand_angle > 20 ) or \
       (right_torso_angle < 130 and right_torso_angle > 100 and right_leg_angle > 100 and right_leg_angle < 130 and right_hand_angle > 20 ) or \
       (left_torso_angle < 140 and left_torso_angle > 100  and right_torso_angle < 130 and right_torso_angle > 10 and left_leg_angle > 110 and left_leg_angle < 130 and left_hand_angle > 20  and right_leg_angle > 100 and right_leg_angle < 130 and right_hand_angle > 20):
        label = 'Ashtanga Namaskar'
        color = (0, 255, 0)  # Green color
        
    return label

def classify_Surya_Seven(landmarks):
    label = 'Wrong pose'
    
    left_leg_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_HIP.value])
    right_leg_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value])
    
    left_torso_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value]) 
    
    right_torso_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                       landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                       landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value]) 
    
    
    left_hand_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]) 
    
    right_hand_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]) 
  
   
     
    if (left_torso_angle < 260 and left_torso_angle > 215   and left_leg_angle > 150 and left_leg_angle < 170 and left_hand_angle > 130 ) or \
       (right_torso_angle < 265 and right_torso_angle > 200 and right_leg_angle > 140 and right_leg_angle < 180 and right_hand_angle > 130 ) or \
       (left_torso_angle < 260 and left_torso_angle > 215  and right_torso_angle < 265 and right_torso_angle > 200 and left_leg_angle > 150 and left_leg_angle < 170 and left_hand_angle > 130  and right_leg_angle > 140 and right_leg_angle < 180 and right_hand_angle > 130):
        label = 'Bhujangasana'
        
    
    return label
