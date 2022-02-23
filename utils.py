def read(source_file):
        lst = []
        with open(source_file, 'r') as f:
            for line in f.readlines():
                line = line.strip()#去除收尾空格
                if not line: #去除空数据
                    continue
                if line == '\n':#去除空行
                    continue
                if line[0:2] == "//":#去除注释行
                    continue
                line = line.replace(' ', '')#去除中间的空格
                line = line.replace('\n', '')#去除末尾回车
                if line.find('//') != -1:
                    line = line[0:line.find('/')]#去除注释
                lst.append(line)
        return lst

def write(source_file, ml_lst):
        with open(source_file.replace('asm','hack'), 'w') as f:
            for line in ml_lst:
                f.write(line+'\n')