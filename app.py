import os
# gradio와 langchain_openai 기능을 이 코드에 불러왔어요.
import gradio as gr
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://mlapi.run/e55afb4c-afa7-4b64-b80f-937f9000573e/v1",
    api_key=os.getenv("OPENAI_API_KEY"), 
    model="helpy-pro",
    # 1. 하이퍼파라미터 설정하기
  
)

# 2. 시스템 프롬프트 설정하기
role = "너는 친절하고 도움을 주는 AI 비서야."

# ------------------------------------------------------
# 챗봇에서 보내기 버튼을 클릭하면 실행될 동작을 정의해요.
def function(message, history):
    # 대화 내용이 저장될 memory예요. 처음에는 시스템 프롬프트를 저장해요.
    memory = role + "\n"

    # history에는 사용자 메시지와 AI 메시지가 자동으로 저장돼요.
    # 반복 탐색하며 각 사용자 메시지를 user에, AI 메시지를 ai에 저장해요.
    for user, ai in history:
        # user와 ai가 비어있지 않다면
        if user and ai:
            # memory에 user와 ai를 구분하여 저장해요.
            memory += ("사용자:" + user + "\n")
            memory += ("AI:" + ai + "\n")
    
    # message에는 최근 내가 입력한 질문이 적혀있어요. 이것도 memory에 추가해요.
    memory += ("사용자:" + message + "\n")
    # 대화 내용을 AI에게 전달하고 AIMessage 객체를 저장해요.
    response = llm.invoke(memory)
    # 저장된 AIMessage에서 content(AI응답)만 반환해요.
    return response.content
    
# -------------------------------------------------------
# 챗봇 객체를 생성해요.
demo = gr.ChatInterface(
    fn=function,
    # 3. title, theme 등 속성 설정하기
    title="제목없음",
    theme=gr.themes.Soft(),
    description="설명없음"
)

# 챗봇 객체를 실행해요.
demo.launch(share=True)
