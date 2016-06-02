# 湾区日报 alfred workflow

## 写在前面说明

这是一个非官方的插件, 方便自己使用, 顺便练练手.

官方网站: [https://wanqu.co](https://wanqu.co)

官方app: [https://itunes.apple.com/app/apple-store/id995762924](https://itunes.apple.com/app/apple-store/id995762924)

**在Alfred3上开发, 不向下兼容..**

## 介绍

提供两个及其简单的功能, 来查阅当前最新一期或指定具体某一期的文章列表.

![湾区日报 alfred workflow](https://raw.githubusercontent.com/yPangXie/wanqu-workflow/master/screenshot/wanqu-screenshot.png)

## 使用方法

 - 直接现在文件中的`wanqu.alfredworkflow` 或者从`Packal`下载:[湾区日报](http://www.packal.org/workflow/wan-qu-ri-bao-fei-guan-fang)
 - 依次打开`Alfred`, `Preferences`, `Workflows`
 - 将`wanqu.alfredworkflow`拖拽进去即可

```bash
# 获取最新一期的数据
wq l

# 获取具体某一期的文章
wq 100
```

## 其他

没有直接从湾区日报网站拿数据, 绕了一下. 请求会发给我的一个小工具`NaSha`. 他来完成页面抓取, 页面数据提取等操作.
