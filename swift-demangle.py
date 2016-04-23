import idaapi
import subprocess

class SwiftDemangle(idaapi.action_handler_t):
    def __init__(self):
        idaapi.action_handler_t.__init__(self)

    def update(self, ctx):
        return idaapi.AST_ENABLE_ALWAYS

    def activate(self, ctx):
        print 'Starting Swift demangling'

        seg = idaapi.get_segm_by_name('.plt');
        # if seg == None:
        #     print 'Segment .plt was not found, exiting'
        #     return

        count = 0
        for funcea in Functions(seg.startEA, seg.endEA):
            func_name = GetFunctionName(funcea)[1:]
            demangled_output = self.demangle(func_name).split(' ---> ')

            name = demangled_output[0].strip()
            demangled_name = demangled_output[1].strip()

            if name == demangled_name:
                continue

            count += 1
            self.comment_xrefs(funcea, demangled_name)

        print 'Successfully demangled %d functions' % count

    def demangle(self, name):
        return subprocess.check_output(['C:/users/gulshan/winexecve.exe', '/bin/swift-demangle', name])
    def comment_xrefs(self, ea, comment):
        for xref in XrefsTo(ea):
            idaapi.add_long_cmt(xref.frm, 1, comment)

action_desc = idaapi.action_desc_t(
    'swift-demangle',
    'Demangle swift functions',
    SwiftDemangle(),
)

idaapi.register_action(action_desc)
idaapi.attach_action_to_menu(
    'Edit/Plugins/Jump to next fixup',
    'swift-demangle',
    idaapi.SETMENU_APP,
)
