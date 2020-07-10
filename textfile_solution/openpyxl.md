# 使用openpyxl模块

## 在openpyxl中主要用到如下3个概念

```text
a. Workbook
    代表一个Excel工作表
b. Worksheet
    代表工作表中的一页
c. Cell
    代表最简单的一个单元格
```

### Workbookd对象

```text
a. active
    获取当前活跃的Worksheet
b. worksheets
    以列表的形式返回所有的Worksheet
c. read_only
    判断是否以read_only模式打开Excel文档
d. encoding
    获取文档的字符集编码
e. properties
    获取文档的元数据，如标题、创建者、创建日期等
f. sheetnames
    获取工作簿中的表（列表）
```

### Worksheet对象

```text
a. title
    表示表格的标题
b. dimensions
    表示表格的大小，这里的大小是指含数据的表格大小，即，左上角的坐标和右下角的坐标
c. max_row
    表示表格的最大行数
d. min_row
    表示表格的最小行数
e. rows
    按行获取单元格
f. max_column
    表示表格的最大列数
g. min_column
    表示表格的最小列数
h. columns
    按列获取单元格
i. freeze_panes
    冻结窗格
j. values
    按行获取表格的内容
```

### Cell对象

```text
a. row
    表示单元格所在的行
b. column
    表示单元格所在的列
c. value
    表示单元格的值
d. coordinate
    表示单元格的坐标
```