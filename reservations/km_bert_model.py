import numpy as np
import tensorflow as tf
from transformers import BertTokenizer, TFBertModel

# 모델과 토크나이저 로드
model_name = 'madatnlp/km-bert'
tokenizer = BertTokenizer.from_pretrained(model_name)

# 모델 구조 정의
class TFBertClassifier(tf.keras.Model):
    def __init__(self, model_name, num_class):
        super(TFBertClassifier, self).__init__()
        self.bert = TFBertModel.from_pretrained(model_name)
        self.dropout = tf.keras.layers.Dropout(self.bert.config.hidden_dropout_prob)
        self.classifier = tf.keras.layers.Dense(num_class, kernel_initializer=tf.keras.initializers.TruncatedNormal(self.bert.config.initializer_range), name="classifier")

    def call(self, inputs, attention_mask=None, token_type_ids=None, training=False):
        outputs = self.bert(inputs, attention_mask=attention_mask, token_type_ids=token_type_ids)
        pooled_output = outputs[1]
        pooled_output = self.dropout(pooled_output, training=training)
        logits = self.classifier(pooled_output)
        return logits

# 학습된 모델 가중치 로드
num_classes = 20  # 실제 클래스 수에 맞게 설정
model = TFBertClassifier(model_name=model_name, num_class=num_classes)

MAX_LEN = 20

# 모델을 먼저 호출하여 변수들을 생성
dummy_input_ids = np.zeros((1, MAX_LEN), dtype=int)
dummy_attention_mask = np.zeros((1, MAX_LEN), dtype=int)
dummy_token_type_ids = np.zeros((1, MAX_LEN), dtype=int)
model((dummy_input_ids, dummy_attention_mask, dummy_token_type_ids))

# 그 후에 가중치를 로드
model.load_weights('reservations/model/weights.h5')

def bert_tokenizer(sentence, max_len):
    inputs = tokenizer.encode_plus(
        sentence,
        None,
        add_special_tokens=True,
        max_length=max_len,
        padding='max_length',
        truncation=True,
        return_token_type_ids=True
    )
    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask']
    token_type_ids = inputs['token_type_ids']
    return input_ids, attention_mask, token_type_ids

def specialty_predict(new_sentence):
    input_id, attention_mask, token_type_id = bert_tokenizer(new_sentence, MAX_LEN)

    new_symptom_input_id = np.array([input_id], dtype=int)  # Add batch dimension
    new_symptom_attention_mask = np.array([attention_mask], dtype=int)  # Add batch dimension
    new_symptom_type_id = np.array([token_type_id], dtype=int)  # Add batch dimension
    new_symptom_input = (new_symptom_input_id, new_symptom_attention_mask, new_symptom_type_id)

    result = model(new_symptom_input, training=False)  # Do not use model.predict.
    output_prob = tf.nn.softmax(result, axis=1)  # To show the probability of the label(class)

    top_3_indices = tf.argsort(output_prob, direction='DESCENDING')[0][:3].numpy()
    top_3_probs = tf.gather(output_prob, top_3_indices, axis=1).numpy()[0]

    top_3_classes = [label_to_class.get(index) for index in top_3_indices]

    recommended_departments = ", ".join(top_3_classes)
    return recommended_departments, top_3_probs

# 예시로 클래스 라벨을 정의합니다.
# 실제 환경에서는 모델이 학습된 라벨을 사용합니다.
label_to_class = {0: '내분비대사내과',
 1: '감염내과',
 2: '소화기내과',
 3: '알레르기내과',
 4: '정형외과',
 5: '성형외과',
 6: '외과',
 7: '심장혈관흉부외과',
 8: '소아청소년과',
 9: '산부인과',
 10: '영상의학과',
 11: '신경과',
 12: '류마티스내과',
 13: '진단검사의학과',
 14: '정신건강의학과',
 15: '치과',
 16: '안과',
 17: '피부과',
 18: '이비인후과',
 19: '가정의학과'}