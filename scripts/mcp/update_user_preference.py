# ~/AI_Workspace/my_mcp_servers/preference_server.py
from mcp.server.fastmcp import FastMCP
import os
from datetime import datetime

# 创建一个 MCP Server 实例
mcp = FastMCP("PreferenceManager")

# 只需要加一个装饰器，这个函数就会被自动转换为 LLM 可见的 Tool
@mcp.tool()
def update_global_preference(category: str, new_preference: str) -> str:
    """
    当用户表达了关于自身的长期特征、个人画像（Persona）或全局偏好时，必须调用此工具进行持久化记录。
    
    捕获范围不仅限于编程习惯，还必须包含以下维度的信息：
    1. 沟通风格：如喜欢简洁直接、需要详细解释原理、特定语气要求等。
    2. 背景与状态：如当前职业角色、生活作息、重要人生节点或计划。
    3. 兴趣与领域：如对特定技术（如AI Agent开发）、金融投资（美股/期权）、特定游戏等长期的关注点。
    4. 工作流与技术栈：如特定的代码规范、工具偏好等。
    
    请忽略一次性的中短期任务要求。
    参数 category 应当简明扼要，例如: 'Communication', 'Interests', 'TechStack', 'Background', 'Workflow'。
    """
    file_path = os.path.expanduser("~/God/USER.md")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"\n- **[{category}]** {new_preference} (Updated: {timestamp})"
    
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(entry)
        
    return "SUCCESS: Preference updated."

if __name__ == "__main__":
    mcp.run()
