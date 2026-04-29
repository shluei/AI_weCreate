import os
import sys
from core.engine import AutoFixEngine
import config

def main(target_file):
    if not os.path.exists(target_file):
        print(f"Error: File {target_file} not found.")
        return

    engine = AutoFixEngine(config.API_KEY, config.MODEL_NAME)
    
    print(f"[*] 开始自动化修复任务: {target_file}")
    
    for i in range(3):  # 最多尝试3次
        print(f"\n--- 迭代轮次 {i+1} ---")
        
        success, output = engine.run_tests(target_file)
        if success:
            print("✅ 恭喜！代码通过了所有测试。")
            break
            
        print("❌ 发现错误，正在生成修复方案...")
        with open(target_file, "r") as f:
            current_code = f.read()
            
        # 修复逻辑
        fixed_code = engine.fix_code(current_code, output)
        
        # 审核逻辑
        print("[*] 正在进行代码二轮审计...")
        final_code = engine.review_code(fixed_code)
        
        # 应用修复
        with open(target_file, "w") as f:
            f.write(final_code)
        print("[*] 修复方案已应用，准备重新测试...")
    else:
        print("\n⚠️ 达到最大尝试次数，修复未完全成功。")

if __name__ == "__main__":
    # 默认修复 samples/buggy_code.py
    sample_path = os.path.join("samples", "buggy_code.py")
    main(sample_path)
