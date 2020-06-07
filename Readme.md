# Software Testing Visual Platform
![python](https://img.shields.io/badge/python-3.7-green)
![GroupInfo](https://img.shields.io/badge/Group%20Size-3-orange)
## 运行环境

- python版本要求: python 3.7
- python库要求: requirements.txt

```shell script
pip install -r requirements.txt 
```

## 目录结构

```text
.
├── app                     # 项目主目录
│   ├── app.py              # app入口文件
│   ├── controller          # 控制层
│   │   ├── __init__.py     # api命名空间注册
│   │   └── demo.py
│   ├── model               # 实体层
│   │   └── demo.py
│   └── service             # 业务逻辑层
│       └── demo.py
└── start.py                # 项目启动文件
```

