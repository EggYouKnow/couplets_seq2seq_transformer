# Transformer Seq2Seq Couplets Model

用于写对联的 Transformer 序列到序列模型。

代码大部分基于 Kyubyong Park 老师的 Tensorflow 的 Transformer 实现（之前刚好发现了个bug，提交了issue）。

最主要的修改就是对数据处理进行了些改写，还有一些其他小地方。

## 运行要求

- NumPy >= 1.11.1
- TensorFlow >= 1.2 (我在1.6上进行的测试)
- nltk

## 文件描述

### 文件

  * `hyperparams.py` 超参数设定
  * `prepro.py` 预处理，创建词表
  * `data_load.py` 数据读入脚本
  * `modules.py` 各种搭建模块
  * `train.py` 训练脚本还有模型
  * `eval.py` 对评估集进行评估
  * `test.py` 对自己指定的只有上联的数据进行评估
  * `online.py` 实时的读入想要处理的上联，给出下联

### 文件夹

  * `results` 存放评估结果的地方
  * `data` 存放数据的地方
  * `logdir` 存放 checkpoint 和各种训练数据的地方

## 数据描述

数据 [**couplets**](https://drive.google.com/file/d/13cJWWp_ST2Xqt76pEr5ZWa6LVJwGYC4-/view?usp=sharing) 包含如下文件和文件夹：

- `train` 里面包含 770491 条上下联数据
- `test` 里面包含 4000 条上下联评估数据
- `vocab` 文件是预处理好的词表

对训练数据的字长进行统计后发现，大部分集中在5-10字左右，最长大概30字左右，所以训练的最大字长我选的也是30.

![](https://upload-images.jianshu.io/upload_images/4787675-38a5c92644e1864d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 训练
* 第一步，先下载对联数据 [**couplets**](https://drive.google.com/file/d/13cJWWp_ST2Xqt76pEr5ZWa6LVJwGYC4-/view?usp=sharing), 然后解压到 `data` 里去
* 第二步，自己调整超参数
* 第三步，运行`prepro.py`预处理数据，产生词表，也可以用提供的词表
* 第四步，运行`train.py`训练模型

## 评估

训练完之后，保存模型，评估脚本会自动读入最新模型来进行评估。

  * 运行 `eval.py` 来评估 `data` 里的评估集
  * 运行 `python test.py 指定文件` 来测试自己提供的评估集。文件格式是每行一句，只包含上联。
  * 运行 `online.py` 进入实时模式，实时输入一句上联，输出下联。

## 结果

### 评估数据结果

- source: 腾 飞 上 铁 ， 锐 意 改 革 谋 发 展 ， 勇 当 千 里 马 
- expected: 和 谐 南 供 ， 安 全 送 电 保 畅 通 ， 争 做 领 头 羊 
- got: 奋 进 开 篇 ， 激 情 发 展 促 和 谐 ， 更 上 一 层 楼

----

- source: 风 弦 未 拨 心 先 乱 
- expected: 夜 幕 已 沉 梦 更 闲 
- got: 月 影 常 怜 梦 亦 寒

----


- source: 花 梦 粘 于 春 袖 口 
- expected: 莺 声 溅 落 柳 枝 头 
- got: 月 光 照 在 水 云 间

----

- source: 一 句 相 思 吟 岁 月 
- expected: 千 杯 美 酒 醉 风 情 
- got: 几 杯 寂 寞 醉 春 秋

----


- source: 几 树 梅 花 数 竿 竹 
- expected: 一 潭 秋 水 半 屏 山 
- got: 一 帘 春 雨 一 帘 风

---


- source: 未 舍 东 江 开 口 咏 
- expected: 且 施 妙 手 点 睛 来 
- got: 不 知 南 海 放 心 歌

----


- source: 彩 屏 如 画 ， 望 秀 美 崤 函 ， 花 团 锦 簇 
- expected: 短 信 报 春 ， 喜 和 谐 社 会 ， 物 阜 民 康 
- got: 春 雨 似 诗 ， 听 莺 歌 燕 语 ， 燕 语 莺 歌

----


- source: 玉 液 
- expected: 金 波 
- got: 金 汤

### 提供数据结果

- 上联: 改革春风吹满地 
- 下联: 复兴大业富千家

----

-  上联: 中国人民真争气
-  下联: 大千世界不争雄

----


- 上联: 盘他  
- 下联: 还我   

----


- 上联: 我们一起学猫叫  
- 下联: 大众齐心做马人    

----


- 上联: 对联  
- 下联: 吟诗    

----


- 上联: 一人我饮酒醉  
- 下联: 两个他喝茶香    

----

- 飞雪连天射白鹿

- 落花遍地戏黄蜂

---

- 自然语言处理

- 无欲心思不通

## TODO

- [ ] 可以试试 Beam Search