# MayaMCP — VSCode to Maya 2026 Scripting Workflow

用 **VSCode** 撰寫 Python 腳本，透過 TCP Socket 即時傳送並在 **Maya 2026** 中執行。

---

## 工作原理

```
VSCode 編輯 .py 腳本
        ↓
run_maya_script_from_vsc.py（TCP Socket）
        ↓
localhost:7001（Maya commandPort）
        ↓
Maya 2026 執行腳本
```

---

## 環境需求

- Autodesk Maya 2026
- Python 3.x（Maya 內建）
- VSCode（任意版本）

---

## 使用步驟

### Step 1：開啟 Maya，啟動通訊埠

每次開啟 Maya 後，必須先執行一次 `VSCmayaPort.py` 來開啟 port 7001。

1. 開啟 **Maya 2026**
2. 在頂部選單點選 **Windows → General Editors → Script Editor**
3. 在 Script Editor 中，切換到 **Python** 標籤
4. 將 `Script_maya/VSCmayaPort.py` 的內容貼入，然後按 **執行（Ctrl+Enter）**
5. 看到以下訊息代表成功：

```
--- 設定完成！通訊埠 :7001 已在 MEL 模式下成功開啟。Maya 已準備就緒。 ---
```

> **注意：** 只要 Maya 沒有關閉，此步驟只需執行一次。重開 Maya 後需再次執行。

---

### Step 2：在 VSCode 設定要執行的腳本路徑

開啟 `run_maya_script_from_vsc.py`，修改第 7 行的 `SCRIPT_PATH`，指向你想執行的 Python 腳本：

```python
# 修改這裡，指向你想在 Maya 中執行的腳本
SCRIPT_PATH = r"i:\code_jenq\VSC_Maya\vscmayatest.py"
```

---

### Step 3：從 VSCode 執行腳本，傳送至 Maya

在 VSCode 的終端機（Terminal）中執行：

```bash
python run_maya_script_from_vsc.py
```

執行成功後會看到：

```
Attempting to connect to Maya (Port: 7001)...
Connection successful!
Reading script: 'i:\code_jenq\VSC_Maya\vscmayatest.py'
Sending script to Maya for execution...
--- Script execution complete ---
```

Maya 視窗中會同步出現執行結果。

---

## 腳本說明

| 檔案 | 用途 |
|------|------|
| `Script_maya/VSCmayaPort.py` | 在 Maya 內開啟 port 7001，每次啟動 Maya 必須先執行 |
| `run_maya_script_from_vsc.py` | VSCode 端的傳送工具，修改 `SCRIPT_PATH` 指向目標腳本後執行 |
| `vscmayatest.py` | 連線測試腳本，確認 VSCode → Maya 通道是否正常 |

---

## 常見問題

**Q: 執行後出現 `Connection refused`？**  
A: Maya 的 port 7001 尚未開啟。請回到 Step 1，在 Maya Script Editor 重新執行 `VSCmayaPort.py`。

**Q: Maya 沒有反應但 VSCode 顯示成功？**  
A: 檢查 `SCRIPT_PATH` 是否指向正確的檔案路徑，且檔案內容語法無誤。

**Q: 重開 Maya 後又失效？**  
A: 每次重新開啟 Maya 都必須重新執行 Step 1。可將 `VSCmayaPort.py` 的內容存入 Maya 的 **userSetup.py** 來自動化這個步驟。

---

## 自動化 Port 開啟（進階）

將以下內容加入 Maya 的 `userSetup.py`（路徑通常在 `Documents/maya/2026/scripts/userSetup.py`），讓 Maya 每次啟動時自動開啟 port：

```python
import maya.cmds as cmds
import maya.utils as utils

def open_command_port():
    if not cmds.commandPort(':7001', query=True):
        cmds.commandPort(name=':7001', sourceType='mel', echoOutput=True)
        print("Maya commandPort :7001 opened.")

utils.executeDeferred(open_command_port)
```
