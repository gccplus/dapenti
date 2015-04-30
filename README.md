# dapenti
此脚本用于从[喷嚏图挂](http://www.dapenti.com/blog/index.asp) 抓取经典段子，只抓取了到2012年7月左右，大概2000+
,功能简单，当时纠结的主要是编码问题：

* requests抓取到的页面Content Type如果没有指定编码，那么会默认按照ISO-8859-1即latin1处理，而此网站用的是gbk编码，也恰好没有指定编码类型，所以出现了各种问题。
* print输出编码是系统的编码，一般windows默认是gbk，所以print时会有一个自动将unicode转换为gbk的过程，所以首先要保证string是unicode编码，gbk自动转换会有各种不能转换的特殊字符，需要手动encode，加上ignore参数 `s.encode('gbk', 'ignore')`
* 输出到文件一般是gbk或者utf-8，gbk比较操蛋，各种问题，一律使用utf-8,开头加上# -*- coding: utf-8 -*，文件中的中文都是utf-8了，还有一些从网页中读取的字符等，如果不是,需要encode成utf-8
* beautifulsoup的编码问题。任何HTML或XML文档都有自己的编码方式,比如ASCII 或UTF-8,但是使用BeautifulSoup解析后,文档都被转换成了Unicode。bs能够自动检测输入编码，但有时也会出问题，可以自己指定 `soup = BeautifulSoup(markup, from_encoding="iso-8859-8")`
