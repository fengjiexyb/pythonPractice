
Python序列化

#持久化

所谓持久化就是把内存中的数据保存在外存（包括数据库）中，达到长期保存的目的。

#序列化
序列化就是讲数据转换为可以通过网络传输或者可以存储到本地磁盘的数据格式（例如xml、json、字符串等）
Python常用的序列化模块有json、pickle、shelve。
#比较
|模块名称|	描述|	提供的api|  |
|----|----|	----|---|
|json|	用于实现Python数据类型与通用（json）字符串之间的转换	|dumps()、dump()、loads()、load()|不能转换自定义类型。明文保存，保密性差|
|pickle	|用于实现Python数据类型与Python特定二进制格式之间的转换	|dumps()、dump()、loads()、load()|不能用于Python之外|
|shelve	|专门用于将Python数据类型的数据持久化到磁盘，shelve是一个类似dict的对象，操作十分便捷|	open()|只能用在Python中|

#json
##接口
json模块提供了以下两个方法来进行序列化和反序列化操作：
```
# 序列化：将Python对象转换成json字符串
dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)

# 反序列化：将json字符串转换成Python对象
loads(s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
```
除此之外，json模块还提供了两个额外的方法允许我们直接将序列化后得到的json数据保存到文件中，以及直接读取文件中的json数据进行反序列化操作：
```
# 序列化：将Python对象转换成json字符串并存储到文件中
dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)

# 反序列化：读取指定文件中的json字符串并转换成Python对象
load(fp, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
```
##JSON与Python之间数据类型对应关系

###Python转JSON

|Python	|JSON|
|---|---|
|dict|	Object|
|list, tuple|	array|
|str|	string|
|int, float, int- & float-derived Enums|	numbers|
|True|	true|
|False|	false|
|None|	null|
###JSON转Python

|JSON|	Python|
|--|--|
|object|	dict|
|array|	list|
|string|	str|
|number(int)|	int|
|number(real)|	float|
|true|	True|
|false|	False|
|null|	None|
##注意
> 
* Python dict中的非字符串key被转换成JSON字符串时都会被转换为小写字符串；
* 自定义类型不能直接转换，比较麻烦。[参考](http://www.cnblogs.com/yyds/p/6563608.html)
* sort_keys参数： 表示序列化时是否对dict的key进行排序（dict默认是无序的）
* indent参数： 表示缩进的意思，它可以使得数据存储的格式变得更加优雅、可读性更强；。[参考](http://www.cnblogs.com/yyds/p/6563608.html)

# pickle
json和pickle都不能追加数据。

pickle模块提供的几个序列化/反序列化的函数与json模块基本一致：
```
# 将指定的Python对象通过pickle序列化作为bytes对象返回，而不是将其写入文件
dumps(obj, protocol=None, *, fix_imports=True)

# 将通过pickle序列化后得到的字节对象进行反序列化，转换为Python对象并返回
loads(bytes_object, *, fix_imports=True, encoding="ASCII", errors="strict")

# 将指定的Python对象通过pickle序列化后写入打开的文件对象中，等价于`Pickler(file, protocol).dump(obj)`
dump(obj, file, protocol=None, *, fix_imports=True)

# 从打开的文件对象中读取pickled对象表现形式并返回通过pickle反序列化后得到的Python对象
load(file, *, fix_imports=True, encoding="ASCII", errors="strict")
```
pickle编码协议[参考](http://www.cnblogs.com/yyds/p/6563608.html)
# shelve

shelve类似key-value数据库，内部是通过pickle协议来实现数据序列化。shelve只有一个open()函数，返回一个shelf对象。shelf是一种持久的、类似字典的对象。它与“dbm”的不同之处在于，其values值可以是任意基本Python对象--pickle模块可以处理的任何数据。keys是普通的字符串。
```
open(filename, flag='c', protocol=None, writeback=False)
```
flag 参数表示打开数据存储文件的格式，可取值与dbm.open()函数一致：

|值	|描述|
|---|---|
|'r'|	以只读模式打开一个已经存在的数据存储文件|
|'w'|	以读写模式打开一个已经存在的数据存储文件|
|'c'|	以读写模式打开一个数据存储文件，如果不存在则创建|
|'n'|	总是创建一个新的、空数据存储文件，并以读写模式打开|

protocol 参数表示序列化数据所使用的协议版本，默认是pickle v3；
writeback 参数表示是否开启回写功能。(下面会说)

我们可以把shelf对象当dict来使用--存储、更改、查询某个key对应的数据，当操作完成之后，调用shelf对象的close()函数即可。当然，也可以使用上下文管理器（with语句），避免每次都要手动调用close()方法。

shelve模块可以看做是pickle模块的升级版，因为shelve使用的就是pickle的序列化协议，但是shelve比pickle提供的操作方式更加简单、方便。shelve模块相对于其它两个模块在将Python数据持久化到本地磁盘时有一个很明显的优点就是，它允许我们可以像操作dict一样操作被序列化的数据，而不必一次性的保存或读取所有数据。
