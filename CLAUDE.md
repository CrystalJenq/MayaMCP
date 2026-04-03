# Project: MayaMCP — VSCode to Maya 2026

## Maya Stubs 位置

maya-stubs 0.4.2 放在：

```
I:\code_jenq\VSC_Maya\maya_stubs-0.4.2\maya_stubs-0.4.2\
```

實際的 `.pyi` stub 檔案在：

```
I:\code_jenq\VSC_Maya\maya_stubs-0.4.2\maya_stubs-0.4.2\src\maya-stubs\
```

包含 `cmds`、`mel`、`OpenMaya` 等模組的型別定義。

## VSCode 設定提示

若要讓 VSCode IntelliSense 使用這些 stubs，在 `.vscode/settings.json` 加入：

```json
{
  "python.analysis.extraPaths": [
    "I:\\code_jenq\\VSC_Maya\\maya_stubs-0.4.2\\maya_stubs-0.4.2\\src"
  ]
}
```

## 核心檔案

- `Script_maya/VSCmayaPort.py` — 在 Maya Script Editor 執行，開啟 port 7001
- `run_maya_script_from_vsc.py` — VSCode 端傳送腳本至 Maya（修改 `SCRIPT_PATH` 後執行）
- `vscmayatest.py` — 連線測試腳本
