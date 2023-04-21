import flask
from PIL import Image
import io
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

app = flask.Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}
    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            image = flask.request.files["image"].read()
            image = Image.open(io.BytesIO(image))
            model_id = 'damo/cv_tinynas_object-detection_damoyolo_safety-helmet'
            safety_hat_detection = pipeline(Tasks.domain_specific_object_detection, model=model_id)
            result = safety_hat_detection(image)
            data["scores"] = result['scores'].tolist()
            data["labels"] = result['labels']
            data["boxes"] = result['boxes'].tolist()
            data["success"] = True
    return flask.jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
