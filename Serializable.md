
Python���л�
# �־û�
��ν�־û����ǰ��ڴ��е����ݱ�������棨�������ݿ⣩�У��ﵽ���ڱ����Ŀ�ġ�
# ���л�
���л����ǽ�����ת��Ϊ����ͨ�����紫����߿��Դ洢�����ش��̵����ݸ�ʽ������xml��json���ַ����ȣ�
Python���õ����л�ģ����json��pickle��shelve��
# �Ƚ�

|ģ������|	����|	�ṩ��api|  |
|----|----|	----|---|
|json|	����ʵ��Python����������ͨ�ã�json���ַ���֮���ת��	|dumps()��dump()��loads()��load()|����ת���Զ������͡����ı��棬�����Բ�|
|pickle	|����ʵ��Python����������Python�ض������Ƹ�ʽ֮���ת��	|dumps()��dump()��loads()��load()|��������Python֮��|
|shelve	|ר�����ڽ�Python�������͵����ݳ־û������̣�shelve��һ������dict�Ķ��󣬲���ʮ�ֱ��|	open()|ֻ������Python��|

# json
##�ӿ�
jsonģ���ṩ�����������������������л��ͷ����л�������
```
# ���л�����Python����ת����json�ַ���
dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)

# �����л�����json�ַ���ת����Python����
loads(s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
```
����֮�⣬jsonģ�黹�ṩ����������ķ�����������ֱ�ӽ����л���õ���json���ݱ��浽�ļ��У��Լ�ֱ�Ӷ�ȡ�ļ��е�json���ݽ��з����л�������
```
# ���л�����Python����ת����json�ַ������洢���ļ���
dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)

# �����л�����ȡָ���ļ��е�json�ַ�����ת����Python����
load(fp, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
```
## JSON��Python֮���������Ͷ�Ӧ��ϵ

### PythonתJSON

|Python	|JSON|
|---|---|
|dict|	Object|
|list, tuple|	array|
|str|	string|
|int, float, int- & float-derived Enums|	numbers|
|True|	true|
|False|	false|
|None|	null|
### JSONתPython

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
## ע��
> 
* Python dict�еķ��ַ���key��ת����JSON�ַ���ʱ���ᱻת��ΪСд�ַ�����
* �Զ������Ͳ���ֱ��ת�����Ƚ��鷳��[�ο�](http://www.cnblogs.com/yyds/p/6563608.html)
* sort_keys������ ��ʾ���л�ʱ�Ƿ��dict��key��������dictĬ��������ģ�
* indent������ ��ʾ��������˼��������ʹ�����ݴ洢�ĸ�ʽ��ø������š��ɶ��Ը�ǿ����[�ο�](http://www.cnblogs.com/yyds/p/6563608.html)

# pickle
json��pickle������׷�����ݡ�

pickleģ���ṩ�ļ������л�/�����л��ĺ�����jsonģ�����һ�£�
```
# ��ָ����Python����ͨ��pickle���л���Ϊbytes���󷵻أ������ǽ���д���ļ�
dumps(obj, protocol=None, *, fix_imports=True)

# ��ͨ��pickle���л���õ����ֽڶ�����з����л���ת��ΪPython���󲢷���
loads(bytes_object, *, fix_imports=True, encoding="ASCII", errors="strict")

# ��ָ����Python����ͨ��pickle���л���д��򿪵��ļ������У��ȼ���`Pickler(file, protocol).dump(obj)`
dump(obj, file, protocol=None, *, fix_imports=True)

# �Ӵ򿪵��ļ������ж�ȡpickled���������ʽ������ͨ��pickle�����л���õ���Python����
load(file, *, fix_imports=True, encoding="ASCII", errors="strict")
```
pickle����Э��[�ο�](http://www.cnblogs.com/yyds/p/6563608.html)
# shelve

shelve����key-value���ݿ⣬�ڲ���ͨ��pickleЭ����ʵ���������л���shelveֻ��һ��open()����������һ��shelf����shelf��һ�ֳ־õġ������ֵ�Ķ������롰dbm���Ĳ�֮ͬ�����ڣ���valuesֵ�������������Python����--pickleģ����Դ�����κ����ݡ�keys����ͨ���ַ�����
```
open(filename, flag='c', protocol=None, writeback=False)
```
flag ������ʾ�����ݴ洢�ļ��ĸ�ʽ����ȡֵ��dbm.open()����һ�£�

|ֵ	|����|
|---|---|
|'r'|	��ֻ��ģʽ��һ���Ѿ����ڵ����ݴ洢�ļ�|
|'w'|	�Զ�дģʽ��һ���Ѿ����ڵ����ݴ洢�ļ�|
|'c'|	�Զ�дģʽ��һ�����ݴ洢�ļ�������������򴴽�|
|'n'|	���Ǵ���һ���µġ������ݴ洢�ļ������Զ�дģʽ��|

protocol ������ʾ���л�������ʹ�õ�Э��汾��Ĭ����pickle v3��
writeback ������ʾ�Ƿ�����д���ܡ�(�����˵)

���ǿ��԰�shelf����dict��ʹ��--�洢�����ġ���ѯĳ��key��Ӧ�����ݣ����������֮�󣬵���shelf�����close()�������ɡ���Ȼ��Ҳ����ʹ�������Ĺ�������with��䣩������ÿ�ζ�Ҫ�ֶ�����close()������

shelveģ����Կ�����pickleģ��������棬��Ϊshelveʹ�õľ���pickle�����л�Э�飬����shelve��pickle�ṩ�Ĳ�����ʽ���Ӽ򵥡����㡣shelveģ���������������ģ���ڽ�Python���ݳ־û������ش���ʱ��һ�������Ե��ŵ���ǣ����������ǿ��������dictһ�����������л������ݣ�������һ���Եı�����ȡ�������ݡ�
