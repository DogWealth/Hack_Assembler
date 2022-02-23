from utils import write, read
from Assembly import Assembly

class Assembler:
    def __init__(self, source_file):
        self.source_file = source_file
        self.assembly_lst = read(source_file)
        self.first_pass()
        self.second_pass()
    
    def first_pass(self):
        count = 0
        for i, assembly in enumerate(self.assembly_lst[:]):
            if assembly[0] == '(':
                Assembly.symbol_table[assembly[1:assembly.find(')')]] = f'{i - count}'
                self.assembly_lst.remove(assembly)
                count += 1

    def second_pass(self):
        index = 16
        for assembly in self.assembly_lst[:]:
            if Assembly(assembly).is_aInstruction():
                s = assembly[1:]
                if not s.isdigit() and s not in Assembly.symbol_table:
                    Assembly.symbol_table[s] = f'{index}'
                    index += 1

    def translate(self):
        machine_language = []
        for a in self.assembly_lst:
            assembly = Assembly(a).construct()
            machine_language.append(assembly.translate())
        write(self.source_file.replace('asm', 'hack'), machine_language)
        return machine_language

    def __repr__(self):
        s = ''
        for line in self.assembly_lst:
            s += repr(line) + '\n'
        return s


