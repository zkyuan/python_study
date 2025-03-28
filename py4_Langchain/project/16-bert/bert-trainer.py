# 1：环境准备
# pip install torch transformers datasets scikit-learn
# 可以自定义huggingface模型下载的位置
# setx HF_HOME “D:\huggingface“  默认位置C:\Users\HP\.cache\huggingface
from transformers import BertTokenizer, BertForSequenceClassification

# 2：加载中文 BERT 预训练模型
# 加载 分词器和 bert 中文预训练模型
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
model = BertForSequenceClassification.from_pretrained('bert-base-chinese', num_labels=3)

# 3：加载 ChnSentiCorp 数据集并进行清洗
from datasets import load_dataset

# 加载 ChnSentiCorp 数据集
# 数据集地址：https://huggingface.co/datasets/lansinuote/ChnSentiCorp
dataset = load_dataset('lansinuote/ChnSentiCorp')

import re


# 定义数据清洗函数
def clean_text(text):
    # 去除标点符号
    text = re.sub(r'[^\w\s]', '', text)
    # 去除前后空格
    text = text.strip()
    return text


# 对数据集中的文本进行清洗
dataset = dataset.map(lambda x: {'text': clean_text(x['text'])})


# 4：数据预处理
def tokenize_function(examples):
    return tokenizer(examples['text'], padding='max_length', truncation=True, max_length=128)


# 对数据集进行分词和编码
encoded_dataset = dataset.map(tokenize_function, batched=True)

# 5：训练模型
from transformers import Trainer, TrainingArguments

# 定义训练参数
# 定义训练参数，创建一个TrainingArguments对象
training_args = TrainingArguments(
    # 指定训练输出的目录，用于保存模型和其他输出文件
    output_dir='./results',
    # 设置训练的轮数
    num_train_epochs=1,
    # 每个设备（如GPU）上的训练批次大小
    per_device_train_batch_size=1,
    # 每个设备上的评估批次大小
    per_device_eval_batch_size=1,
    # 设置评估策略为每个epoch结束后进行评估
    evaluation_strategy="epoch",
    # 指定日志保存的目录
    logging_dir="./logs",
)

print("---------------开始训练---------------")
# 使用 Trainer 进行训练 ,Trainer 是一个简单但功能齐全的 PyTorch 训练和评估循环
trainer = Trainer(
    model=model,
    args=training_args,
    # 训练集
    train_dataset=encoded_dataset['train'],
    # 评估集
    eval_dataset=encoded_dataset['validation'],
)

# 开始训练
trainer.train()

# 步骤 6：评估模型性能
from sklearn.metrics import accuracy_score


# 定义评估函数
def compute_metrics(p):
    # p.predictions 是模型对输入数据的预测输出，
    preds = p.predictions.argmax(-1)  # argmax(-1) 的作用是沿着最后一个维度（通常是类别维度）取最大值对应的索引，即模型预测的类别
    # p.label_ids 是真实的标签。
    return {"accuracy": accuracy_score(p.label_ids, preds)}


# 在测试集上评估模型 自动调用compute_metrics
trainer.evaluate(encoded_dataset['test'], metric_key_prefix="eval")

"""{'eval_loss': 0.2, 'eval_accuracy': 0.85}
# eval_loss: 0.2：这是模型在测试集上的损失值。
# 损失值是一个衡量模型预测与实际标签之间差异的指标。
# 较低的损失值通常表示模型的预测更接近于真实标签。
# eval_accuracy: 0.85：这是模型在测试集上的准确率。
# 准确率是指模型正确预测的样本数量占总样本数量的比例。
# 在这个例子中，准确率为 0.85，意味着模型在测试集上有 85% 的样本被正确分类。
"""
# 7：导出模型
# 保存模型和分词器
model.save_pretrained('./sentiment_model')
tokenizer.save_pretrained('./sentiment_model')
