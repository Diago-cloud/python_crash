#Python编程从入门到实践
###第二章   变量和简单数据类型
####2.2变量
    1）变量名只能包含字母、数字和下划线。不能以数字打头。
    2）变量名不能包含空格，可以用下划线来分隔其中单词。
    3）不要将Python关键字和函数名用作变量名。
#####2.3字符串
    1）字符串就是一系列字符。用引号括起的都是字符串，可以是单引号也可以是双引号
    2）方法是Python可对数据执行的操作。每个方法后面都跟着一对括号，
            这是因为方法通常需要额外的信息来完成其工作
        2-1）title（）将每个单词的首字母都改成大写。upper（）lower（）
    3）Python使用加号（+）来合并字符串,这种合并字符串的方法称为拼接
    4）空白泛指任何非打印字符，如空格、制表符和换行符。
        4-1）确保字符串末尾没有空白u，可使用方法rstrip（），这种删除是暂时的。
            剔除字符串开头的空白，使用方法lstrip（）
            剔除字符串两端的空白，使用方法strip（）
####2.4数字
    1）Python使用两个乘号表示乘方运算。
    2）Python将带小数点的数字都成为浮点数。
    3）将非字符串值表示为字符串调用函数str（）
    4）计算整数结果时，不是四舍五入而是删除小数部分
####2.5注释
    1）用（#）表示注释
    The Zen of Python, by Tim Peters
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
###第三章   列表类型
####3.1列表是什么
    1）列表是由一系列按特定顺序排列的元素组成。
    2）用（[]）表示列表，用逗号来分隔其中的元素
    3）访问最后一个列表元素索引可以特殊指定为-1，以此类推
    4)

    
