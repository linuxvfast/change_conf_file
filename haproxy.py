__author__ = 'linux vfast'
import re,json
filename = 'haproxy.txt'

def search(args):
    '''查找域名对应的信息'''
    with open(filename, "r",encoding='utf-8') as f:
        for line in f:
            if re.match("backend %s" % args.strip(), line):
                print(line.strip())
                print(f.readline())
                break
        else:
             print("Not Found '%s' in configure file" % args.strip())

def add_backend():
    '''添加域名对应的信息'''
    while True:
        daemon = input('请输入域名:')
        with open(filename,'r',encoding='utf-8') as f:
            f.seek(0)
            for line in f:
                if re.match("backend %s" % daemon.strip(), line):
                    print(daemon.strip()+'已经存在')
                    break
            else:
                daemon_server = input('请输入ip地址:')
                daemon_weight = input('请输入权重:')
                daemon_maxconn = input('请输入最大的链接数:')
                backend_info = 'backend '+ daemon +'\n'+'\t\t'+'server '+daemon_server+'  '+'weight '\
                                   +daemon_weight+' maxconn '+daemon_maxconn
                # print(backend_info)
                with open(filename, 'a', encoding='utf-8') as f:
                    f.writelines('\n'+backend_info)
                break

def delete_daemon():
    '''删除域名对应的信息'''
    while True:
        daemon = input('请输入域名:')
        with open(filename,'r',encoding='utf-8') as f:
            f.seek(0)
            ss = []
            for line in f:
                if re.match("backend %s" % daemon.strip(), line):
                    # print(line.strip()+'\n'+'\t\t'+f.readline())
                    # delete_search = line.strip()+'\n'+'\t\t'+f.readline()
                    f.readline()
                    continue
                else:
                    ss.append(line)
            # with open('haproxy.json', 'w', encoding='utf-8') as f_file:
            #     json.dump(ss,f_file)
            with open('haproxy.txt', 'w', encoding='utf-8') as f_file:
                for line in ss:
                    f_file.write(line)
            break





if __name__ == '__main__':
    while True:
        choise = input("What are you do? (add|delete|search|q):")
        if choise == "search":
            args = input("Input backend name:")
            if args:
                search(args)
            else:
                print("格式错误!")
        elif choise == "add":
            add_backend()
        elif choise == 'delete':
            delete_daemon()
        elif choise == "q":
            break
        else:
            print('输入错误，请重新输入')
            continue
