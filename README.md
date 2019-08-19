# Color（色弱视觉渲染）

### 前景

随着19年第二代HoloLens的出现，我坚信HoloLens的开发以后会越来越普及。尽管现在硬件条件仍然十分困难，但也已经有了足以支持我们想法的技术。坚信编程可以改变很多事情，所以有了如下的项目。

### 原理

色弱患者是有矫正可能的，我们希望这个世界对于他们能够更加的精彩。通过重点针对色弱患者颜色辨识困难的区域，我们进行有区分度的、特定区域的进行渲染。从而让他们能够更好的辨识颜色。

### 功能块

1. 可根据语音进行模式的调整包括：

- 红、蓝、绿三色的色弱模式的选择
-  在某一色弱模式下进行矫正强弱的选择

2. 可以针对在光线较弱的地方进行辨识加强（神经卷积进行轮廓的勾选和强调）

其他的功能还有待开发