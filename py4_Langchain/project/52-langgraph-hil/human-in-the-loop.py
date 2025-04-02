"""
 * @author: zkyuan
 * @date: 2025/4/2 22:33
 * @description: 人机交互：在图中中断，让人去输入一些指令去操作.
 伪代码
"""
from typing import TypedDict, Literal, Annotated


class State(TypedDict):
    input: Annotated[list,str]

from langgraph.types import interrupt, Command


def human_node(state:State):
    value = interrupt(
        #任何可序列化为JSON 的值，供人类查看。
        # #例如，一个问题、一段文本或状态中的一组键
        {
            "text to revise":state["some text"]
         }
    )
    #使用人类的输入更新状态或根据输入调整图形，
    return {"some_text":value}
    graph = graph_builder.compile(checkpointer=checkpointer)  #interrupt工作所需
    #运行图形直到遇到中断
    thread_config={"configurable":{"thread id":"some id"}}
    graph.invoke(some_input,config=thread_config)
    #用人类的输入恢复图形
    graph.invoke(Command(resume=value_from_human),config=thread_config)


def human_approval(state: State)-> Command[Literal["some node", "another node"]]:
    is_approved = interrupt(
        {
            "question":"这是正确的吗?",
            #展示应由人类审查和批准的输出。
            "llm_output":state["llm_output"]
        }
    )
    if is_approved:
        return Command(goto="some node")
    else:
        return Command(goto="another node")
    #将节点添加到图形中的适当位置并连接到相关节点。
    graph_builder.add_node("human approval",human_approval)
    graph = graph_builder.compile(checkpointer=checkpointer)
    #在运行图形并触发中断后，图形将暂停。
    #用批准或拒绝恢复。
    thread_config ={"configurable":{"thread id": "some id"}}
    graph.invoke(Command(resume=True),config=thread_config)

    graph.invoke(inputs, config=config)
    graph.invoke(None, config=config)
