import mediapipe as mp
from utils.first import calculateAngle,mp_pose

def classifyTPose(landmarks):
    
    label = 'Wrong pose'
    
    
    right_armpit_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]) 
    
    right_hand_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]) 
    left_hand_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]) 
    
    left_armpit_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]) 
    
    right_leg_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value])
    
    left_leg_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value])
    
    left_t_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value])
   
    right_t_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_HIP.value])
   
    
    if left_armpit_angle > 75 and left_leg_angle > 170 and left_t_angle < 100 and right_t_angle< 100 and right_leg_angle>170 and right_armpit_angle > 75 and right_hand_angle>150 and left_hand_angle>150 and right_armpit_angle<120 and left_armpit_angle<120 :
        label = 'T Pose'
        
        return label

    return label


def classifyTreePose(landmarks):
    
    label = 'Wrong pose'
    
    left_leg_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_HIP.value])
    right_leg_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value])
    
   
    right_armpit_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]) 
    
    left_armpit_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]) 
    
    if left_leg_angle > 200 and  ( right_leg_angle > 160 and right_leg_angle <200 )  and right_armpit_angle > 150 and left_armpit_angle > 150:
            label = 'Tree Pose'
            
            return label
        
    
    return label
