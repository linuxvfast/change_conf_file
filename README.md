# change_conf_file

haproxy.py 为主配置文件

haproxy.txt 为需要修改的配置文件

删除的结构如下

backend www.test.com

		server 10.0.0.1  weight 10 maxconn 1000000
		
    
添加对应的信息也需要整体添加


查询只显示如上结构的信息
