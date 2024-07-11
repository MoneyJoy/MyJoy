### learn-git

#### 基本命令

`git init` 创建仓库

`git status`  查看仓库的状态

`git add` 添加到暂存区（可是使用通配符添加所有同一后缀的文件），`git add .` 表示提交所有文件。

`git commit` 提交（只会提交在缓存区的文件），需要用 `-m` 输入提交信息。

`git log` 查看提交记录

##### 版本

###### `git reset` 回退版本

`git reset --soft` soft表示回退到某一个版本并且保存工作区和暂存区的内容

`git reset --hard` hard表示回退到某一个版本并且丢弃工作区和暂存区的内容

`git reset --mixed` mixed表示回退到某一个版本并且只保留工作区的内容

###### `git diff` 查看差异

默认查看工作区和暂存区

`git diff HEAD` 查看工作区和仓库

`git diff cached` 查看暂存区和仓库

`git diff` 后面加上两次版本的提交ID可以比较两个版本直接的差异

##### 文件操作

###### 删除版本库中的文件

方法一：

- 先用 rm 删除工作区的文件
- 使用 `git add <file>` 更新暂存区
- 最后提交

方法二：

- `git rm <file>` 删除工作区和暂存区
- **最后记得提交**

###### 忽略文件

`.gitignore` 按行从上到下进行匹配

#### 远程仓库

##### `GitHub`

**拉取推送**

`git pull` 

`git push` 

**本地推送操作**

- `git remote add origin <.git地址>` 

- `git remote -v` 

- `git push -u origin master` 

拉取更新：`git pull <远程仓库名><远程分支名>:<本地分支名>`

**分支**

`git branch <分支名>` 创建分支

`git switch <分支名>` 切换分支 

`git merge <被合并分支>` 合并分支，在 `main` 分支中使用命令

`git branch -d` 删除分支

`git rebase <目标分支>` 从分叉点之后接到目标分支
