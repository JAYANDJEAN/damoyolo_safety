from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

model_id = 'damo/cv_tinynas_object-detection_damoyolo_safety-helmet'
input_location = '/Users/yuan.feng/Downloads/IMG_3753.jpg'

safety_hat_detection = pipeline(Tasks.domain_specific_object_detection, model=model_id)
result = safety_hat_detection(input_location)
print("result is : ", result)
