# 湾区日报 alfred workflow

## 写在前面说明

这是一个非官方的插件, 方便自己使用, 顺便练练手.

官方网站: [https://wanqu.co](https://wanqu.co)

官方app: [https://itunes.apple.com/app/apple-store/id995762924](https://itunes.apple.com/app/apple-store/id995762924)

~~在Alfred3上开发, 不向下兼容..~~
支持Alfred2+

## 介绍

提供三个及其简单的功能, 来查阅当前最新一期, 指定具体某一期或者5篇随机的文章.

![湾区日报 alfred workflow](https://raw.githubusercontent.com/yPangXie/wanqu-workflow/master/screenshot/wanqu-screenshot.png)

## 使用方法

 - 直接现在文件中的`wanqu.alfredworkflow` 或者从`Packal`下载:[湾区日报](http://www.packal.org/workflow/wan-qu-ri-bao-fei-guan-fang)
 - 依次打开`Alfred`, `Preferences`, `Workflows`
 - 将`wanqu.alfredworkflow`拖拽进去即可

```bash
# 获取最新一期的数据
wq l

# 获取5篇随机文章
wq r

# 获取具体某一期的文章
wq 100
```

## 更新日志

**v4.1.0 (2016/07/24)**

 - 小优化: 当输入的指令不合法时, 不再发送请求, 直接返回错误提示.

**v4.0.0 (2016/07/12)**

 - fix: 输入指定期数, 可能发送多次请求
 - refactor: 添加`workflow`内置的版本号和描述信息

**v3.0.0 (2016/07/04)**

 - feat: 支持`wq r`命令: 获取历史所有文章中的任意5篇(跨所有期)

**v2.x.x及之前版本 (2016/06/01~2016/06-04)**

 - feat: 支持`wq l`命令: 获取最新一期的数据
 - feat: 支持`wq n`命令: 替换`n`为指定期数, 获取对应的文章

## 其他

没有直接从湾区日报网站拿数据, 绕了一下. 请求会发给我的一个小工具`NaSha`. 他来完成页面抓取, 页面数据提取等操作.
