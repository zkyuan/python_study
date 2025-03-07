from transformers import AdamW
from transformers.optimization import get_scheduler
import torch
from data import MyDataset
from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM, GPT2Model

dataset = MyDataset()

#加载编码器
tokenizer = AutoTokenizer.from_pretrained('uer/gpt2-chinese-cluecorpussmall')
#加载模型
model = AutoModelForCausalLM.from_pretrained(
    'uer/gpt2-chinese-cluecorpussmall')
def collate_fn(data):
    data = tokenizer.batch_encode_plus(data,
                                       padding=True,
                                       truncation=True,
                                       max_length=512,
                                       return_tensors='pt')

    data['labels'] = data['input_ids'].clone()

    return data


#数据加载器
loader = torch.utils.data.DataLoader(
    dataset=dataset,
    batch_size=4,
    collate_fn=collate_fn,
    shuffle=True,
    drop_last=True,
)
print(len(loader))
#训练
def train():
    global model
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = model.to(device)

    optimizer = AdamW(model.parameters(), lr=2e-5)
    scheduler = get_scheduler(name='linear',
                              num_warmup_steps=0,
                              num_training_steps=len(loader),
                              optimizer=optimizer)

    model.train()
    for i, data in enumerate(loader):
        for k in data.keys():
            data[k] = data[k].to(device)
        out = model(**data)
        loss = out['loss']

        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)

        optimizer.step()
        scheduler.step()

        optimizer.zero_grad()
        model.zero_grad()

        if i % 50 == 0:
            labels = data['labels'][:, 1:]
            out = out['logits'].argmax(dim=2)[:, :-1]

            select = labels != 0
            labels = labels[select]
            out = out[select]
            del select

            accuracy = (labels == out).sum().item() / labels.numel()

            lr = optimizer.state_dict()['param_groups'][0]['lr']

            print(i, loss.item(), lr, accuracy)
    #保存模型参数，未保存模型结构
    torch.save(model.state_dict(), 'net.pt')
    print("权重保存成功！")

if __name__ == '__main__':
    for epoch in range(1000):
        train()