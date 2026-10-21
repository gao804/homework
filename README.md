# homework

高琴（20244080227）的 Python 作业，包含 EXP01、HW01、EXP02、HW02 的完整 Notebook、中文解题说明和实际运行结果。

## 作业文件

| 作业 | Notebook | 内容 |
| --- | --- | --- |
| EXP01 | [20244080227_高琴_exp01.ipynb](EXP01/20244080227_高琴_exp01.ipynb) | 基本运算、函数与循环、容器统计、文件与异常、类与复制，共五个实验 |
| HW01 | [20244080227_高琴_hw01.ipynb](HW01/20244080227_高琴_hw01.ipynb) | 简单函数、欧几里得算法、欧拉数近似、整数幂判断 |
| EXP02 | [20244080227_高琴_exp02.ipynb](EXP02/20244080227_高琴_exp02.ipynb) | NumPy 数组与索引、随机抽样与缺失值、SciPy 与 Matplotlib、pandas |
| HW02 | [20244080227_高琴_hw02.ipynb](HW02/20244080227_高琴_hw02.ipynb) | 字符串与列表函数、元组表示向量和矩阵、Vector 类 |

原题位于 [assignments](assignments/)。EXP01 的解析模块为 [student_utils.py](EXP01/student_utils.py)，输入及输出文件位于 [exp01_data](EXP01/exp01_data/)。

## 运行

在仓库根目录打开 Anaconda Prompt 或已配置 conda 的终端：

```bash
conda env create -f environment.yml
conda activate homework
python -m ipykernel install --sys-prefix --name homework --display-name "Python (homework)"
jupyter notebook
```

打开目标 Notebook，选择 `Python (homework)` 内核，然后“重启内核并运行全部单元”。通过 Jupyter 打开时，工作目录应为 Notebook 所在文件夹，EXP01 会在该目录生成 `exp01_data` 和 `student_utils.py`。

也可以在仓库根目录执行：

```bash
conda run --no-capture-output -n homework python scripts/run_notebooks.py
```

脚本为每个 Notebook 启动一个全新内核，按顺序运行所有代码单元；没有未捕获异常时保存运行结果。每个 Notebook 最后的检查单元会验证关键结果和边界输入。

环境文件固定了 pip 版 `pyzmq==26.4.0`：本机初次安装的 conda 版 pyzmq/ZeroMQ 组合启动内核时出现 `Bad file descriptor`，换用上述 wheel 后重新验证。

## 结果与复现

- EXP01：1 到 100 求和为 5050；6 条有效成绩、3 条无效记录；平均分 76.67，及格率 83.33%；无效记录行号为 8、9、10。
- HW01：三组指定输入的 GCD 分别为 1、300、60；级数前 0、1、4 项分别为 0.0、1.0、约 2.666667。
- GCD 额外与 `math.gcd` 对比了 -20 到 20 的全部数对；整数幂对底数 1 到 10、目标数 1 到 300 做了枚举对照；欧拉数近似检查了 0.1、0.001、0.000001、0.000000000001 四种误差要求。
- 运行记录中的机器指纹和 RUN_ID 由当前执行机器按题目公式生成，换电脑重新运行会改变，不是手写固定值。
- EXP01 每次先重写输入文件和报告，再演示追加模式；反复运行不会累积重复报告内容。

提交课程作业时使用上表中带学号、姓名的 `.ipynb` 文件。需要附带实验模块和数据时，可一并提交整个 `EXP01` 目录。
