from crewai import Task,Crew,Agent
from pydantic import BaseModel,Field
import os
#定义一个 研究员
researcher=Agent(
    role="Ai 行业分析师",
    goal="精准总结指定领域的最新趋势",
    backstory="你是一位资深的科技记者，擅长噪音中提取信号，拒绝泛泛而谈",
    varbose=True #看agent 思考链
)
#定义一个具体的任务

task=Task(
    description="调研2026年ai agent在跨境电商领域的三个落地案例，每个案例包含，痛点，解决方案，效果数据",
    expected_output="Markdown 格式的表格，包含案例名称，痛点，方案，效果四列",
    agent=researcher

)

class caseStudy(BaseModel):
    title:str=Field(description="案例标题")
    summary:str=Field(description="摘要，10个字内")
    name:str=Field(description="案例及公司名称")
    pain_point:str=Field(description="核心痛点，不超过20个字")
    solution:str=Field(description="Agent 解决方案")
    metric:str=Field(description="量化效果:如效率提升50%")

task2=Task(
    description="调研2026年ai agent在跨境电商领域的三个落地案例，每个案例包含，痛点，解决方案，效果数据",
    expected_output="Markdown 格式的表格，包含案例名称，痛点，方案，效果四列",
    agent=researcher,
    output_pydantic=caseStudy
)

def main():
    print("Hello from first-crew!")
    crew=Crew(tracing=True,agents=[researcher],tasks=[task2])
    result=crew.kickoff()
    print(result)
    with open('./README.md', 'a', encoding='utf-8') as f:
       f.writelines(result)

if __name__ == "__main__":
    main()
