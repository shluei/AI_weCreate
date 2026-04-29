# AI Auto-Fix Agent

这是一个基于多智能体协作的代码自愈系统原型。

## 项目结构
- `main.py`: 项目入口
- `config.py`: 配置文件（需填写 API Key）
- `core/`: 核心逻辑文件夹
- `samples/`: 演示用的 Bug 代码

## 使用说明
1. 安装依赖：`pip install -r requirements.txt`
2. 在 `config.py` 中填写您的 API Key。
3. 运行主程序：`python main.py`

Agent 会自动运行 `samples/buggy_code.py`，发现错误并尝试修复。
