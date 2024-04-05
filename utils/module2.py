import mediapipe as mp
from utils.first import calculateAngle,mp_pose

def classifySitPose(landmarks):
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
    
    
    if (left_torso_angle > 70 and left_leg_angle > 160 and left_hand_angle > 160) or \
       (right_torso_angle > 70 and right_leg_angle > 160 and right_hand_angle > 160 ) or \
       (right_torso_angle > 70 and left_torso_angle > 70 and right_leg_angle > 160 and left_leg_angle > 160 and right_hand_angle > 160 and left_hand_angle > 160):
        label = 'Sitting pose'
        return label
    return label


def classifyChildPose(landmarks):
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
    
    right_upper_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]) 
    
    left_upper_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]) 
    
       
    
    if (left_torso_angle < 50  and left_leg_angle < 50 and left_hand_angle > 160 and left_hand_angle<220 and left_upper_angle > 160) or \
       (right_torso_angle < 50  and right_leg_angle < 50 and right_hand_angle > 160 and right_hand_angle<220 and right_upper_angle > 160) or \
       (right_torso_angle < 50 and left_torso_angle < 50 and right_leg_angle < 50 and left_leg_angle < 50 and right_upper_angle > 160 and left_upper_angle > 160 and left_hand_angle<220 and right_hand_angle<220 and right_hand_angle > 160 and left_hand_angle > 160):
        label = 'Child pose'
        
        return label
    return label
    

def classifyPlankPose(landmarks):
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
    return label
 

