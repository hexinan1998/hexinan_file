# Git

------

## 工作流程图

![](D:\download_git\hexinan_study\git_and_linux\img1.png) 

## 第一次使用

```bash
1. 首先你要做的是  把你的ssh 公钥交给 git；  "只用做一次， 提交公钥"  
	linux or mac可以在终端：
	ssh-keyhen -t rsa -C "userEmal@xxx.com"
	cd ~/.ssh
	cat id_ras.pub
	windows 需要在 gitbash 这个命令窗口下执行上述命令
	之后会直接显示一串字符，这串字直接复制过去

2. 第一次 使用时需要告诉  git  你的名字与你的邮箱 "只用做一次"
	git config --global user.name "username"
	git config --global user.email "you@com"
3. 选定文件夹初始化一个本地仓库  git init

4. 写测试文件 ，提交进入暂存区 git add <file>
5. 在本地提交进分支  git commit -m <message>
6. 从本地把它推到 remote 
	git remote add origin git@github.com:hexinan1998/hexinan_file.git   从本地到远程关联github服务器 （只须关联一次）
	git push -u origin master
	由于第一次推送所以要加 -u  git不但会把本的master 分支内容推送带远程新的master分支
	还会把本地的master分支和远程的master 分支关联起来，在以后的推送或者拉取是就可以直接简化命令
	
7. 克隆
	git clone git@github.com:hexinan1998/hexinan_file.git
	如果是第一次  从git克隆文件，会有 worning 将git主机的公钥添加进入主机列表
```

## 命令集合

```bash
git  	
	--version 				查看版本号
	--healp					帮助
	clone 					克隆一个存储库到新目录
	init  					初始化一个存储库
	config --global  	 	 全局配置  下面主要使用两个配置：user.name  user.email
	add  file   		 	 将文件添加进入本地仓库 (添加一个新的内容进入索引)
	mv  					移动或者重命名一个文件，一个目录，或者一个符号链接
	rm  					删除一个文件来自文件树或者来自一个索引,命令git rm用于删除一个文件。
					    	如果一个文件已经被提交到版本库，那么你永远不用担心误删，但是要小心，你只能恢复文件到最新版本 
	commit 					记录仓库的改变（ 版本号 ）
	log  				 	打印仓库的改变
		append GPL  	 	 最近一次的版本
		add distributed   	 上一次的版本
		--pretty=oneline      打印所有版本 ， 漂亮的一行
	branch                    集合   创建  或者 删除 -d 一个分支
	
	pull  					从远程把文件拉到本地
	push  					从本地把文件推到远程
	reset /* git reset --hard commit_id  */  重新设置版本库中存储的头指针指向  想要指向的版本;
	status   				查看当前工作区的状态
	checkout /*git checkout -- file */  文件会回到最近一次的 git add 或者 git commit 的状态 丢弃工作区的修改
	#  git checkout --file命令中的--很重要，没有--，就变成了“切换到另一个分支”的命令，我们在后面的分支管理中会再次遇到git checkout命令。
	#  git reset HEAD <file> 既可以把版本回退也可以把暂存区的修改撤销掉 （unstage）ex
	#  丢弃暂存区的修改
	
```

区分 chackout 与  reset

场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令git checkout -- file。

场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令git reset HEAD <file>，就回到了场景1，第二步按场景1操作。

场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退一节，不过前提是没有推送到远程库

## 分支管理

```bash
#项目不会有很多同事一起开发，如果我负责的部分没有写完但是我想提交，但是不完整的提交会对其他同事的部分。
#这就有了分支，每个人都有自己的分支，想提交就提交，直到开发完整再与主分支合并，这样既安全有不会影响别人开发。

#创建与合并分支
查看分支： 
git branch

创建分支： 
git branch <name>

切换分支： 
git checkout <name>或者git switch <name>

创建+切换分支： 
git checkout -b <name>或者git switch -c <name>

合并某分支到当前分支： 
git merge <name>

删除分支： 
git branch -d <name>
```

资料引用

https://www.liaoxuefeng.com/wiki/896043488029600

https://www.cnblogs.com/imyalost/p/8762522.html

https://www.runoob.com/git/git-tutorial.html