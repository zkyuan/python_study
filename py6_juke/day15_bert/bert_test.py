import torch
from MyData import Mydataset
from torch.utils.data import DataLoader
from net import Model
from transformers import AdamW,BertTokenizer

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

token = BertTokenizer.from_pretrained("bert-base-chinese")

def collate_fn(data):
    sentes = [i[0] for i in data]
    label = [i[1] for i in data]
    # print(sentes)
    #编码
    data = token.batch_encode_plus(batch_text_or_text_pairs=sentes,
                            truncation=True,
                            padding="max_length",
                            max_length=500,
                            return_tensors="pt",
                            return_length=True)
    input_ids = data["input_ids"]
    attention_mask = data["attention_mask"]
    token_type_ids = data["token_type_ids"]
    labels = torch.LongTensor(label)
    # print(input_ids,attention_mask,token_type_ids)
    return input_ids,attention_mask,token_type_ids,labels
#创建数据集
test_dataset = Mydataset("test")
#创建dataloader
test_laoder = DataLoader(dataset=test_dataset,
                          batch_size=32,
                          shuffle=True,
                          drop_last=True,
                          collate_fn=collate_fn)

if __name__ == '__main__':
    acc = 0
    total = 0
    #开始测试
    print(DEVICE)
    model = Model().to(DEVICE)
    model.load_state_dict(torch.load("params/2bert.pt"))
    model.eval()
    for i, (input_ids, attention_mask, token_type_ids, labels) in enumerate(test_laoder):
        input_ids, attention_mask, token_type_ids, labels = input_ids.to(DEVICE), attention_mask.to(
            DEVICE), token_type_ids.to(DEVICE), labels.to(DEVICE)
        out = model(input_ids, attention_mask, token_type_ids)

        out = out.argmax(dim=1)
        acc += (out == labels).sum().item()
        total+= len(labels)
    print(acc/total)
