from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks


input_location = 'https://modelscope.oss-cn-beijing.aliyuncs.com/test/images/image_safetyhat.jpg'
data = {}
model_id = 'damo/cv_tinynas_object-detection_damoyolo_safety-helmet'
safety_hat_detection = pipeline(Tasks.domain_specific_object_detection, model=model_id)
result = safety_hat_detection(input_location)
data["scores"] = result['scores'].tolist()
data["labels"] = result['labels']
data["boxes"] = result['boxes'].tolist()
print("result is : ", data)
