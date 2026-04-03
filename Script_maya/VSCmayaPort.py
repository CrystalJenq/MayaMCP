import maya.cmds as cmds

PORT_NAME = ':7001'

# 步驟 1: 確保任何可能存在的舊通訊埠都被徹底關閉，以提供一個乾淨的環境
if cmds.commandPort(PORT_NAME, query=True):
    print(f"偵測到正在運行的通訊埠 {PORT_NAME}，正在重設...")
    try:
        # 修正：關閉時必須明確使用 'name' 關鍵字
        cmds.commandPort(name=PORT_NAME, close=True)
        print("通訊埠已成功關閉。")
    except RuntimeError as e:
        print(f"嘗試關閉通訊埠時發生錯誤: {e}")


# 步驟 2: 以 Python 模式開啟通訊埠
try:
    # 再次檢查以確保通訊埠已關閉
    if not cmds.commandPort(PORT_NAME, query=True):
        print(f"正在以 Python 模式開啟通訊埠 {PORT_NAME}...")
        cmds.commandPort(name=PORT_NAME, sourceType='python', echoOutput=True)
        print(f"--- 設定完成！通訊埠 {PORT_NAME} 已在 Python 模式下成功開啟。Maya 已準備就緒。 ---")
    else:
        print(f"通訊埠 {PORT_NAME} 仍然在運行，這不符合預期。請重新啟動 Maya 再試一次。")
except RuntimeError as e:
    print(f"開啟通訊埠時發生錯誤。它可能仍被另一個程式佔用。原始錯誤: {e}")

