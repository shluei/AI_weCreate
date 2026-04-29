def get_division(a, b):
    # 故意留下的 Bug: 没有处理除以 0 的情况
    return a / b

def test_logic():
    print("正在运行测试...")
    assert get_division(10, 2) == 5
    assert get_division(10, 0) == 0  # 这里会触发 ZeroDivisionError
    print("测试通过！")

if __name__ == "__main__":
    test_logic()
