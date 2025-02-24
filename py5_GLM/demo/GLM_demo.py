"""
 * @author: zkyuan
 * @date: 2025/2/23 21:15
 * @description: 智普GLM大模型
"""
import os

from langchain_core.output_parsers import StrOutputParser
from zhipuai import ZhipuAI

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "zhipu"
os.environ["LANGCHAIN_API_KEY"] = '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'

model = ZhipuAI(api_key=os.getenv("ZHIPU_API_KEY"))

result = model.chat.completions.create(
    model="glm-4-plus",
    messages=[{'role': "user", 'content': '用C语言写一个冒泡排序的函数', }]
)
print(result) # Completion(model='glm-4-plus', created=1740326223, choices=[CompletionChoice(index=0, finish_reason='stop', message=CompletionMessage(content='当然可以。下面是一个使用C语言编写的冒泡排序函数的实现。这个函数将对一个整型数组进行排序，按照从小到大的顺序排列数组中的元素。\n\n```c\n#include <stdio.h>\n\n// 冒泡排序函数\nvoid bubbleSort(int arr[], int n) {\n    int i, j, temp;\n    for (i = 0; i < n-1; i++) {\n        // 最后i个元素已经是排好序的了\n        for (j = 0; j < n-i-1; j++) {\n            if (arr[j] > arr[j+1]) {\n                // 交换arr[j]和arr[j+1]\n                temp = arr[j];\n                arr[j] = arr[j+1];\n                arr[j+1] = temp;\n            }\n        }\n    }\n}\n\n// 打印数组函数\nvoid printArray(int arr[], int size) {\n    for (int i = 0; i < size; i++) {\n        printf("%d ", arr[i]);\n    }\n    printf("\\n");\n}\n\n// 主函数，用于测试冒泡排序函数\nint main() {\n    int arr[] = {64, 34, 25, 12, 22, 11, 90};\n    int n = sizeof(arr)/sizeof(arr[0]);\n    \n    printf("Original array: \\n");\n    printArray(arr, n);\n    \n    bubbleSort(arr, n);\n    \n    printf("Sorted array: \\n");\n    printArray(arr, n);\n    \n    return 0;\n}\n```\n\n这段代码首先定义了`bubbleSort`函数，它接受一个整型数组和数组的大小作为参数。然后，通过两层嵌套循环实现了冒泡排序算法。在每一轮的内部循环中，相邻的元素会被比较，如果它们的顺序错误（即左边的元素大于右边的元素），就会交换它们的位置。\n\n`printArray`函数用于打印数组中的元素，方便我们验证排序结果。\n\n`main`函数则是用来测试`bubbleSort`函数的，它初始化了一个未排序的数组，调用`bubbleSort`对其进行排序，并打印排序前后的数组。', role='assistant', tool_calls=None))], request_id='20250223235652ce8bf1b7bb6347c8', id='20250223235652ce8bf1b7bb6347c8', usage=CompletionUsage(prompt_tokens=15, completion_tokens=452, total_tokens=467))

# 解析结果
print(result.choices[0].message.content)
"""
```c
#include <stdio.h>

// 冒泡排序函数
void bubbleSort(int arr[], int n) {
    int i, j, temp;
    for (i = 0; i < n-1; i++) {
        // 最后i个元素已经是排好序的了
        for (j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                // 交换arr[j]和arr[j+1]
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

// 打印数组函数
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// 主函数，用于测试冒泡排序函数
int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr)/sizeof(arr[0]);
    
    printf("Original array: \n");
    printArray(arr, n);
    
    bubbleSort(arr, n);
    
    printf("Sorted array: \n");
    printArray(arr, n);
    
    return 0;
}
```

这段代码首先定义了`bubbleSort`函数，它接受一个整型数组和数组的大小作为参数。然后，通过两层嵌套循环实现了冒泡排序算法。在每一轮的内部循环中，相邻的元素会被比较，如果它们的顺序错误（即左边的元素大于右边的元素），就会交换它们的位置。

`printArray`函数用于打印数组中的元素，方便我们验证排序结果。

`main`函数则是用来测试`bubbleSort`函数的，它初始化了一个未排序的数组，调用`bubbleSort`对其进行排序，并打印排序前后的数组。
"""

