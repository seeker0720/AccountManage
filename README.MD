## AccountManage账户信息管理器

![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/seeker0720/AccountManage?style=flat&logo=appveyor)![GitHub last commit](https://img.shields.io/github/last-commit/seeker0720/AccountManage?style=flat&logo=appveyor)![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/seeker0720/AccountManage?style=flat&logo=appveyor)![ Python version](https://img.shields.io/badge/python-3.6%2B-blue?style=flat&logo=appveyor)![GitHub](https://img.shields.io/github/license/seeker0720/AccountManage?style=flat&logo=appveyor)

用于管理用户的账户信息，如登录名，密码等，类似于Google密码管理器、Dashlane等，不同于这些线上应用，该程序只允许你在本地运行，所有信息都存储在本地MySQL数据库中

### 部署教程

> Tips教程都会使用这些约定来介绍:
>
> - AccountManage源码位置在 `$PATH`下，`$PATH`在这里仅代表源码所放路径
> - 数据库登入用户为`admin`
> - 数据库名称为`accountdb`
> - 数据库登录密码为`AccountManage123!@#`

#### 环境
`Windows7`  
`Python3+`  
`MySQL8.0+或MySQL5.7+`  
你需要安装相应的python解释器和MySQL数据库应用，当然你也可以在Linux系统下运行该程序，该教程仅针对Window系统。

#### 创建虚拟环境
打开命令行，将目录切换到AccountManage目录下，输入以下命令

```powershell
$PATH\AccountManage>virtualenv AM_env
```

执行完成后，会生成一个AM_env文件夹，




执行以下命令激活虚拟环境

```powershell
$PATH\AccountManage>.\AM_env\Scripts\activate
```



#### 安装依赖的第三方库

```powershell
(AM_env)$PATH\AccountManage>pip install -r requirements.txt
```

#### 创建数据库

启动MySQL数据库，分别输入以下命令，创建数据库  

登录数据库
```powershell
mysql -uroot -p
```
创建数据库和用户
```sql
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'AccountManage123!@#';
CREATE DATABASE `accountdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
GRANT all ON accountdb.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;
exit
```

如果MySQL版本是8.0的版本，第一行的SQL语句有些许改动：

```sql
CREATE USER 'admin'@'localhost' IDENTIFIED WITH mysql_native_password BY 'AccountManage123!@#';
```



上面的命令分别创建了数据库和用于登录的用户，你可以修改为你自己的，同时将settings.py文件中对应的部分修改

#### 修改settings.py文件

需要注意`DATABASES`中的数据

```python
DATABASES = {
    'default': {
        'DB_API': 'mysql+pymysql',
        'NAME': 'accountdb',
        'USER': 'admin',
        'PASSWORD': 'AccountManage123!@#',
        'HOST': 'localhost',
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}
```

需要修改的部分分别为`NAME`、`USER`、`PASSWORD`,修改为自己的即可

#### 创建管理员密码

将目录切换到`AccountManage\core\`下，输入以下命令创建管理员密码：

```powershell
(AM_env)$PATH\AccountManage\core\>python manage.py createpassword
```

#### 启动程序

创建管理员密码后，执行以下命令启动程序

```powershell
(AM_env)$PATH\AccountManage\core\>python manage.py runapp
```



##### 目录结构-v0.0.1

+ AccountManage /
  + AM_env /
  + core /
    + \_\_init__.py
    + auth.py
    + common.py
    + main.py
    + models.py
    + admin.py
    + get_command_line_argv.py
    + manage.py
  + conf /
    + \_\_init__.py
    + settings.py
  + docs /
    + \_\_init__.py
  + REDEME.md
  + requirements.txt



- **v0.0.1版本说明**
  - 程序能实现简单的用户账户信息管理，具有查询、删除、修改、添加等基本功能



