# python_tutorial
the tutorial of python 

## ubuntu16.04安装多个python版本
安装完ubuntu16.04之后，系统自带了python2.x和python3.5，想要安装最新版的python3.6.3，所以采用了pyenv去管理多版本。
### 1.下载设置pyenv
```c
git clone https://github.com/yyuu/pyenv.git ~/.pyenv

//~/.bashrc设置环境变量
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

exec $SHELL -l
```

### 2. pyenv
```bash
pyenv install --list
pyenv install 版本号
pyenv rehash    //更新pyenv
pyenv versions  //已安装版本
pyenv globle 版本号    //设置全局版本
pyenv local 版本号     //局部版本
```

### 3.创建虚拟环境
```bash
pyenv virtualenv 3.4.3 TEST
pyenv activate TEST
pyenv deactivate
pyenv uninstall TEST
```

## vitualBox共享文件夹
```shell
mount -t vboxsf vmshare  ~/shared/
``` 
### 4. 安装matplotlib
- 在pyenv下安装
[详见](https://matplotlib.org/users/installing.html)
```shell
python -mpip install -U pip
python -mpip install -U matplotlib
```

- 错误：ModuleNotFoundError: No module named '_tkinter'
```shell
//1. 安装 tk-dev
apt-get install python3-tk
apt-get install tk-dev

//2.重新在pyenv下安装python
pyenv install 3.6.3

```
[详见](https://www.imooc.com/article/21754)



# RNG
http://www.chronox.de/jent/doc/CPU-Jitter-NPTRNG.html
https://lwn.net/Articles/642166/

# anaconda
https://www.jianshu.com/p/62f155eb6ac5
https://www.jianshu.com/p/2f3be7781451

# 
http://zkeeer.space/?p=192

# 正则小例子

My number is 0954 2079035

Your number is 0954-2079035

grep '0[0-9]\{3\}[ -][0-9]\{7\}' reg.txt