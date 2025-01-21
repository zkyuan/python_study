"""
 * @author: zkyuan
 * @date: 2025/1/21 11:31
 * @descipton: 包：模块分类管理
"""
import com
# 文件夹里面有“__init__.py”文件，
# 导包时首先执行“__init__.py”文件，控制包的导入行为,不要在里面写太多代码
# 当包被作为模块导入时，包目录下生成一个“__pycache__”文件夹
from com import *  # 导入时执行__init__.py

print(type(com))
register.registerFun()

# __all__：本质上是一个列表，可以控制要引入的东西
login.loginFun()

# 包中包含包
