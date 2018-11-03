# 用来爬取《影》的评论

[pycharts](http://pyecharts.org/#/zh-cn/)
### aSpider

* 采用递归的方式更新url,直到爬到开映日期
### city_coordinates这里有个坑：
* 这个文件是记录坐标和地名的文件，主要为了生成geo这张图。
* github项目中的city_coordinate与本地的并不匹配，本地的文件存储在python库安装路径（"Lib\site-packages\pyecharts\datasets"这个路径下）。
* 目的是为了检索数据，去除和city_coordinates里面城市不一样的名字，不然会报错
* ps：暂时没有想到很好的修改名字的方法，不如统统去掉，大城市的名字一般不会错。
## 其他记录
### Geo地理坐标系
```python
'''
name -> str
图例名称
attr -> list
属性名称
value -> list
属性所对应的值
type -> str
图例类型，有'scatter', 'effectScatter', 'heatmap'可选。默认为 'scatter'
maptype -> str
地图类型。 从 v0.3.2+ 起，地图已经变为扩展包，支持全国省份，全国城市，全国区县，全球国家等地图，具体请参考 地图自定义篇
coordinate_region -> str
城市坐标所属国家。从 v0.5.7 引入，针对国际城市的地理位置的查找。默认为 中国。具体的国家/地区映射表参照 countries_regions_db.json。更多地理坐标信息可以参考 数据集篇
symbol_size -> int
标记图形大小。默认为 12
border_color -> str
地图边界颜色。默认为 '#111'
geo_normal_color -> str
正常状态下地图区域的颜色。默认为 '#323c48'
geo_emphasis_color -> str
高亮状态下地图区域的颜色。默认为 '#2a333d'
geo_cities_coords -> dict
用户自定义地区经纬度，类似如 {'阿城': [126.58, 45.32],} 这样的字典。
is_roam -> bool
是否开启鼠标缩放和平移漫游。默认为 True
如果只想要开启缩放或者平移，可以设置成'scale'或者'move'。设置成 True 为都开启
'''
add(name, attr, value,
    type="scatter",
    maptype='china',
    coordinate_region='中国',
    symbol_size=12,
    border_color="#111",
    geo_normal_color="#323c48",
    geo_emphasis_color="#2a333d",
    geo_cities_coords=None,
    is_roam=True, **kwargs)
    
```

###utf-8和utf-8-sig
Python 'utf-8-sig' Codec
This work similar to UTF-8 with the following changes:

* On encoding/writing a UTF-8 encoded BOM will be prepended/written as the
  first three bytes.

* On decoding/reading if the first three bytes are a UTF-8 encoded BOM, these
  bytes will be skipped.







### re模块：
re.sub()
分成子字符串
### jieba模块： 
Python 中文分词组件，把句子中所有的可以成词的词语都扫描出来
* jieba.cut 方法接受三个输入参数: 需要分词的字符串；cut_all 参数用来控制是否采用全模式；HMM 参数用来控制是否使用 HMM 模型
* jieba.lcut 以及 jieba.lcut_for_search 直接返回 list
### 
### 一些函数
#### join函数：
连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串。
#### replace函数：
Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
