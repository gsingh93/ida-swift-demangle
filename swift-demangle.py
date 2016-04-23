import idaapi
import subprocess

class myplugin_t(idaapi.plugin_t):
    flags = idaapi.PLUGIN_UNL
    comment = 'Demangles Swift function names'

    help = "Demangles Swift function names"
    wanted_name = "Swift function demangler"
    wanted_hotkey = "Ctrl-H"

    def init(self):
        return idaapi.PLUGIN_OK

    def run(self, arg):
        for funcea in Functions(SegStart(ScreenEA()), SegEnd(ScreenEA())):
            func_name = GetFunctionName(funcea)[1:]
            demangled_output = self.demangle(func_name).split(' ---> ')

            name = demangled_output[0].strip()
            demangled_name = demangled_output[1].strip()

            if name == demangled_name:
                continue

            self.comment_xrefs(funcea, demangled_name)

    def demangle(self, name):
        return subprocess.check_output(['C:/users/gulshan/winexecve.exe', '/bin/swift-demangle', name[0:]])

    def comment_xrefs(self, ea, comment):
        for xref in XrefsTo(ea):
            MakeComm(xref.frm, comment)

    def term(self):
        pass

def PLUGIN_ENTRY():
    return myplugin_t()
