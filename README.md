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

