# OpenCV 学习笔记

基于 Python + OpenCV 的入门实践代码集合。每个脚本对应一个独立的知识点，从环境测试、图像读写一路覆盖到形态学处理、滤波、边缘检测与视频运动目标检测。

## 项目结构

```
opencv/
├── LICENSE
├── README.md              # 中文说明（本文件）
├── README.en.md           # English description
└── OpenCV入门/            # 全部练习脚本
    ├── first.py           # 图像读取与显示
    ├── mouse.py           # 鼠标事件回调
    ├── TrackBar.py        # 滑动条控件
    ├── video_read.py      # 视频读取
    ├── video_write.py     # 视频写入
    ├── test.py            # 摄像头采集并保存
    ├── aftrer.py          # 绘图函数（线/椭圆/多边形/文字）
    ├── drewshape.py       # 鼠标交互式绘图
    ├── drewshape copy.py  # 绘图模式切换（线/圆）
    ├── thresh.py          # 六种阈值处理
    ├── blur.py            # 滤波与边缘检测
    ├── contours.py        # 轮廓查找与绘制
    ├── addlogo.py         # 图像水印（alpha 混合）
    └── car_count.py       # 车辆计数（运动目标检测）
```

## 环境要求

| 依赖 | 版本 |
|---|---|
| Python | 3.8+ |
| opencv-python | 4.x |
| numpy | 任意近期版本 |
| matplotlib | 仅 `car_count.py` 需要 |

```bash
pip install opencv-python numpy matplotlib
```

## 目录与知识点对照

| 脚本 | 知识点 | 核心 API |
|---|---|---|
| `first.py` | 图像读取、显示、按键交互、保存 | `imread` / `imshow` / `waitKey` / `imwrite` |
| `mouse.py` | 鼠标事件回调 | `setMouseCallback` |
| `TrackBar.py` | 滑动条控件，实时调参 | `createTrackbar` / `getTrackbarPos` |
| `video_read.py` | 视频文件读取与逐帧显示 | `VideoCapture` |
| `video_write.py` | 摄像头采集并录制为视频 | `VideoWriter` / `VideoWriter_fourcc` |
| `test.py` | 摄像头属性获取与视频保存 | `cap.get(3)` / `cap.get(4)` |
| `aftrer.py` | 基础绘图：直线、椭圆、多边形、文字 | `line` / `ellipse` / `polylines` / `putText` |
| `drewshape.py` | 鼠标拖拽实时绘制图形（含预览） | 事件回调 + ROI 局部还原 |
| `drewshape copy.py` | 绘图模式切换（按 L 画线 / C 画圆） | 全局状态 + 按键分支 |
| `thresh.py` | 六种阈值处理方式 | `threshold` + `THRESH_OTSU` |
| `blur.py` | 图像平滑滤波 + 边缘检测 | `blur` / `GaussianBlur` / `medianBlur` / `bilateralFilter` / `Sobel` / `Scharr` / `Laplacian` / `Canny` |
| `contours.py` | 轮廓查找与绘制 | `findContours` / `drawContours` |
| `addlogo.py` | 图像水印叠加、alpha 通道混合 | `multiply` / `add` / ROI 赋值 |
| `car_count.py` | 运动目标检测与车辆计数 | `createBackgroundSubtractorKNN` + 形态学 + 轮廓面积过滤 |

## 脚本说明

### 图像基础操作

**`first.py`** — 加载图片并以 `WINDOW_NORMAL` 模式显示，按 `q` 退出、按 `s` 保存为 `cat.png`，其他按键打印对应字符，用于熟悉键值交互的基本范式。

**`aftrer.py`** — 在空白画布上调用 `cv2.line` 绘制一条红色直线（`(0,0,255)`，线宽 5）。文件内以注释形式列出了 `ellipse()`、`polylines()`、`fillPoly()`、`putText()` 等绘图函数的用法提示。

### 交互控件

**`TrackBar.py`** — 创建 R / G / B 三个滑动条（范围 0–255）与一个 480×640 的黑色画布。滑动时通过 `getTrackbarPos` 读取数值并实时刷新画布颜色，是最直观的「参数调优」交互演示。

**`mouse.py`** — 注册鼠标回调函数，将每次事件（触发类型、坐标、标志位、用户数据）打印到控制台，用于理解 OpenCV 事件模型。

**`drewshape.py`** — 完整的鼠标绘图程序。左键按下确定起点、拖动时实时预览、松开完成绘制，支持直线与圆形两种模式。实现要点是拖动过程中借助临时图像做预览，避免残影。

**`drewshape copy.py`** — 精简版，保留鼠标回调与按键切换绘图模式（`l` 画线 / `c` 画圆）的骨架，便于对照理解状态管理。

### 视频处理

**`video_read.py`** — 从视频文件（默认 `103236.mp4`，可改为摄像头 `0`）逐帧读取并显示，按 `q` 退出、`s` 截取当前帧。

**`video_write.py`** — 从摄像头采集，使用 MJPG 编码与 24 FPS 录制到 `out.avi`。帧尺寸通过 `cap.get(3)` / `cap.get(4)` 动态获取，避免分辨率不匹配导致的写入失败。

**`test.py`** — 摄像头采集 + 视频写入的完整流程示范：读取属性 → 创建 `VideoWriter` → 循环取帧写入 → 释放资源。

### 图像处理

**`thresh.py`** — 演示六种阈值化方式：二值化、反向二值化、截断、阈值化为 0、反向阈值化为 0，以及大津算法（`THRESH_OTSU`，自动求取最佳阈值）。

**`blur.py`** — 滤波与边缘检测的综合练习，包含三部分：

| 类别 | 方法 |
|---|---|
| 平滑滤波 | 均值、高斯、中值、双边、方框、自定义卷积核（`filter2D`） |
| 一阶微分 | Sobel（x/y 方向）、Scharr |
| 二阶微分 / 边缘 | Laplacian、Canny |

> 注：中值滤波的核大小必须为奇数；双边滤波在保边的同时去噪，代价是速度较慢。

**`contours.py`** — 灰度化 → 大津法二值化 → `findContours` 查找轮廓（`RETR_LIST` + `CHAIN_APPROX_SIMPLE`）→ `drawContours` 以红色描边显示。

**`addlogo.py`** — 图像水印程序，提供三个函数：

- `add_watermark_with_bitwise()`：将水印叠加到指定位置，支持带 alpha 通道的 PNG 水印，通过 `multiply` + `add` 完成加权混合，并对越界坐标做钳制
- `create_text_watermark()`：用 `putText` 生成透明底的文字水印图
- `add_multiple_watermarks()`：在多个位置批量添加水印

> 混合公式为 `结果 = 水印 × alpha + 背景 × (1 - alpha)`，与图像处理的 alpha 合成一致。

### 综合应用

**`car_count.py`** — 视频车辆检测与计数。处理链路：

```
读取视频帧 → 高斯去噪 → KNN 背景建模 → 腐蚀 → 膨胀（3 次）
→ 形态学闭运算（2 次）→ 查找轮廓 → 面积与长宽比双重过滤 → 绘制框与面积
```

过滤条件：轮廓面积 > 700，且长宽比落在 `0.2 ~ 5.0` 之间——后者用于排除细长的误检区域（如车道线）。按 `Esc` 退出、`s` 保存当前帧。

> 代码中存在 `cv2.cvtColor(frame, ...)` 未接收返回值的写法（原意应为转灰度），以及 `findContours` 的第二个参数误传了形态学标志 `MORPH_CLOSE`。这些属于学习过程中的痕迹，保留原样以反映真实探索路径。

## 使用说明

1. 进入脚本目录：`cd OpenCV入门`
2. 准备测试素材：部分脚本依赖外部图片 / 视频，需自行放置
   - `first.py` → `cat.1.jpg`
   - `blur.py`、`contours.py` → `dog.293.jpg`
   - `thresh.py` → `cat.14.jpg`
   - `car_count.py` → `video.mp4`
   - `video_read.py` → `103236.mp4`
3. 运行脚本：`python first.py`

通用按键约定：`q` / `Esc` 退出，`s` 保存当前帧。脚本运行到 `waitKey` 时会等待按键，关闭窗口前请先按键退出，否则窗口可能无响应。

## 学习路线

仓库中的脚本大致遵循如下递进顺序：

```
图像读写与显示  →  交互控件（鼠标 / 滑动条）
      ↓
视频读写  →  绘图函数  →  阈值处理  →  滤波与边缘检测
      ↓
轮廓处理  →  图像合成（水印）  →  运动目标检测与计数
```

建议按「目录与知识点对照」表的顺序逐个运行，每步先看效果再读代码。

## 许可证

本项目采用 MIT License，详见 [LICENSE](LICENSE)。
