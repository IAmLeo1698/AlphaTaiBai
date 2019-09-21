from flask import Flask
from flask import request
import json
from run_bert_chinese_inference import *

app = Flask(__name__)

@app.route('/api/emb/v1', methods = ['POST'])
def emb():
    sents = request.json
    features = convert_sents_to_features(sents, 64)
    dataset = convert_features_dataset(features)
    res = inference_batch(dataset, 64)
    # use the [CLS] Token
    res = res.numpy()
    res = res[:,0].tolist()
    return json.dumps(res)

if __name__ == "__main__":
    app.run()
