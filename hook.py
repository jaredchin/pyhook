"""
这个模块构造了一个方便调用的监控键鼠事件的函数库,以及热键。
by 原照萌
"""
from baseconst import *

# global variables
threadId = 0  # 当前进程id
hhooks = {"m": 0, "k": 0}  # handle of hooks
cbf_keyboard = None  # the cbf jut mean Callback function
cbf_mouse = None
usercbf_keyboard = None
usercbf_mouse = None
cbf_hotkey = None




# -------------------------------------------------

def starthook(hooktype):
    """
    WH_KEYBOARD_LL = 13 # install a hook for lowlevel keyboard input event
    WH_MOUSE_LL = 14 # isntall a hook for lowlevel mouse input event
    """
    hooktype = hooktype.lower()
    if hooktype == "m":
        hooktypeId = 14
        callfunc = cbf_mouse
        if not callable(usercbf_mouse):
            raise Exception("you must set the callback function.")
    elif hooktype == "k":
        hooktypeId = 13
        callfunc = cbf_keyboard
        if not callable(usercbf_keyboard):
            raise Exception("you must set the callback function.")
    else:
        raise Exception("hooktype must 'be mouse' or 'keyboard'.")

    thhook = SetWindowsHookEx(hooktypeId, callfunc, GetModuleHandle(c_void_p(None)), 0)
    if thhook == 0:
        raise Exception("SetWindowsHookEx failed!")
    else:
        hhooks[hooktype] = thhook


def mainloop():
    global threadId
    threadId = GetCurrentThreadId()
    msg = MSG()
    while GetMessage(byref(msg), c_void_p(None), 0, 0) > 0:
        if msg.message == WM_UNLOCKMS:
            if hhooks['m'] != 0:
                ret = UnhookWindowsHookEx(hhooks['m'])  # if function succeed.return nonzero
                if ret == 0:
                    raise Exception("UnhookWindowsHookEx failed.")
                hhooks['m'] = 0
        elif msg.message == WM_UNLOCKKB:
            if hhooks['k'] != 0:
                ret = UnhookWindowsHookEx(hhooks['k'])  # if function succeed.return nonzero
                if ret == 0:
                    raise Exception("UnhookWindowsHookEx failed.")
                hhooks['k'] = 0
        elif msg.message == WM_HOTKEY:
            cbf_hotkey()
        elif msg.message == WM_READYCLOSE:
            closeloop()
        TranslateMessage(byref(msg))
        DispatchMessage(byref(msg))

def stophook(hooktype,cl=False):
    if hooktype == 'm':

        PostThreadMessage(threadId, WM_UNLOCKMS, 0, 0)
    elif hooktype == 'k':
        PostThreadMessage(threadId, WM_UNLOCKKB, 0, 0)
    else:
        Exception("hooktype can only be 'm' or 'k'.")
    if cl:
        PostThreadMessage(threadId, WM_READYCLOSE, 0, 0)

def closeloop():
    global threadId
    if threadId != 0:
        PostThreadMessage(threadId, WM_QUIT, 0, 0) # Psot WM_QUIT message to mainloop
        threadId = 0


def keyboardproc(nCode, wParam, lParam):
    Param = lParam.contents

    args={'keystatu': wParam, 'keycode': Param.vkCode,
          'scancode': Param.scanCode, 'flags': Param.flags}
    ret = usercbf_keyboard(args)

    if ret == 0:  # return 0 for not to block ,other to block
        CallNextHookEx(hhooks['k'], nCode, wParam, lParam)
        return 0
    else:
        return 1

def mouseproc(nCode, wParam, lParam):
    Param = lParam.contents
    args = {'keystatu': wParam, 'x': Param.pt.x, 'y': Param.pt.y,
            'mouseData': Param.mouseData >> 16}

    ret = usercbf_mouse(args)
    if ret == 0:
        CallNextHookEx(hhooks['m'], nCode, wParam, lParam)
        return 0
    else:
        #CallNextHookEx(hhooks['m'], nCode, wParam, lParam)
        return 1

def setcbf(myfunc, hooktype):
    global usercbf_keyboard, usercbf_mouse, cbf_keyboard, cbf_mouse

    if hooktype.lower() == "k":
        usercbf_keyboard = myfunc
        keyfunctype = WINFUNCTYPE(c_int, c_int, c_int, POINTER(KBDLLHOOKSTRUCT))
        cbf_keyboard = keyfunctype(keyboardproc)
    elif hooktype.lower() == "m":
        usercbf_mouse = myfunc
        keyfunctype = WINFUNCTYPE(c_int, c_int, c_int, POINTER(MSLLHOOKSTRUCT))
        cbf_mouse = keyfunctype(mouseproc)


def sethotkey(func, hotid, mode, vkcode):
    # mode neel selected from mod.
    global cbf_hotkey
    cbf_hotkey = func
    ret = RegisterHotKey(c_void_p(None), hotid, mode, vkcode)
    if ret == 0:
        raise Exception("RegisterHotKey failed.")

def unsethotkey(hotid):
    ret = UnregisterHotKey(c_void_p(None),hotid)
    if ret == 0:
        raise Exception("UnregisterHotKey failed.")


# test keyboard hook
if __name__ == '__main__':
    def testcallbackfunc(args):
        print("vkCode:", args["keycode"])
        if args["keycode"] == 81:
            closeloop()
        return 0
    setcbf(testcallbackfunc)
    starthook('k')
    print('start loop,press Q to exit.')
    mainloop()
    print('unlock hook.')

